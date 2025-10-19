from flask import Flask, jsonify, request
import conexao

app = Flask(__name__)
bd = conexao



@app.route('/tasks', methods=['GET'])
def obterTarefas():
    conn = None
    cur = None

    try:
        conn = bd.conectar()

        if conn is None:
            return jsonify({"mensagem": "Erro ao conectar ao banco de dados."}), 500

        cur = conn.cursor()

        cur.execute("SELECT * FROM tarefas;")
        query = cur.fetchall()
        
        tarefasFormatadas = []
        for tarefa in query:
            tarefasFormatadas.append ({
                "id": tarefa[0],
                "title": tarefa[1],
                "description": tarefa[2],
                "status": tarefa[3],
                "createdAt": tarefa[4]
            })
        return jsonify(tarefasFormatadas)
    except Exception as e:
        return jsonify({"mensagem": f"Erro ao obter tarefas: {e}"}, 500)
    finally:
        bd.desconectar(cur, conn)

      

@app.route('/tasks/<int:id>', methods=['GET'])
def obterTarefaEspecifica(id):
    conn = None
    cur = None

    try:
        conn = bd.conectar()

        if conn is None:
            return jsonify({"mensagem": "Erro ao conectar ao banco de dados."}), 500

        cur = conn.cursor()

        cur.execute("SELECT * FROM tarefas WHERE id = %s;", (id,))
        query = cur.fetchone()

        if query is None:
            return jsonify({"mensagem": "Tarefa nao encontrada."}), 404

        tarefa_dict = {
            "id": query[0],
            "title": query[1],
            "description": query[2],
            "status": query[3],
            "createdAt": query[4]
        }

        return jsonify(tarefa_dict)
    except Exception as e:
        return jsonify({"mensagem": f"Erro ao obter tarefa: {e}"}, 500)
    finally:
        bd.desconectar(cur, conn)


@app.route('/tasks', methods=['POST'])
def criarTarefa():
    conn = None
    cur = None
    description = None

    novaTarefa = request.get_json(silent=True)

    if not novaTarefa:
        return jsonify({"mensagem": "Erro ao criar tarefa. Dados inválidos."}), 400

    if not novaTarefa.get('title'):
        return jsonify({"mensagem": "Erro ao criar tarefa. Título é obrigatório."}), 400
    
    if not novaTarefa.get('createdAt'):
        return jsonify({"mensagem": "Erro ao criar tarefa. Data de criação é obrigatória."}), 400
    
    try:
        title = novaTarefa.get('title')
        description = novaTarefa.get('description')
        status = novaTarefa.get('status')
        createdAt = novaTarefa.get('createdAt')

        if not status:
            status = 'pendente'

        conn = bd.conectar()
        
        if conn is None:
            return jsonify({"mensagem": "Erro ao conectar ao banco de dados."}), 500
        
        cur = conn.cursor()

        cur.execute("INSERT INTO tarefas (title, description, status, createdAt) VALUES (%s, %s, %s, %s);", (title, description, status, createdAt))
        conn.commit()

        return jsonify({"mensagem": "Tarefa criada com sucesso."}), 201
    
    except Exception as e:
        conn.rollback()

        return jsonify({"mensagem": f"Erro ao criar tarefa: {e}"}), 500
    finally:
        bd.desconectar(cur, conn)
    
@app.route('/tasks/<int:id>', methods=['PUT'])
def atualizarTarefa(id):
    conn = None
    cur = None

    dadosAtualizados = request.get_json(silent=True)

    if not dadosAtualizados:
        return jsonify({"mensagem": "Erro ao atualizar tarefa. Dados inválidos."}), 400

    try:
        conn = bd.conectar()

        if conn is None:
            return jsonify({"mensagem": "Erro ao conectar ao banco de dados."}), 500
        
        cur = conn.cursor()

        if dadosAtualizados.get('id') is not None:
            return jsonify({"mensagem": "Erro ao atualizar tarefa. Não é permitido alterar o ID da tarefa."}), 400


        
        camposParaAtualizar = []
        valoresParaAtualizar = []

        for campo in ['title', 'description', 'status', 'createdAt']:
            if campo in dadosAtualizados:
                camposParaAtualizar.append(f"{campo} = %s")
                valoresParaAtualizar.append(dadosAtualizados[campo])
        
        if not camposParaAtualizar:
            return jsonify({"mensagem": "Nenhum campo válido encontrado para atualização."}), 400
        
        valoresParaAtualizar.append(id)

        sqlAtualizacao = f"UPDATE tarefas SET {', '.join(camposParaAtualizar)} WHERE id = %s;"
        cur.execute(sqlAtualizacao, tuple(valoresParaAtualizar))

        if cur.rowcount == 0:
            return jsonify({"erro": "Tarefa com o ID fornecido não encontrada."}), 404
        
        conn.commit()
        return jsonify({"mensagem": "Tarefa atualizada com sucesso."})
    
    except Exception as e:
        conn.rollback()
        return jsonify({"mensagem": f"Erro ao atualizar tarefa: {e}"}), 500
    finally:
        bd.desconectar(cur, conn)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def deletarTarefa(id):
    conn = None
    cur = None

    try:
        conn = bd.conectar()

        if conn is None:
            return jsonify({"mensagem": "Erro ao conectar ao banco de dados."}), 500
        
        cur = conn.cursor()

        cur.execute("DELETE FROM tarefas WHERE id = %s;", (id,))
        if cur.rowcount == 0:
            return jsonify({"erro": "Tarefa com o ID fornecido não encontrada."}), 404

        conn.commit()

        return jsonify({"mensagem": "Tarefa deletada com sucesso."})
    except Exception as e:
        conn.rollback()
        return jsonify({"mensagem": f"Erro ao deletar tarefa: {e}"}), 500
    finally:
        bd.desconectar(cur, conn)
    
if __name__ == '__main__':
    app.run(port=5000, host='localhost',debug=True)
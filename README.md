# API de para gerenciamento de tarefas (To-Do List)     

## Sobre o Projeto
Esta é uma API RESTful completa para gerenciamento de tarefas (CRUD - Criar, Ler, Atualizar, Deletar), desenvolvida em Python com o framework Flask. A aplicação se conecta a um banco de dados PostgreSQL e está implantada na nuvem utilizando a plataforma Render.

**URL da API online:** https://api-tasks-guiafonso.onrender.com/tasks

**URL para utilização do postman:** 

## **Funcionalidades**
* Listar todas as tarefas cadastradas.
* Obter uma tarefa específica pelo seu ID.
* Criar uma nova tarefa.
* Atualizar uma tarefa existente (título, descrição, status, etc.).
* Deletar uma tarefa pelo seu ID.

## Tecnologias Utilizadas
* Backend: Python 3.11
* Framework Web: Flask
* Servidor de Produção: Gunicorn
* Banco de Dados: PostgreSQL
* Driver do Banco de Dados: Psycopg2
* Plataforma de Deploy: Render

## **EndPoints da API**
#### A seguir estão os detalhes de como interagir com cada endpoint da API.

1. ### Listar todas as tarefas
    * Método: GET
    * URL: /tasks
    * Resposta de Sucesso (200 OK):
    ```
    [
    {
            "id": 1,
            "title": "Configurar o banco de dados no Render",
            "status": "concluida",
            "description": "Criar a instância PostgreSQL e a tabela 'tarefas'.",
            "createdAt": "2025-10-19",
            "completedAt": "2025-10-19"
    },
    {
            "id": 2,
            "title": "Fazer o deploy da API",
            "description": null,
            "status": "pendente",
            "createdAt": "2025-10-20",
            "completedAt": null
    }
    ]
    ```
    
2. ### Obter uma tarefa específica

    ##### Retorna os detalhes de uma única tarefa, identificada pelo seu id.
    * Método: GET
    * URL: /tasks/<id>
    * Exemplo de URL: /tasks/1
    * Resposta de Sucesso (200 OK):
    ```
    {
        "id": 1,
        "title": "Configurar o banco de dados no Render",
        "description": "Criar a instância PostgreSQL e a tabela 'tarefas'.",
        "status": "concluida",
        "createdAt": "2025-10-19",
        "completedAt": "2025-10-19"
    }
    ```
3. ### Criar uma nova tarefa
    #### Cadastra uma nova tarefa no banco de dados 
    * Método: POST
    * URL: /tasks
    * **Corpo da Requisição (JSON):**
    ```
        {
            "title": "Documentar a API no README",
            "description": "Criar um README completo com exemplos para cada endpoint."
        }

    ```
    **Obs.:** status (padrão: "pendente"), createdAt (padrão: data atual) e completedAt são opcionais.
    * Resposta de Sucesso (201 Created):
    ```
        {
            "mensagem": "Tarefa criada com sucesso."
        }

    ```

4. ### Atualizar uma tarefa
    #### Modifica uma ou mais informações de uma tarefa existente.
    * Método: PUT
    * URL: /tasks/<id>
    * Exemplo de URL: /tasks/2
    * **Corpo da Requisição (JSON):**
    ``` 
        {
            "status": "concluida"
        }

    ```
    * Resposta de Sucesso (200 ok):
        ```
        {
            "mensagem": "Tarefa atualizada com sucesso."
        }
        ```

5. ###  Deletar uma tarefa
    #### Remove uma tarefa do banco de dados.
    * Método: DELETE
    * URL: /tasks/<id>
    * Exemplo de URL: /tasks/1
    * Resposta de Sucesso (200 OK):
    ```
        {
            "mensagem": "Tarefa deletada com sucesso."
        }

    ```

## Como Executar Localmente (Desenvolvimento)
1. Clone o repositório:
    ```
    git clone [https://github.com/guiafonso237/API_TASKS.git](https://github.com/guiafonso237/API_TASKS.git)
    cd API_TASKS
    ```
2. Crie e ative um ambiente virtual:
    ```
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
4. Configure o banco de dados local:
    * Certifique-se de que o PostgreSQL está rodando
    * Ajuste as credenciais no arquivo conexao.py para corresponder ao seu ambiente local.
    * Garanta que a tabela esteja criada e que todas as permissões necessárias estejam liberadas 

5. Inicie a aplicação:
    ```
    python main.py
    ```
    #### A API estará disponível em http://localhost:5000.

### Autor
* Guilherme Afonso B. Damasceno
* GitHub: @guiafonso237


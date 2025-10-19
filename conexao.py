import psycopg2
import sys
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

def conectar():
    conn = None
    try:
        if DATABASE_URL is None:
            print("Erro: A variável de ambiente DATABASE_URL não foi definida.", file=sys.stderr)
            return None
            
        conn = psycopg2.connect(DATABASE_URL)
        return conn

    except psycopg2.OperationalError as e:
        print(f"Erro: Não foi possível conectar ao banco de dados.", file=sys.stderr)
        print(f"Detalhes: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado na conexão: {e}", file=sys.stderr)
        return None

def desconectar(cur, conn):
    if cur:
        cur.close()
    if conn:
        conn.close()


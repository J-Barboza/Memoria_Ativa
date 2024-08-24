import sqlite3

def connect():
    return sqlite3.connect('memoria_ativa.db')

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    # Outras tabelas serão criadas aqui com o progresso do projeto

    conn.commit()
    conn.close()

# # Verificação para garantir que o arquivo não seja executado diretamente
# if __name__ != "__main__":
#     raise RuntimeError("Este script não pode ser executado diretamente. Utilize o main.py.")

import sqlite3
from database import connect

class UserManager:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()

    def register(self):
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        try:
            self.cursor.execute('''
                INSERT INTO users (username, password) 
                VALUES (?, ?)
            ''', (username, password))
            self.conn.commit()
            print("Cadastro realizado com sucesso!")
        except sqlite3.IntegrityError:
            print("Usuário já existe! Tente outro nome.")

    def login(self):
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")

        self.cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password))
        
        user = self.cursor.fetchone()

        if user:
            print(f"Bem-vindo(a), {username}!")
            return True
        else:
            print("Usuário ou senha incorretos.")
            return False

# # Verificação para garantir que o arquivo não seja executado diretamente
# if __name__ != "__main__":
#     raise RuntimeError("Este script não pode ser executado diretamente. Utilize o main.py.")

from database import create_tables
from user import UserManager
from activities import ActivityManager

def main():
    # Criar tabelas ao iniciar o aplicativo
    create_tables()
    
    print("Bem-vindo ao Projeto Memória Ativa!")
    user_manager = UserManager()
    
    while True:
        print("\n1. Login\n2. Cadastro\n3. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            if user_manager.login():
                break
        elif choice == '2':
            user_manager.register()
        elif choice == '3':
            print("Até logo!")
            return
        else:
            print("Opção inválida. Tente novamente.")

    # Menu principal após login
    while True:
        print("\n1. Iniciar Atividade\n2. Configurações\n3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            activity_manager = ActivityManager()
            activity_manager.start_activity()
        elif choice == '2':
            # Chamar menu de configurações (a ser implementado)
            pass
        elif choice == '3':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

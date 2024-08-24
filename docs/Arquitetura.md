# Arquitetura da Versão em Python

## Módulos Principais

- **main.py:** Ponto de entrada do aplicativo, onde o fluxo principal de execução será controlado.

- **user.py:** Gerenciamento de usuários, incluindo cadastro, login e salvamento de progresso.
- **activities.py:** Implementação das atividades cognitivas (Sudoku, quebra-cabeças, etc.).
- **game_mode.py:** Definição dos modos de jogo (Treino, Desafios, etc.).
- **feedback.py:** Módulo responsável por calcular e apresentar feedback e progresso ao usuário.
- **settings.py:** Configurações do aplicativo, como dificuldade, personalizações, etc.
- **utils.py:** Funções utilitárias que podem ser usadas em diferentes partes do código.

## Fluxo Básico de Execução

1. **Início:** O usuário é apresentado com opções para cadastro ou login.

2. **Menu Principal:** Após o login, o usuário acessa o menu principal onde pode escolher entre Treino, Desafios ou acessar as configurações.
3. **Escolha de Atividade:** O usuário escolhe uma atividade (ex: Sudoku) e o nível de dificuldade.
4. **Execução da Atividade:** A atividade é apresentada, e o usuário interage com ela.
5. **Feedback:** Após completar a atividade, o usuário recebe feedback sobre seu desempenho.
6. **Progresso:** O progresso é salvo, e o usuário pode escolher outra atividade ou encerrar o jogo.

# Implementação Inicial

## Passos Iniciais

1. Criar os arquivos principais (`main.py`, `user.py`, etc.).

2. Estruturar o `main.py` para lidar com o fluxo básico de navegação (menu principal).
3. Implementar a base do sistema de usuários (`user.py`), permitindo o cadastro e login simples.
4. Desenvolver uma primeira atividade simples (ex: um Sudoku básico) em `activities.py`.

## Estrutura Inicial do Projeto

1. Criação de Arquivos e Módulos

```plaintext
memoria_ativa/
│
├── src/
│   ├── main.py
│   ├── user.py
│   ├── database.py
│   ├── activities.py
│   ├── game_mode.py
│   ├── feedback.py
│   ├── settings.py
│   └── utils.py
│
└── docs/
    ├── Projeto Memória Ativa
    ├── Funcionalidades.md
    └── ArquiteturaPython.md
```
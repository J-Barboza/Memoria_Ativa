import random

# activities.py

class ActivityManager:
    def __init__(self):
        pass

    def start_activity(self):
        print("\nSelecione a atividade:")
        print("1. Sudoku")
        # Outras atividades podem ser adicionadas aqui
        choice = input("Escolha uma atividade: ")

        if choice == '1':
            self.sudoku()
        else:
            print("Atividade inválida.")

    def sudoku(self):
        print("Iniciando Sudoku...")
        puzzle = self.generate_sudoku()
        self.display_sudoku(puzzle)
        while True:
            row = int(input("Digite a linha (1-9) ou 0 para sair: ")) - 1
            if row == -1:
                break
            col = int(input("Digite a coluna (1-9): ")) - 1
            num = int(input("Digite o número (1-9): "))
            if puzzle[row][col] == 0:
                puzzle[row][col] = num
                self.display_sudoku(puzzle)
            else:
                print("Posição já preenchida. Escolha outra.")

            if self.check_solution(puzzle):
                print("Parabéns! Você completou o Sudoku.")
                break

    def generate_sudoku(self):
        base  = 3
        side  = base * base

        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        def shuffle(s): return random.sample(s,len(s))
        rBase = range(base)
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = squares * 3//4
        for p in random.sample(range(squares), empties):
            board[p//side][p%side] = 0

        return board

    def display_sudoku(self, board):
        base = 3
        side = base * base
        line = "+" + "+".join(["-" * base] * base) + "+"

        for r in range(side):
            if r % base == 0:
                print(line)
            row = "|".join(" ".join(str(board[r][c]) if board[r][c] != 0 else "." for c in range(g*base, (g+1)*base)) for g in range(base))
            print(f"|{row}|")
        print(line)

    def check_solution(self, board):
        base = 3
        side = base * base

        def valid_block(block):
            return sorted(block) == list(range(1, side+1))

        def get_block(board, r, c):
            return [board[r + i//base][c + i%base] for i in range(side)]

        for i in range(side):
            if not valid_block(board[i]) or not valid_block([board[r][i] for r in range(side)]):
                return False

        for r in range(0, side, base):
            for c in range(0, side, base):
                if not valid_block(get_block(board, r, c)):
                    return False

        return True

# # Verificação para garantir que o arquivo não seja executado diretamente
# if __name__ != "__main__":
#     raise RuntimeError("Este script não pode ser executado diretamente. Utilize o main.py.")

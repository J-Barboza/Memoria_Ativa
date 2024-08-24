# sudoku_gui.py

import tkinter as tk
from tkinter import messagebox
from activities import ActivityManager

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku - Memória Ativa")
        self.board = ActivityManager().generate_sudoku()
        self.cells = {}

        self.create_grid()

    def create_grid(self):
        for r in range(9):
            for c in range(9):
                cell_value = self.board[r][c]
                cell_text = tk.StringVar()
                
                cell_entry = tk.Entry(self.master, width=2, font=('Arial', 18), textvariable=cell_text, justify='center')

                if cell_value != 0:
                    cell_text.set(cell_value)
                    cell_entry.config(state='disabled')
                else:
                    cell_text.set("")

                # Aplicar padding padrão
                padx = 1
                pady = 1

                # Verificar se é a borda de um quadrante de 3x3 e ajustar as linhas
                if c % 3 == 0 and c != 0:
                    padx = (5, 1)
                if r % 3 == 0 and r != 0:
                    pady = (5, 1)

                cell_entry.grid(row=r, column=c, padx=padx, pady=pady)
                self.cells[(r, c)] = cell_text

        check_button = tk.Button(self.master, text="Verificar Solução", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=9, pady=10)

        self.add_grid_lines()

    def add_grid_lines(self):
        # Adicionar as linhas pretas grossas para os quadrantes
        for i in range(10):
            if i % 3 == 0:
                line = tk.Frame(self.master, height=2, bg='black')
                line.grid(row=i, column=0, columnspan=9, sticky='ew')
                line = tk.Frame(self.master, width=2, bg='black')
                line.grid(row=0, column=i, rowspan=9, sticky='ns')

    def check_solution(self):
        board = []
        for r in range(9):
            row = []
            for c in range(9):
                try:
                    value = int(self.cells[(r, c)].get())
                except ValueError:
                    value = 0
                row.append(value)
            board.append(row)
        
        if ActivityManager().check_solution(board):
            messagebox.showinfo("Sudoku", "Parabéns! Você completou o Sudoku.")
        else:
            messagebox.showwarning("Sudoku", "A solução ainda não está correta. Continue tentando!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()

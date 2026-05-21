import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text=' ', font=('Arial', 20), width=5, height=2,
                                                command=lambda i=i, j=j: self.play_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def play_move(self, row, col):
        if self.board[row][col] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player

            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        player = self.board[row][col]

        # Check row
        if all(self.board[row][c] == player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == player for r in range(3)):
            return True
        # Check diagonal
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
                self.board[i][j] = ' '
        self.current_player = 'X'


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()

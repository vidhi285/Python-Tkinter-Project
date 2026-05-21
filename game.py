import tkinter as tk
from tkinter import messagebox
import random

class GameSelectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Games")
        self.master.geometry("450x300")
        self.master.config(bg='skyblue')
        self.master.iconbitmap('game.ico')
        self.label_instruction = tk.Label(self.master, text='Click the button below to select a game',fg='purple', bg='pink', font=('cambria', 20))
        self.label_instruction.pack(pady=10)

        # Create buttons
        self.btn_tic_tac_toe = tk.Button(self.master, text="Tic Tac Toe", font=('Arial',15),fg='purple', bg='pink', command=self.open_tic_tac_toe)
        self.btn_tic_tac_toe.pack(pady=10)

        self.btn_memory_puzzle = tk.Button(self.master, text="Memory Puzzle",font=('Arial',15),fg='purple', bg='pink', command=self.open_memory_puzzle)
        self.btn_memory_puzzle.pack(pady=10)     

        self.btn_pong_game = tk.Button(self.master, text="Pong Game",font=('Arial',15),fg='purple', bg='pink', command=self.open_pong_game)
        self.btn_pong_game.pack(pady=10)

        self.btn_exit = tk.Button(self.master, text="Exit",font=('Arial',15),fg='purple', bg='pink', command=self.exit_program)
        self.btn_exit.pack(pady=10)

    def open_tic_tac_toe(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = TicTacToe(self.new_window)

    def open_memory_puzzle(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = MemoryPuzzle(self.new_window)

    def open_pong_game(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = PongGame(self.new_window)

    def exit_program(self):
        self.master.destroy()

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

class MemoryPuzzle:
    def __init__(self, master, rows=4, columns=4):
        self.master = master
        self.master.title("Memory Puzzle")
        self.rows = rows
        self.columns = columns
        self.total_pairs = (self.rows * self.columns) // 2
        self.cards = [f"{i}" for i in range(1, self.total_pairs + 1)] * 2
        random.shuffle(self.cards)
        self.buttons = []
        self.selected_card = None  # Initialize selected_card attribute
        self.create_board()

    def create_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                button = tk.Button(self.master, text=" ", font=('Helvetica', 12), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, row, col):
        button = self.buttons[row][col]
        card_value = self.cards[row * self.columns + col]

        button.config(text=card_value)
        button.config(state="disabled")

        if self.selected_card is not None:
            if self.selected_card[0] == card_value:
                messagebox.showinfo("Match!", "You found a match!")
                self.selected_card = None
            else:
                self.master.after(500, self.hide_unmatched, row, col)
        else:
            self.selected_card = (card_value, row, col)

    def hide_unmatched(self, row, col):
        self.buttons[self.selected_card[1]][self.selected_card[2]].config(text=" ")
        self.buttons[row][col].config(text=" ")
        self.buttons[self.selected_card[1]][self.selected_card[2]].config(state="normal")
        self.buttons[row][col].config(state="normal")
        self.selected_card = None

class PongGame:
    def __init__(self, master, width=600, height=400, paddle_width=10, paddle_height=80, ball_size=15):
        self.master = master
        self.master.title("Pong Game")
        self.width = width
        self.height = height
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.ball_size = ball_size
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        self.paddle_speed = 10
        self.ball_speed = 5
        self.paddle1 = self.canvas.create_rectangle(50, (self.height - self.paddle_height) / 2,
                                                    50 + self.paddle_width, (self.height + self.paddle_height) / 2,
                                                    fill='white')
        self.paddle2 = self.canvas.create_rectangle(self.width - 50 - self.paddle_width,
                                                    (self.height - self.paddle_height) / 2,
                                                    self.width - 50, (self.height + self.paddle_height) / 2,
                                                    fill='white')
        self.ball = self.canvas.create_oval((self.width - self.ball_size) / 2, (self.height - self.ball_size) / 2,
                                            (self.width + self.ball_size) / 2, (self.height + self.ball_size) / 2,
                                            fill='white')
        self.ball_dx = random.choice([-1, 1]) * self.ball_speed
        self.ball_dy = random.choice([-1, 1]) * self.ball_speed
        self.canvas.bind_all('<KeyPress-Up>', self.move_paddle1_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_paddle1_down)
        self.canvas.bind_all('<KeyPress-w>', self.move_paddle2_up)
        self.canvas.bind_all('<KeyPress-s>', self.move_paddle2_down)
        self.update()

    def move_paddle1_up(self, event):
        self.canvas.move(self.paddle1, 0, -self.paddle_speed)

    def move_paddle1_down(self, event):
        self.canvas.move(self.paddle1, 0, self.paddle_speed)

    def move_paddle2_up(self, event):
        self.canvas.move(self.paddle2, 0, -self.paddle_speed)

    def move_paddle2_down(self, event):
        self.canvas.move(self.paddle2, 0, self.paddle_speed)

    def update(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        if (ball_coords[1] <= 0 or ball_coords[3] >= self.height):
            self.ball_dy *= -1

        if ball_coords[0] <= 0:
            messagebox.showerror("Game Over", "You lose!")
            self.master.destroy()

        if (ball_coords[2] >= self.width):
            self.ball_dx *= -1
            paddle2_coords = self.canvas.coords(self.paddle2)
            if (ball_coords[2] >= paddle2_coords[0] and ball_coords[3] >= paddle2_coords[1] and
                ball_coords[0] <= paddle2_coords[2] and ball_coords[1] <= paddle2_coords[3]):
                self.ball_dx *= -1

        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)

        if (ball_coords[2] >= paddle2_coords[0] and ball_coords[3] >= paddle2_coords[1] and
            ball_coords[0] <= paddle2_coords[2] and ball_coords[1] <= paddle2_coords[3]):
            self.ball_dx *= -1

        if (ball_coords[0] <= paddle1_coords[2] and ball_coords[3] >= paddle1_coords[1] and
            ball_coords[2] >= paddle1_coords[0] and ball_coords[1] <= paddle1_coords[3]):
            self.ball_dx *= -1

        self.master.after(20, self.update)

def main():
    root = tk.Tk()
    app = GameSelectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

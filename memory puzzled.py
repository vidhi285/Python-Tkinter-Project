import tkinter as tk
from tkinter import messagebox
import random

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

def main():
    root = tk.Tk()
    game = MemoryPuzzle(root)
    root.mainloop()

if __name__ == "__main__":
    main()

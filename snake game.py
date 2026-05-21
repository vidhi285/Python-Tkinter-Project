import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master, width=400, height=400, cell_size=20):
        self.master = master
        self.master.title("Snake Game")
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        self.snake = [(0, 0)]
        self.food = self.generate_food()
        self.direction = 'Right'
        self.score = 0
        self.draw_game()

        self.master.bind('<Key>', self.change_direction)
        self.update()

    def draw_game(self):
        self.canvas.delete("all")

        # Draw snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                          (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                          fill='green')

        # Draw food
        x, y = self.food
        self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                     (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                     fill='red')

        # Display score
        self.canvas.create_text(self.width / 2, 10, text=f"Score: {self.score}", fill='white')

    def generate_food(self):
        while True:
            food = (random.randint(0, (self.width // self.cell_size) - 1),
                    random.randint(0, (self.height // self.cell_size) - 1))
            if food not in self.snake:
                return food

    def change_direction(self, event):
        if event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'
        elif event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'

    def update(self):
        head = self.snake[0]
        if self.direction == 'Left':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'Right':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'Up':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'Down':
            new_head = (head[0], head[1] + 1)

        if (new_head[0] < 0 or new_head[0] >= self.width // self.cell_size or
            new_head[1] < 0 or new_head[1] >= self.height // self.cell_size or
            new_head in self.snake[1:]):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.draw_game()
        self.master.after(100, self.update)

    def game_over(self):
        self.canvas.create_text(self.width / 2, self.height / 2, text="Game Over", fill='white')

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

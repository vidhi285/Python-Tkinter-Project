import tkinter as tk
from tkinter import messagebox
import random

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
    game = PongGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

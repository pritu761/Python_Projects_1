FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.write(f"LEVEL {self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"LEVEL {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

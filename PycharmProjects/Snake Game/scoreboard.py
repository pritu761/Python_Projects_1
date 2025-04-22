from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.scoreboard()

    def scoreboard(self):
        self.clear()

        self.write(f"Score {self.score}  High Score {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}\n")
        self.score = 0
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

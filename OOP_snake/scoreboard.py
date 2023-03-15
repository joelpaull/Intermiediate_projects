from turtle import Turtle
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = 0
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER, Score: {self.score}", align="center", font=FONT)
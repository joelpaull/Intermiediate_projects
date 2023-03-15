from turtle import Turtle
FONT = ("courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.write(arg=f"{self.score}", align="center", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", align="center", font=FONT)
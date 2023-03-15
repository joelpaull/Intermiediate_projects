from turtle import Turtle
POSITION_L = (-350, 0)
POSITION_R = (350, 0)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.new_y = ''
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def move_down(self):
        self.new_y = self.ycor() - 20
        self.sety(self.new_y)

    def move_up(self):
        self.new_y = self.ycor() + 20
        self.sety(self.new_y)

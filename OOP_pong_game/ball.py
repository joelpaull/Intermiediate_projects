from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("blue")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_restart(self):
        self.goto(0, 0)
        self.wall_bounce()
        self.paddle_bounce()
        self.move_speed = 0.09
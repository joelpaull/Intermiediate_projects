from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(random.randint(-255, 255), random.randint(-255, 255))

    def refresh(self):
        self.goto(random.randint(-255, 255), random.randint(-255, 255))
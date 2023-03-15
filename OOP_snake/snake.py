from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in START_POSITION:
            self.add_body_part(pos)

    def add_body_part(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        snake.speed("fastest")
        self.snake_body.append(snake)

    def grow_on_eating(self):
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def face_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def face_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def face_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def face_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hit_wall(self):
        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            return True
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

play_again = True
while play_again:
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(key="Left", fun=snake.face_left)
    screen.onkey(key="Right", fun=snake.face_right)
    screen.onkey(key="Down", fun=snake.face_down)
    screen.onkey(key="Up", fun=snake.face_up)

    game_on = True
    speed = 0.1
    while game_on:
        if speed > 0.03:
            speed -= 0.00005
        if snake.hit_wall():
            game_on = False

        for n in snake.snake_body[1:]:
            if snake.head.distance(n) < 10:
                game_on = False

        screen.update()
        time.sleep(speed)
        snake.move()
    #     Detect Food collision
        if int(snake.head.distance(food)) < 20:
            food.refresh()
            scoreboard.add_score()
            snake.grow_on_eating()
    scoreboard.game_over()
    # Ask user to play again:
    time.sleep(0.75)
    replay = screen.textinput(title="Snake", prompt="Do you want to play again? 'Yes' or 'No'")
    if replay.lower() == "no":
        play_again = False

    for n in snake.snake_body:
        n.reset()
    food.reset()
    scoreboard.reset()

screen.exitonclick()
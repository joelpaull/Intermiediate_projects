from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_on = True

# Create Paddles
PADDLE_POSITION_L = (-350, 0)
PADDLE_POSITION_R = (350, 0)
paddle_l = Paddle(PADDLE_POSITION_L)
paddle_r = Paddle(PADDLE_POSITION_R)
# Create ball
ball = Ball()
# Create scoreboard
scoreboard = Scoreboard
SCORE_POSITION_L = (-50, 220)
SCORE_POSITION_R = (50, 220)
scoreboard_l = Scoreboard(SCORE_POSITION_L)
scoreboard_r = Scoreboard(SCORE_POSITION_R)
while game_on:
    screen.listen()
    ball.move()
    # Player 1 movement
    screen.onkey(key="w", fun=paddle_l.move_up)
    screen.onkey(key="s", fun=paddle_l.move_down)
    # Player 2 movement
    screen.onkey(key="Up", fun=paddle_r.move_up)
    screen.onkey(key="Down", fun=paddle_r.move_down)
    screen.update()
    # ball hits top/bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_bounce()
    # ball hits left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()
    time.sleep(ball.move_speed)
    if ball.xcor() > 380:
        scoreboard_l.add_score()
        ball.ball_restart()
    if ball.xcor() < -380:
        scoreboard_r.add_score()
        ball.ball_restart()

screen.exitonclick()
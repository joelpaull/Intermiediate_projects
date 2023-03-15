import turtle
import pandas as pd
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed_correctly = []

game_on = True
correct_guess = 0
while game_on:
    with open("50_states.csv") as states_data:
        data = pd.read_csv(states_data)
        states_list = data.state.to_list()
        user_answer = screen.textinput(title=f"Guessed {correct_guess}/50 States Correct", prompt="What is your guess?").capitalize()

        if user_answer == "Exit":
            states_to_learn = [state for state in states_list if state not in states_guessed_correctly]
            learning_data = pd.DataFrame(states_to_learn)
            learning_data.to_csv("Learning_data.csv")
            break

        if user_answer in states_list:
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            # Get state 'row'
            state_data = data[data.state == user_answer]
            # column headings saved as attributes
            turtle.goto(int(state_data.x), int(state_data.y))
            turtle.write(arg=user_answer, font=("arial", 12, "bold"))
            correct_guess += 1
            states_guessed_correctly.append(user_answer)
            if correct_guess == 50:
                game_on = False
                turtle.goto(0,0)
                turtle.write(arg="You got all the states!", font=("arial", 25, "bold"))
screen.exitonclick()
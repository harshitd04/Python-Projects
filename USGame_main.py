import turtle
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

screen = turtle.Screen()
screen.title("US States Guessing Game.")
image = (r"C:\Users\RAKESH KUMAR DABAS\PycharmProjects\PythonProject\day-25\.venv\day-25-us-states-game-start"
         r"\blank_states_img.gif")
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv(r"C:\Users\RAKESH KUMAR DABAS\PycharmProjects\PythonProject\day-25\.venv"
               r"\day-25-us-states-game-start\50_states.csv")

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
states_list = states_data["state"].to_list()
game_on = True
correct_guesses = []

score = 0
while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{score}/50", "What's another state's name?").title()
    if answer_state in states_list:

        if answer_state in correct_guesses:
            print("Already guessed.")

        else:
            state_data = states_data[states_data["state"] == answer_state]
            my_turtle.goto(state_data.x.item(),state_data.y.item())
            my_turtle.write(state_data.state.item())
            correct_guesses.append(answer_state)
            score += 1

    elif answer_state == "Exit":
        break

if len(correct_guesses) == 50:
    my_turtle.goto(-60,0)
    my_turtle.write("You won.",font = ("Arial",20,"bold"))

to_learn_states = []

for i in states_list:
    if i not in correct_guesses:
        to_learn_states.append(i)

new_data = pandas.DataFrame(to_learn_states)
new_data.to_csv("states_to_learn.csv")
# screen.exitonclick()
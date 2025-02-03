from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(f"Enter your choice","Choose who will win from rainblow colors: ")
my_colors = ["red","orange","yellow","green","blue","purple"]
y_cord = -105

list_of_turtles = []
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(my_colors[i])
    new_turtle.goto(x=- 230, y=y_cord)
    y_cord += 40
    list_of_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won. The winner is: {winner}")
            else:
                print(f"You lost. The winner is: {winner}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()







from turtle import Turtle, Screen
import random

def change_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

screen = Screen()
timmy = Turtle()
screen.colormode(255)
# turtle.colormode(255)

timmy.shape("turtle")
timmy.color("Blue")
timmy.speed(0)
# timmy.pensize(2)

timmy.penup()
# timmy.goto(0, screen.window_height() // 2 - 20)
timmy.pendown()

#--------------------
# angles = [0,90,180,270]
# for i in range(100):
#     timmy.forward(30)
#     timmy.right(random.choice(angles))
#     timmy.pencolor(change_colour())

degree = 360
while degree > 0:
    timmy.circle(100)
    timmy.right(5)
    degree -= 5
    timmy.pencolor(change_colour())






screen = Screen()
screen.exitonclick()
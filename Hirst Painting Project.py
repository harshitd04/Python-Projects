# import colorgram
# colors = colorgram.extract("hirst painting.jpg",10)
# # print(colors)
#
# rgb_colours = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colours.append((r,g,b))
# print(rgb_colours)

from turtle import Turtle, Screen
import random
color_list = [(221, 57, 96), (49, 90, 176), (252, 241, 247), (213, 235, 250), (236, 135, 164), (246, 145, 185)]

timmy = Turtle()
screen = Screen()

timmy.hideturtle()
timmy.pensize(10)
screen.colormode(255)
y_cord = 0

print(timmy.xcor(),timmy.ycor())
for i in range(9):
    for j in range(9):
        timmy.pencolor(random.choice(color_list))
        timmy.pendown()
        timmy.forward(1)
        timmy.penup()
        timmy.forward(29)
    y_cord += 20
    timmy.goto(0, y_cord)



screen.exitonclick()




import turtle

import random
from levels import Levels, Startline, Endline, Game_Over
from turtle import Screen
from my_turtle import MyTurtle
from my_cars import Cars
import time

screen = Screen()
screen.setup(height = 600,width=600)
screen.tracer(0)
screen.colormode(255)
screen.title("Turtle Race")

my_turtle = MyTurtle()
levels = Levels()
startline = Startline()
endline = Endline()

cars_list = []
for i in range(15):
    new_car = Cars()
    new_car.goto(random.randint(-50,300),random.randint(-225,200))
    cars_list.append(new_car)

screen.listen()
screen.onkey(my_turtle.move,"w")
screen.onkey(my_turtle.move,"Up")

sleep_time = 0.09
game_on = True

while game_on:
    time.sleep(sleep_time)
    screen.update()

    if random.randint(1,3) == 1:
        new_car = Cars()
        cars_list.append(new_car)

    for car in cars_list:
        car.move_car()
        if car.xcor() < -325:
            cars_list.remove(car)
        elif abs(car.xcor() - my_turtle.xcor()) < 20 and abs(car.ycor() - my_turtle.ycor()) < 20:
                print("Whoosh!! Collision detected!")
                gameover = Game_Over()
                game_on = False

    if my_turtle.ycor() > 224:
        sleep_time *= 0.9
        my_turtle.goto(0, -265)
        levels.increase_level()


screen.exitonclick()
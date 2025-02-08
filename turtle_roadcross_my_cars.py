from turtle import Turtle
import random

CORDINATES_FOR_CARS_Y = [-225,-200,-175,-150,-125,-100,-75,-50,-25,0,25,50,75,100,125,150,175,200]
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.left(180)
        self.turtlesize(stretch_len=2)
        self.random_color()
        self.goto(310, random.choice(CORDINATES_FOR_CARS_Y))

    def move_car(self):
        self.forward(15)

    def random_color(self):
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color(r,g,b)







from turtle import Turtle
STARTING_POSTIION = (0,-265)

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSTIION)

    def move(self):
        self.forward(20)
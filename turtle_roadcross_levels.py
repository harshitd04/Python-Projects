from turtle import Turtle
import time

class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-275,235)
        self.write(f"Level : {self.level}", font = ("Arial", 16, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", font=("Arial", 16, "normal"))

class Startline(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(0, -235)
        self.turtlesize(stretch_wid=0.1,stretch_len=40)

class Endline(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(0, 220)
        self.turtlesize(stretch_wid=0.1,stretch_len=40)

class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)


    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(y=new_y,x=self.xcor())

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(y=new_y,x=self.xcor())




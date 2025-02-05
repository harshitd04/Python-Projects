from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))

    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score+=1
        self.show_score()




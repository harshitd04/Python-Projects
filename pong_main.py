from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height= 600,width=800)
screen.title("Pong")

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 283 or  ball.ycor() < -283:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or  ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 385:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -385:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
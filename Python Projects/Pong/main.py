from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

### detect collision with wall ###
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

### detect collision w/ paddle ###
    if ball.distance(r_paddle) < 50 and ball.xcor() < -330 or ball.distance(l_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

### detect l_paddle miss ###
    if ball.xcor() > 380:
        ball.rest_position()
        scoreboard.r_point()

### detect r_paddle miss ###
    if ball.xcor() < -380:
        ball.rest_position()
        scoreboard.l_point()

screen.exitonclick()

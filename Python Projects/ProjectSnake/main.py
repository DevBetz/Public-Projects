from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Project Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Score()


### Directions ###
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

### while loop game is on ###
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ### Detect collision with food ###
    if snake.head.distance(food) <20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ### Detect collision with wall ###
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.clear
        scoreboard.reset()
        snake.reset()

    ### Detect collision with tail ###
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.clear()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

# Highest Score is 125, see if you can beat it! #

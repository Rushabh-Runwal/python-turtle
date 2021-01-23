from turtle import Screen
import time
from Food import Food
from Snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.title('Snake Game')
screen.setup(600,600)
screen.bgcolor('#000')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

score = 0
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     collision with food
    if snake.t[0].distance(food) < 15:
        scoreboard.increment()
        snake.extend()
        food.refresh()

#     collision with wall;8
    x = snake.t[0].xcor()
    y = snake.t[0].ycor()

    if x > 300 or x < -300 or y > 300 or y < -300:
        scoreboard.refresh()
        snake.refresh()
        # scoreboard.game_over()
        # game_on = False

#     detect collision with body
# if head collide with  any part of tail
    for i in snake.t[1:]:
        if snake.t[0].distance(i) < 10:
            scoreboard.refresh()
            snake.refresh()
            # scoreboard.game_over()
            # game_on = False

screen.exitonclick()
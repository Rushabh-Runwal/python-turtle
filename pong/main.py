from turtle import  Screen,Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height= 600,width= 800)
screen.bgcolor("#000")
screen.title("PONG")
screen.tracer(0)

p1 = Paddle((350,0))
p2 = Paddle((-350,0))
screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, key="Down")

screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, 's')

ball = Ball()
scoreboard = Scoreboard()

while True:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.xcor() >= 330 and ball.distance(p1) <= 40 or ball.xcor() <= -330 and ball.distance(p2) <= 40:
        ball.bounce_x()

    if ball.xcor() >= 420:
        scoreboard.increment_p1()
        ball.refresh()

    if ball.xcor() <= -420:
        scoreboard.increment_p2()
        ball.refresh()
    ball.move()
screen.exitonclick()
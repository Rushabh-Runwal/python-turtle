import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, 'space')
scoreboard = Scoreboard()
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_all()
    if player.ycor() >= 300:
        scoreboard.level_up()
        cars.level_up()
        player.refresh()
    for i in cars.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

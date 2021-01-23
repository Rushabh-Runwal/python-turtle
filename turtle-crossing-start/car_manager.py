import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_d = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,4) == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(280, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_all(self):
        for i in self.all_cars:
            i.fd(self.move_d)

    def level_up(self):
        self.move_d += MOVE_INCREMENT



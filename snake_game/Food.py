from turtle import Turtle
import random


def r():
    return random.randint(-280, 280), random.randint(-280, 280)


class Food(Turtle):

    def __init__(self):
        super().__init__('circle')
        # self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.goto(r())

    def refresh(self):
        self.goto(r())
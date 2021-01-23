from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.t = []
        self.create_snake()

    def create_snake(self):
        for p in pos:
            self.add_t(p)

    def add_t(self,p):
        n_t = Turtle('square')
        n_t.color('#fff')
        n_t.penup()
        n_t.goto(p)
        self.t.append(n_t)

    def extend(self):
        self.add_t(self.t[-1].position())

    def move(self):
        for i in range(len(self.t) - 1, 0, -1):
            self.t[i].goto(self.t[i - 1].xcor(), self.t[i - 1].ycor())
        self.t[0].fd(20)

    def up(self):
        if self.t[0].heading() != 270:
            self.t[0].setheading(90)

    def down(self):
        if self.t[0].heading() != 90:
            self.t[0].setheading(270)

    def right(self):
        if self.t[0].heading() != 180:
            self.t[0].setheading(0)

    def left(self):
        if self.t[0].heading() != 0:
            self.t[0].setheading(180)

    def refresh(self):
        for i in self.t:
            i.goto(1000, 1000)
        self.t.clear()
        self.create_snake()
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__('circle')
        self.color('#fff')
        self.penup()
        self.speed('slow')
        self.x, self.y = 10, 10
        self.move_speed = 0.1

    def move(self):
        self.bounce_y()
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

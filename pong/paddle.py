from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__('square')
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color('#FFF')
        self.penup()
        self.goto(pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 40)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 40)

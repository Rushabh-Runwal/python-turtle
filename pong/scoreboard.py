from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('#fff')
        self.draw_middle_line()
        self.penup()
        self.p1 = 0
        self.p2 = 0
        self.display()

    def display(self):
        self.clear()
        self.draw_middle_line()
        self.write(f"{self.p1}   {self.p2}", move=False, align='center', font=('Courier', 50, 'normal'))

    def increment_p1(self):
        self.p1 += 1
        self.display()

    def increment_p2(self):
        self.p2 += 1
        self.display()

    def draw_middle_line(self):
        self.penup()
        self.speed('fastest')
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        for _ in range(15):
            self.fd(20)
            self.penup()
            self.fd(20)
            self.pendown()
        self.goto(0,220)


from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.level = 1
        self.display()

    def display(self):
        self.write(f"Level {self.level}", move= False, align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", move= False, align='center', font=FONT)

from turtle import *
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)


def shapes():
    for i in range(3, 11):
        tim.pencolor(random.randint(1, 255), (random.randint(1, 255)), (random.randint(1, 255)))
        for _ in range(i):
            tim.forward(100)
            tim.right(360 / i)


def random_walk():
    tim.speed(8)
    tim.pensize(10)
    for _ in range(100):
        tim.pencolor(random.randint(1, 255), (random.randint(1, 255)), (random.randint(1, 255)))
        tim.forward(30)
        tim.setheading(random.choice([0, 90, 180, 270]))


def spiral():
    tim.speed("fastest")
    for i in range(1,360,5):
        tim.setheading(i)
        tim.pencolor(random.randint(1, 255), (random.randint(1, 255)), (random.randint(1, 255)))
        tim.circle(100)


def hist_painting():
    tim.speed(10)
    for i in range(10):
        tim.penup()
        tim.setpos(screen.window_width() // 2 * -1 + 50 , screen.window_height() // 2 * -1 + 50 + (i*50))
        tim.pendown()
        for _ in range(10):
            tim.pencolor(random.randint(1, 255), (random.randint(1, 255)), (random.randint(1, 255)))
            tim.dot(20)
            tim.penup()
            tim.forward(50)
            tim.pendown()


def etchToSketch():
    def move_fd():
        tim.fd(10)

    def move_lt():
        tim.lt(10)

    def move_rt():
        tim.rt(10)

    def move_bk():
        tim.bk(10)

    def clear():
        tim.home()
        tim.clear()

    screen.listen()
    screen.onkey(move_fd, "w")
    screen.onkey(move_lt, "a")
    screen.onkey(move_rt, "d")
    screen.onkey(move_bk, "s")
    screen.onkey(clear, "c")


def turtle_race():
    tim.hideturtle()
    screen.setup(height=400,width=500)
    user_bet = screen.textinput(title="Make Your Bet !", prompt= "which color turtle will win? enter a color: ")
    colors = ['red','green','blue','orange','purple','yellow']
    turtles_lst = []
    y = 125
    c = 0
    for i in colors:
        t = Turtle(shape='turtle')
        t.penup()
        t.color(i)
        t.goto(x=-230,y = y - (c*50))
        c += 1
        turtles_lst.append(t)


turtle_race()









screen.exitonclick()

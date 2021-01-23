from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def rest():
    global rep
    rep = 0
    window.after_cancel(timer)
    ticks.config(text="")
    canvas.itemconfig(time,text="00:00")
    title.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    if rep % 2 != 0:
        count_down(WORK_MIN*60)
        title.config(text="Work",fg=GREEN)
        window.attributes("-topmost", 0)
    elif rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Long Break",fg=RED)
        window.attributes("-topmost", 1)
    elif rep % 2 == 0:
        window.attributes("-topmost", 1)
        count_down(SHORT_BREAK_MIN*60)
        title.config(text="Short Break", fg=PINK)
        window.attributes("-topmost", 1)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    text_hr = count//60
    if text_hr < 10:
        text_hr = f"0{text_hr}"
    text_min = count % 60
    if text_min < 10:
        text_min = f"0{text_min}"
    canvas.itemconfig(time, text=f"{text_hr}:{text_min}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks="".join(["✔"]*(rep//2))
        ticks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pormodoro")
window.config(padx=100, pady=50, bg = YELLOW)

canvas = Canvas(width=200,height=300,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,150, image= tomato)

time = canvas.create_text(100,170, text="00:00", fill="white",font= (FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

title = Label(text="Timer",fg= GREEN,bg=YELLOW, font=(FONT_NAME,30,"bold"))
title.grid(row=0,column=2)

st_btn = Button(text="start", highlightthickness=0,command=start_timer)
st_btn.grid(row=3, column=1)

reset_btn = Button(text="reset", highlightthickness=0,command=rest)
reset_btn.grid(row=3, column=3)

ticks = Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
ticks.grid(row=4, column=2)

window.mainloop()
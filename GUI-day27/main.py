from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=300 ,height=200)
window.config(padx=20,pady=30)

def get_ans():
    km = int(Km_input.get())
    m_input.config(text=f"{km/1.60934}")

Km = Label(text="Enter KM reading")
Km.grid(column=0, row=0)

Km_input = Entry(width=50)
Km_input.grid(column=0,row=1)

Miles = Label(text="in Miles: ")
Miles.grid(column= 1,  row=0)

m_input = Entry(text = "0")
m_input.grid(column= 1,  row=1)

button = Button(text="Calculate",command=get_ans)
button.grid(column=2,row=1)



window.mainloop()


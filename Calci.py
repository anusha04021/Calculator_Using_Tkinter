# Step1: importing
from tkinter import *
from tkinter import messagebox

# Step2: gui interactions
window = Tk()
window.geometry('500x500')

# Step3: Adding inputs

# Entry box
entry_box = Entry(window, width=56, borderwidth=5)
entry_box.place(x=0, y=0)


# Buttons
def click(num):
    result = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(result) + str(num))


btn = Button(window, text='1', width=12, command=lambda: click(1))
btn.place(x=10, y=60)

btn = Button(window, text='2', width=12, command=lambda: click(2))
btn.place(x=80, y=60)

btn = Button(window, text='3', width=12, command=lambda: click(3))
btn.place(x=170, y=60)

btn = Button(window, text='4', width=12, command=lambda: click(4))
btn.place(x=10, y=120)

btn = Button(window, text='5', width=12, command=lambda: click(5))
btn.place(x=80, y=120)

btn = Button(window, text='6', width=12, command=lambda: click(6))
btn.place(x=170, y=120)

btn = Button(window, text='7', width=12, command=lambda: click(7))
btn.place(x=10, y=180)

btn = Button(window, text='8', width=12, command=lambda: click(8))
btn.place(x=80, y=180)

btn = Button(window, text='9', width=12, command=lambda: click(9))
btn.place(x=170, y=180)

btn = Button(window, text='0', width=12, command=lambda: click(0))
btn.place(x=10, y=240)


def add():
    num1 = entry_box.get()
    global math
    math = 'Addition'
    global i
    i = int(num1)
    entry_box.delete(0, END)


btn = Button(window, text='+', width=12, command=add)
btn.place(x=80, y=240)


def subtract():
    num1 = entry_box.get()
    global math
    math = 'Subtraction'
    global i
    i = int(num1)
    entry_box.delete(0, END)


btn = Button(window, text='-', width=12, command=subtract)
btn.place(x=170, y=240)


def multiply():
    num1 = entry_box.get()
    global math
    math = 'Multiplication'
    global i
    i = int(num1)
    entry_box.delete(0, END)


btn = Button(window, text='*', width=12, command=multiply)
btn.place(x=10, y=300)


def divide():
    num1 = entry_box.get()
    global math
    math = 'Division'
    global i
    i = int(num1)
    entry_box.delete(0, END)


btn = Button(window, text='/', width=12, command=divide)
btn.place(x=80, y=300)


def equals():
    num_2 = entry_box.get()
    entry_box.delete(0, END)
    try:
        if math == "Addition":
            entry_box.insert(0, i + int(num_2))
        elif math == "Subtraction":
            entry_box.insert(0, i - int(num_2))
        elif math == "Multiplication":
            entry_box.insert(0, i * int(num_2))
        elif math == "Division":
            entry_box.insert(0, i / int(num_2))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


btn = Button(window, text='=', width=12, command=equals)
btn.place(x=170, y=300)


def clear():
    entry_box.delete(0, END)


btn = Button(window, text='clear', width=12, command=clear)
btn.place(x=10, y=350)

# Step4: mainloop
mainloop()


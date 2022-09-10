import tkinter as tk
from tkinter import *

# * - Button, Entry, Label
window = tk.Tk()
window.geometry("860x500")
window.title("My EMI Tkinter")


# The simple() will calculate the Simple Interest and EMI
# SI = (p * r * t) / 100
# EMI = P * R * ((1 + R) ** N) / ((1 + R) ** N) - 1
def simple():
    mySI = float(p.get()) * float(r.get()) * float(t.get())
    mySI2 = mySI / 100

    P = float(p.get())
    R = float(r.get()) / 12 / 100
    N = float(t.get()) * 12
    upper = P * R * ((1 + R) ** N)
    lower = ((1 + R) ** N) - 1
    emi = upper / lower
    lblResult.config(text="Simple Interest is " + str(mySI2) + "\n and EMI is " + str(emi))


# Principal - Label and Entry widget
lblP = Label(window, text="Enter Principal")
p = Entry(window)

# Rate - Label and Entry widget
lblR = Label(window, text="Enter Rate")
r = Entry(window)

# Time - Label and Entry widget
lblT = Label(window, text="Enter Time")
t = Entry(window)

# grid() method for Principal, Rate and Time fields
lblP.grid(column=0, row=0)
p.grid(column=1, row=0)

lblR.grid(column=0, row=1)
r.grid(column=1, row=1)

lblT.grid(column=0, row=2)
t.grid(column=1, row=2)

# Calculate SI - Button widget and its grid() method
btnSI = Button(window, text="Calculate SI", command=simple, bg='blue', fg='white')
btnSI.grid(column=1, row=3)

# Result - Label widget
lblResult = Label(window, text="Result Will Come Here", font=('Verdana', 20))
lblResult.grid(column=1, row=4)

window.mainloop()

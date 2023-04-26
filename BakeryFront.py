from tkinter import *
from tkinter import ttk

gui = Tk()

gui.configure(background="light yellow")

gui.title("Bakery Management")

gui.geometry("1024x768")

button1 = Button(gui, text= ' Products ', fg='Black', bg='dark yellow', 
                command=lambda: height=1, width=7)
button1.grid(row=2, column=0)


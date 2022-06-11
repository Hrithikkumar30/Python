from cProfile import label
from tabnanny import check
from tkinter import *
APP = Tk()
APP.geometry("200x200")

check = IntVar()#checkbox contain only integer variable
chk = Checkbutton(APP, text="Check box",variable=check) 
chk.deselect() #deselect checkbox
chk.pack()

def show():
    msg = Label(APP, text = check.get())
    msg.pack()
B = Button (APP, text = "Show", command = show)
B.pack()

APP.mainloop()
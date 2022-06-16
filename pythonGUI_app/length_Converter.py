from tkinter import *
App = Tk()
App.title("Length Converter")
App.geometry("300x150")

scales = ['Meters','Inches','Feet']
_from = StringVar() #_from is a variable that will be used to store the value of the dropdown menu
from_menu = OptionMenu(App,_from,*scales) #creates a dropdown menu
from_menu.grid(row=0,column=0) #places the dropdown menu in the grid

lbl = Label(App,text="Convert to:") #creates a label
lbl.grid(row=0,column=1) #places the label in the grid

to_ = StringVar() #_to is a variable that will be used to store the value of the dropdown menu
to_menu = OptionMenu(App,to_,*scales) #creates a dropdown menu
to_menu.grid(row=0,column=2)

enterLable = Label(App,text="Enter Value:") #creates a label
enterLable.grid(row=1,column=0) #places the label in the grid

numE = Entry(App) #creates a textbox
numE.grid(row=1,column=1) #places the textbox in the grid

def convert():
    From = _from.get()
    To = to_.get()
    num = numE.get()
    if From == "Meters" and To == "Inches":
        num = float(num) * 39.3701
        num = round(num,2)
    elif From=="Meters" and To == "Feet":
        num = float(num) * 3.28084
        num = round(num,2)
    elif From == "Inches" and To == "Meters":
        num = float(num) * 0.0254
        num = round(num,2)
    elif From == "Inches" and To == "Feet":
        num = float(num) * 0.0833333
        num = round(num,2)
    elif From ==  "Feet" and To == "Meters":
        num = float(num) * 0.3048
        num = round(num,2)
    elif From == "Feet" and To == "Inches":
        num = float(num) * 12
        num = round(num,2)
    else:
        num = num

    numL = Label(App,text=num) #creates a label
    numL.grid(row=1,column=2) #places the label in the grid

conB = Button(App,text="Convert",command=convert) #creates a button
conB.grid(row=2,column=0) #places the button in the grid

App.mainloop()
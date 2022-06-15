from tkinter import *
from datetime import datetime


App = Tk()
App.title("Age Calculator")

date = Label(App, text="Date")
date.grid(row=0, column=0)

inpD = Entry(App,width=2)
inpD.grid(column=1,row=0,)

month = Label(App, text="month")
month.grid(row=0, column=2)

inpM = Entry(App,width=2)
inpM.grid(column=3,row=0)

year = Label(App, text="year")
year.grid(row=0, column=4)

inpY = Entry(App,width=4)
inpY.grid(column=5,row=0)



def find_days():
    
    date = int(inpD.get())
    mon = int(inpM.get())
    year = int(inpY.get())
    dob = datetime(day= date, month = mon, year = year)
    time_now = datetime.now()
    time_dif = time_now - dob

    days =  Label(App,text = "You lived"+ str(time_dif.days) + "days")
    days.grid(row=3,column=0,columnspan=4)


def find_seconds():
    
    day = int(inpD.get())
    mon = int(inpM.get())
    yr = int(inpY.get())
    dob = datetime(day = day, month = mon, year = yr)
    time_now = datetime.now()
    time_dif = time_now - dob

    seconds = Label(App,text = "You lived"+ str(time_dif.total_seconds()) + "seconds")
    seconds.grid(row=4,column=0,columnspan=6)
    

DaysB = Button(App, text="Find Days", command=find_days)
DaysB.grid(row=2,column=0 ,padx=25,pady=5)
SeconndsB = Button(App, text="Find Seconds", command=find_seconds)
SeconndsB.grid(row=2,column=1,padx=45,pady=5)
App.mainloop()
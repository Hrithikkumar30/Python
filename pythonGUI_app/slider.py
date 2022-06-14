from random import choice, sample
from tkinter import *
# App = Tk()
# sld = Scale(App, from_=0, to=100, orient=HORIZONTAL) #this method used to create a scale
# sld.pack()    
# App.mainloop()









App =Tk()
App.title('Element picker')
App.geometry('350x200')
App['background'] = 'pink'

inp = Entry(App,background='grey',foreground='black')#this method used to create a entry/input field
inp.grid(column=0,row=0,columnspan=2,padx=35,pady=15)

no_choice = IntVar()
sld = Scale(App, from_=1, to=7, orient=HORIZONTAL,variable=no_choice) 
sld.grid(column=0,row=1,padx=35,pady=15)


def pick():
    INP = inp.get().split(',') #this method used to get the value of entry

    if no_choice.get() != 1:
        chois = 'Choice: ' + str(sample(INP ,no_choice.get()))
    else:
        chois = 'Choice: ' + str(choice(INP))


    msg = Label(App, text=chois, width=35, font=('Courier',12,'bold'),background='white',foreground='yellow')
    msg.grid(column=0,row=3,padx=45,columnspan=2,pady=5)
    if Bexit['state']== DISABLED: #this method used to disable button
        Bexit['state']=NORMAL #this method used to enable button
  
B = Button(App, text='pick', command=pick,background='white',foreground='black')
B.grid(column=0,row=2,padx=35,pady=15)

Bexit = Button(App, text='exit', command=App.destroy, state=DISABLED,background='red',foreground='black')
Bexit.grid(column=1,row=2,padx=35,pady=15)

App.mainloop()

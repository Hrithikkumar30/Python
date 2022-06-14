from tkinter import *
# from random import randint
from random import choice , sample

from matplotlib.pyplot import pink

# Normal Random Generator app

# App = Tk() #this class used to create a window
# App.title('App') #this method used to set title of window
# App.geometry('500x500') #this method used to set size of window

# Display = Label(App, text='Application Window') #this method used to create a label
# Display.pack() #this method used to display label

# def show_msg():
#     msg = Label(App, text=randint(1,100))
#     msg.pack()
# B = Button(App, text='Generate', command=show_msg) #this method used to create a button
# B.pack()
# App.mainloop() #this class used to run the window




# user input and display in window app

# App =Tk()
# App.title('Entry')
# App.geometry('350x100')

# inp = Entry(App)#this method used to create a entry/input field
# inp.pack()

# def entry():
#     INP = inp.get() #this method used to get the value of entry
#     msg = Label(App, text=INP)
#     msg.pack()
  
# B = Button(App, text='Show', command=entry)
# B.pack()
# App.mainloop()




# app for choose a item provided by user

App =Tk()
App.title('Element picker')
App.geometry('350x200')
App['background'] = 'pink'

inp = Entry(App,background='grey',foreground='black')#this method used to create a entry/input field
inp.grid(column=0,row=0,columnspan=2,padx=35,pady=15)

no_choice = IntVar()
chk = Checkbutton(App, text="Check box",variable=no_choice , onvalue=2, offvalue=1)
chk.deselect() #deselect checkbox
chk.grid(column=0,row=2,padx=35,pady=15)


def pick():
    INP = inp.get().split(',') #this method used to get the value of entry

    if no_choice.get() == 2:
        chois = 'Choice: ' + str(sample(INP ,2))
    else:
        chois = 'Choice: ' + str(choice(INP))


    msg = Label(App, text=chois, width=20, font=('Courier',12,'bold'),background='white',foreground='yellow')
    msg.grid(column=0,row=3,padx=45,columnspan=2,pady=5)
    if Bexit['state']== DISABLED: #this method used to disable button
        Bexit['state']=NORMAL #this method used to enable button
  
B = Button(App, text='pick', command=pick,background='white',foreground='black')
B.grid(column=0,row=1,padx=35,pady=15)

Bexit = Button(App, text='exit', command=App.destroy, state=DISABLED,background='red',foreground='black')
Bexit.grid(column=1,row=1,padx=35,pady=15)

App.mainloop()




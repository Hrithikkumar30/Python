from msilib.schema import RadioButton
from random import choice, sample
from tkinter import * 
# App = Tk()

# choice = StringVar()

# rb1 = Radiobutton(App , text = "Choice 1" , variable = choice , value = "1")
# rb2 = Radiobutton(App , text = "Choice 2" , variable = choice , value = "2")
# rb3 = Radiobutton(App , text = "Choice 3" , variable = choice , value = "3")
# rb1.pack()
# rb2.pack()

# def show():
#     msg = Label(App, text = choice.get())
#     msg.pack()

# B = Button(App, text='Show', command=show)
# B.pack()

# App.mainloop()







App =Tk()
App.title('Element picker')
App.geometry('350x200')
App['background'] = 'pink'

inp = Entry(App,background='grey',foreground='black')#this method used to create a entry/input field
inp.grid(column=0,row=0,columnspan=2,padx=35,pady=15)

no_choice = IntVar()
rb1 = Radiobutton(App , text = "Choice 1" , variable = no_choice , value = "1")
rb2 = Radiobutton(App , text = "Choice 2" , variable = no_choice , value = "2")
rb1.grid(column=0,row=1,padx=35,pady=15)
rb2.grid(column=1,row=1,padx=35,pady=15)


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
B.grid(column=0,row=2,padx=35,pady=15)

Bexit = Button(App, text='exit', command=App.destroy, state=DISABLED,background='red',foreground='black')
Bexit.grid(column=1,row=2,padx=35,pady=15)

App.mainloop()


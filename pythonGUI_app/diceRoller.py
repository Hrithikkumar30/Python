from tkinter import *
from turtle import width
# Dice unicode characters dictionary
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}
App = Tk()
App.title("Dice Roller")
dice = Label(App, text=Dice[0], font=('Times', 100), foreground="black")
dice.grid(row=0, column=0, padx=25, pady=5)

def roll():
    from random import randint
    dice_choice = randint(1, 6)
    msg = Label(App, text=Dice[dice_choice], font=('Times', 100), foreground="black", width=2)
    # dice.config(text=Dice[dice_choice])
    msg.grid(row=0, column=0, padx=25, pady=5)

rollButton = Button(App, text='Roll', command=roll)
rollButton.grid(row=1, column=0)
App.mainloop()
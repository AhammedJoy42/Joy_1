
from tkinter import *

# button = you click it, then it does stuff

jewel = Tk();

def click():
    print("You clicked the button!");

button = Button(jewel, text = "click me!", command= click,
                font = ("Comic sens!", 35),
                fg = 'green',
                bg = 'black');

button.pack();

jewel.mainloop();
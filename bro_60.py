
from tkinter import *

# label = an area widget that holds text and/or an image within a window

joy = Tk();

#photo = PhotoImage(file = '')

label = Label(joy, text = "Hello World",
              font = ('Arial', 40, 'bold'),
              fg = 'green',
              bg = 'black',
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20);
#label.pack();

label.place(x = 2, y = 2);
joy.mainloop();

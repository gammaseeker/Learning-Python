import tkinter
import random
from tkinter import *

root = tkinter.Tk()
#frame = Frame(root)
"""top = Toplevel(root)
top.title("About this application...")

msg = Message(top, text="xd")
msg.pack()

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()"""
Label(root, text="x =").grid(row=0)
Label(root, text="c =").grid(row=1)
Label(root, text="n =").grid(row=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
#frame.pack()

def buttonClick():
    print(e1.get())
    
"""bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )"""

sinButton = Button(root, command = buttonClick, text="Sin(x)", fg="red").grid(row=3, column=2, sticky=W, pady=4)
#sinButton.pack( side = LEFT)

cosButton = Button(root, command = buttonClick, text="Cos(x)", fg="brown").grid(row=3, column=3, sticky=W, pady=4)
#cosButton.pack( side = LEFT )

eButton = Button(root, command = buttonClick, text="e^(x)", fg="blue").grid(row=3, column=4, sticky=W, pady=4)
#eButton.pack( side = LEFT )

lnButton = Button(root, command = buttonClick, text="ln(x)", fg="black").grid(row=3, column=5, sticky=W, pady=4)
#lnButton.pack( side = BOTTOM)

arcTanButton = Button(root, command = buttonClick, text="arctan(x)", fg="blue").grid(row=3, column=6, sticky=W, pady=4)
#arcTanButton.pack( side = BOTTOM)

arcSinButton = Button(root, command = buttonClick, text="arcsin(x)", fg="blue").grid(row=3, column=7, sticky=W, pady=4)
#arcSinButton.pack( side = LEFT)

arcCosButton = Button(root, command = buttonClick, text="arccos(x)", fg="blue").grid(row=3, column=8, sticky=W, pady=4)
#arcCosButton.pack( side = LEFT)

root.mainloop()

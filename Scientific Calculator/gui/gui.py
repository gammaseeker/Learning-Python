import _tkinter
import tkinter
from tkinter import messagebox

#tkinter._test()
top = tkinter.Tk()
def helloCallBack():
    messagebox.showinfo("Title", "Hello World")
def helloAll():
    messagebox.showinfo("Test", "Test")

B = tkinter.Button(top, text = "Hello", command = helloCallBack())
C = tkinter.Button(top, text = "Test", command = helloAll())
B.pack(side = LEFT)
C.pack(side = RIGHT)
top.mainloop()

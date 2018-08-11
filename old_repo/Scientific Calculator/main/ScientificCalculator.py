#Joyce Feng
#Joey Jiemjitpolchai
import math
import tkinter
import random
from tkinter import *

root = tkinter.Tk()

Label(root, text="x =").grid(row=0)
Label(root, text="c =").grid(row=1)
Label(root, text="n =").grid(row=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)

def sinClick():
    print(calcSin(float(e1.get()), float(e2.get()), int(e3.get())))

def cosClick():
    print(calcCos(float(e1.get()), float(e2.get()), int(e3.get())))

"""def oneOverXPlusOneClick():
    print(calcOneOverXPlusOne(float(e1.get()), float(e2.get()), int(e3.get())))"""

def eClick():
    print(calcE(float(e1.get()), float(e2.get()), int(e3.get())))
def arcTanClick():
    print(calcArcTan(float(e1.get()), float(e2.get()), int(e3.get())))

def arcSinClick():
    print(calcArcSin(float(e1.get()), float(e2.get()), int(e3.get())))

def arcCosClick():
    print(calcArcCos(float(e1.get()), float(e2.get()), int(e3.get())))
                
def calcCos(x, c, n): #Tested
    if (n%2 == 1):
        return "Enter an even degree."
    sum = 0
    for k in range(0, math.ceil(n/2)+1):
        sum += ((-1)**k) * ((x-c)**(2*k))/math.factorial(2*k)
    return sum

def calcSin(x, c, n): #Tested
    if (n%2 == 0):
        return "Enter an odd degree."
    sum = 0
    for i in range (0, math.ceil(n/2)):
        sum += ((-1)**i)*((x-c)**(2*i+1))/math.factorial(2*i+1)
    return sum

""""def calcLn(x, c, n):#To be fixed
    if(x < 0):
        return("Enter an x between the range of 1 to infinity.")
    if (c < 1):
        return ("Enter a c between the range of 1 to infinity.")
    sum = 0
    for i in range (1, n+1):
            sum += (((-1)**(i-1))*((x-c)**i)/(i))
    return sum"""

"""def calcOneOverXPlusOne(x, c, n):
    if(x == -1):
        return "Enter another number."
    sum = 1
    for i in range(1, n + 1):
        sum += ((-1)**n) * (x-c)**n
    return sum"""

def calcE(x, c, n):#Tested
    sum = 0
    for i in range (0, n+1):
        sum += ((x-c)**i)/math.factorial(i)
    return sum

def calcArcTan(x, c, n):#Tested
    if (n%2 == 0):
        return("Enter an odd degree.")
    sum = 0
    for i in range(0, math.ceil(n/2)):
        sum += ((-1)**i)*((x-c)**(2*i+1))/(2*i+1)
    return sum

def calcArcSin(x, c, n):#Tested
    if (n%2 == 0):
        return("Enter an odd degree.")
    if (x < -1 or x > 1):
        return("Enter a number between the range of -1 to 1.")
    sum = 0
    for i in range (0, math.ceil(n/2)):
        sum += math.factorial(2*i)*(x**(2*i+1))/((((2**i)*math.factorial(i))**2)*(2*i+1))
    return sum

def calcArcCos(x, c, n):#Tested
    if (n%2 == 0):
        return("Enter an odd degree.")
    if (x < -1 or x > 1):
        return("Enter a number between the range of -1 to 1.")
    sum = (math.pi)/2
    for i in range (0, math.ceil(n/2)):
         sum -= ((math.factorial(2*i))*(x**(2*i+1)))/((2**(2*i))*((math.factorial(i))**2)*(2*i+1))
    return sum

sinButton = Button(root, command = sinClick, text="Sin(x)", fg="black").grid(row=3, column=2, sticky=W, pady=4)
cosButton = Button(root, command = cosClick, text="Cos(x)", fg="black").grid(row=3, column=3, sticky=W, pady=4)
eButton = Button(root, command = eClick, text="e^(x)", fg="black").grid(row=3, column=4, sticky=W, pady=4)
#lnButton = Button(root, command = oneOverXPlusOneClick, text="1/(1+x)", fg="black").grid(row=3, column=5, sticky=W, pady=4)
arcTanButton = Button(root, command = arcTanClick, text="arctan(x)", fg="black").grid(row=3, column=5, sticky=W, pady=4)
arcSinButton = Button(root, command = arcSinClick, text="arcsin(x)", fg="black").grid(row=3, column=6, sticky=W, pady=4)
arcCosButton = Button(root, command = arcCosClick, text="arccos(x)", fg="black").grid(row=3, column=7, sticky=W, pady=4)

root.mainloop()

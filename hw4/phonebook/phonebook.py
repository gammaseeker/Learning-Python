import tkinter
from tkinter import *
import shelve

root = tkinter.Tk()
records = []
flag = 0
class Record:
    def __init__(self, name, phone, address, rec_type):
        self.name = name
        self.phone = phone
        self.address = address
        self.rec_type = rec_type

def doRadio(ne_data, pe_data, ae_data, f):
    global records
    if not ne_data or not pe_data or not ae_data:
        r = tkinter.Tk()
        r.title("Error Window")
        r.geometry("500x100")
        e = Label(r, text="Enter all text fields")
        e.pack()

    if f == 1:#type = personal
        rec = Record(ne_data, pe_data, ae_data, "Personal")    
        records.append(rec)                

    else:
        if f == 2: # type = business
            rec = Record(ne_data, pe_data, ae_data, "Business")    
            records.append(rec)                
        else:
            r = tkinter.Tk()
            r.title("Error Window")
            r.geometry("500x100")
            e = Label(r, text="Error select a radio button")
            e.pack()

#TODO: add db functionality
def flagSelection(num):
    global flag
    flag = num

def record_window():
    r = tkinter.Tk()
    r.title("CSE 337 Phonebook")
    r.geometry("500x200")
    
    n = Label(r, text="Name")
    ne = Entry(r, width=40)
    p = Label(r, text="Phone")
    pe = Entry(r, width=40)
    a = Label(r, text="Address")
    ae = Entry(r, width=40)


    rad=StringVar()

    r1=Radiobutton(r, text="Personal", value="Personal", variable=rad, command=lambda: flagSelection(1)) 
    r2=Radiobutton(r, text="Business", value="Business", variable=rad, command=lambda: flagSelection(2))
    saveb = Button(r, text="Save record", command=lambda: doRadio(ne.get(), pe.get(), ae.get(), flag))

    n.pack()
    ne.pack()
    p.pack()
    pe.pack()
    a.pack()
    ae.pack()
    r1.pack()
    r2.pack()
    saveb.pack()

def search(name, r):
    global records
    if not name:
        Label(r, text="Enter a name").pack()
        return
    for record in records:
        if(record.name == name):
            Label(r, text="Record found:").pack()
            
            nameStr = "Name: " + record.name
            Label(r, text=nameStr).pack()
            
            phoneStr = "Phone: " + record.phone
            Label(r, text=phoneStr).pack()

            addrStr = "Address: " + record.address
            Label(r, text=addrStr).pack()
            
            typeStr = "Type: " + record.rec_type
            Label(r, text=typeStr).pack()
            return

        e = Label(r, text="Record does not exist")
        e.pack()

def delete(name, r):
    global records

    if not name:
        Label(r, text="Enter a name").pack()
        return
    for record in records:
        if(record.name == name):
            records.remove(record)
            Label(r, text="Success").pack()
            return

        e = Label(r, text="Record does not exist")
        e.pack()

def search_window():
    r = tkinter.Tk()
    r.title("CSE 337 Phonebook")
    r.geometry("500x200")

    n = Label(r, text="Name")
    ne = Entry(r, width=40)
    searchb = Button(r, text="Search", command= lambda: search(ne.get(), r))
    n.pack()
    ne.pack()
    searchb.pack()

def delete_window():
    r = tkinter.Tk()
    r.title("CSE 337 Phonebook")
    r.geometry("500x200")
    
    n = Label(r, text="Name")
    ne = Entry(r, width=40)
    deleteb = Button(r, text="Delete", command=lambda:delete(ne.get(), r))
    n.pack()
    ne.pack()
    deleteb.pack()
        
root.title("CSE 337 Phonebook")
root.geometry("500x200")

createb = Button(root, text="Create/Edit Record", command=record_window)
searchb = Button(root, text="Search Record", command=search_window)
deleteb = Button(root, text="Delete Record", command=delete_window)
#root.bind("<Button-1>")
createb.pack()
searchb.pack()
deleteb.pack()
root.mainloop()


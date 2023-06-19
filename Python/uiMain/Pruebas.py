from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x250')
ws.config(bg="grey")



Checkbutton(ws, text='0, 0').grid(row=0, column=0)
Checkbutton(ws, text='0, 1').grid(row=0, column=1)
Checkbutton(ws, text='0, 2').grid(row=0, column=1)
Checkbutton(ws, text='1, 0').grid(row=1, column=0)
Checkbutton(ws, text='1, 1').grid(row=1, column=1)
Checkbutton(ws, text='1, 2').grid(row=1, column=2)
Checkbutton(ws, text='2, 0').grid(row=2, column=0)
Checkbutton(ws, text='2, 1').grid(row=2, column=1)
Checkbutton(ws, text='2, 2').grid(row=2, column=2)

ws.mainloop()
from tkinter import *
 
ws = Tk() 
ws.geometry('300x250')
ws.title('Python Guides')

def clear_selection():
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    cb4.deselect()
    cb5.deselect()
    cb6.deselect()
    
var = BooleanVar() 
var.set(True)
 
cb1 = Checkbutton(ws, text='Click me!', variable=var)
cb1.pack()
cb2 = Checkbutton(ws, text='Click me!', variable=var)
cb2.pack()
cb3 = Checkbutton(ws, text='Click me!', variable=var)
cb3.pack()
cb4 = Checkbutton(ws, text='Click me!', variable=var)
cb4.pack()
cb5 = Checkbutton(ws, text='Click me!', variable=var)
cb5.pack()
cb6 = Checkbutton(ws, text='Click me!', variable=var)
cb6.pack()

Button(ws, text='Deselect All Check buttons', command=clear_selection).pack()



 
ws.mainloop()
#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x250")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")
txt=Text(frame,state="normal")
txt.place(relheight=0.60, rely=0.35, relwidth=0.25, relx=0.02)

#Create a text label
Label(frame,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

#Create a button to close the window
Button(frame, text="Clear", font=('Helvetica bold', 10), command=
clear_frame).pack(pady=20)

win.mainloop()
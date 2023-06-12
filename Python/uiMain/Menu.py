import tkinter
from tkinter import*

ventanaInicio = Tk()
ventanaInicio.title ("Inicio")
ventanaInicio.geometry ("500x500")

menuBar=Menu(ventanaInicio)
ventanaInicio.config(menu=menuBar)

menuInicio=Menu(menuBar)
menuBar.add_cascade(label="Menu 123", menu=menuInicio)

ventanaInicio.rowconfigure(0, weight=1)  
ventanaInicio.columnconfigure(0, weight=1) 

ventanaInicio.columnconfigure(0, weight=1)
ventanaInicio.columnconfigure(1, weight=1)

frame1 = Frame(ventanaInicio, bg="lightpink1", borderwidth=1, relief="solid")
frame1.grid(row=0, column=0, sticky="nsew", padx=3)

frame2 = Frame(ventanaInicio, bg="DeepSkyBlue2",borderwidth=1, relief="solid")
frame2.grid(row=0, column=1, sticky="nsew", padx=3) 


frameP3=Frame(frame1, bg="red", height=200, width=200)
frameP3.place(relheight=0.3, relwidth=1)


ventanaInicio.mainloop()
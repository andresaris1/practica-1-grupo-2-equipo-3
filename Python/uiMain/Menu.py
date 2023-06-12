import tkinter
from tkinter import*

ventanaInicio = Tk()
ventanaInicio.title ("Inicio")
ventanaInicio.geometry ("500x500")

menuBar=Menu(ventanaInicio)
ventanaInicio.config(menu=menuBar)

menuInicio=Menu(menuBar)
menuBar.add_cascade(label="Inicio", menu=menuInicio)
menuInicio.add_command(label="Salir",)
menuInicio.add_command(label="Descripción",)

menuInicio.config(activebackground="sienna1")

ventanaInicio.rowconfigure(0, weight=1)  
ventanaInicio.columnconfigure(0, weight=1) 

ventanaInicio.columnconfigure(0, weight=1)
ventanaInicio.columnconfigure(1, weight=1)

frame1 = Frame(ventanaInicio, bg="lightpink1", borderwidth=1, relief="solid")
frame1.grid(row=0, column=0, sticky="nsew", padx=3)

frame2 = Frame(ventanaInicio, bg="DeepSkyBlue2",borderwidth=1, relief="solid")
frame2.grid(row=0, column=1, sticky="nsew", padx=3) 


frameP3=Frame(frame1, bg="purple", height=200, width=200, borderwidth=1, relief="solid")
frameP3.pack(side="top", fill="x", padx=3, pady=3)

frameP4=Frame(frame1, bg="green", height=200, width=200, borderwidth=1, relief="solid")
frameP4.pack(expand=True, fill="both", padx=3, pady=3)

frameP5=Frame(frame2, bg="red", height=200, width=200, borderwidth=1, relief="solid")
frameP5.pack(side="top", fill="x", padx=3, pady=3)

frameP6=Frame(frame2, bg="orange", height=200, width=200, borderwidth=1, relief="solid")
frameP6.pack(expand=True, fill="both", padx=3, pady=3)


ventanaInicio.mainloop()
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk

import os

def AbrirFuncional():
    ventanaFuncional.state(newstate = "normal")
    ventanaInicio.state(newstate = "withdraw")
    

#CREACION DE LA VENTANA DE INICIO
ventanaInicio = Tk()
ventanaInicio.title ("Sistema de gestion hotelera")
ventanaInicio.geometry ("500x500")

menuBar=Menu(ventanaInicio)
ventanaInicio.config(menu=menuBar)

menuInicio=Menu(menuBar, tearoff=0)
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

#Zona P3 Bienvenidad
Bienvenida=Label(frameP3,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion hotelera UN 3000 ", font=("Arial", 20))
Bienvenida.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.7, anchor='center')

#Zona P4 Carrusel de imagnes y Boton de incio
path=os.path.join(os.path.dirname(__file__), "img/hotel.png")

imgHotel=tk.PhotoImage(file=path)
labelCarrusel=Label(frameP4,image=imgHotel)
labelCarrusel.pack(side="top")

BotonInicio=Button(frameP4,text="INCIO", command=AbrirFuncional)
BotonInicio.pack(side="bottom")


#CREACION DE LA VENTANA FUNCIONAL
ventanaFuncional = Tk()
ventanaFuncional.title ("Sistema de gestion hotelera")
ventanaFuncional.geometry ("500x500")
ventanaFuncional.state(newstate = "withdraw")

#Label de prueba
lprueba=Label(ventanaFuncional,text="Label para probar que la\n nueva ventana funciona")

ventanaInicio.mainloop()
ventanaFuncional.mainloop()
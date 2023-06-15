import tkinter as tk
from tkinter import *
from tkinter import messagebox

import os
def Aplicacion():
    messagebox.showinfo("Sistema de gestion hotelera UN 3000","Bienvenido, este es el nuevo sistema de gestion hotelera 3000.\nEste sistema cuenta con  las siguientes opciones:\n\n- Registro de usuarios\n\n- Reserva de alojamiento\n\n- Reserva Turistica\n\n- Reserva de eventos\n\n- Informacion de las instalaciones\n\n- Adicion de servicios\n\nGracias por preferirnos ;)")

def Acercade():
    messagebox.showinfo("Integrantes","Este es el nuevo sistema de gestion hotelera 300\n(Ahora con Interfaz Grafica)\nCreada como proyecto para la materia POO 2023-1s por:\n\nJuan José Lotero Florez\n\nCarolina Humanez Urrego\n\nSebastian Mendoza Gonzalez\n\nAndrés Felipe Arismendi Alzate\n\nMiguel Angel Quiceno Hincapie\n\nBest Team Ever")

def reiniciar():
    for widgets in frame2.winfo_children():
      widgets.destroy()
    Aceptar=Button(frame2, text="Aceptar", font=("Arial", 14), relief=RAISED)
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)
    Cancelar=Button(frame2, text="Cancelar", command=lambda:[bienvenido(),reiniciar()], font=("Arial", 14), relief=RAISED)
    Cancelar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.75)

def bienvenido():
    frame3.place(relheight=1, relwidth=1)
    
    Presentacion=Label(frame3,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion hotelera UN 3000 ", font=("Arial", 20), bg="light steel blue")
    Presentacion.place(relx=0.5, rely=0.5, anchor='center')


def Registro():
    reiniciar()
    frame3.place_forget()
    Titulo.config(text="Registro de nuevos usuarios")
    Descripcion.config(text="Realiza el registro del nuevo cliente. Por favor complete los siguentes datos")

    Documento=Label(frame2,text="No. Documento", font=("Arial", 13))
    Documento.place(relheight=0.125, relwidth=0.2, rely=0.10, relx=0.2)
    Nombre=Label(frame2, text="Nombre", font=("Arial", 13))
    Nombre.place(relheight=0.125, relwidth=0.2, rely=0.25, relx=0.2)
    Telefono=Label(frame2, text="Telefono", font=("Arial", 13))
    Telefono.place(relheight=0.125, relwidth=0.2, rely=0.40, relx=0.2)
    CuentaBancaria=Label(frame2, text="Cuenta Bancaria", font=("Arial", 13))
    CuentaBancaria.place(relheight=0.125, relwidth=0.2, rely=0.55, relx=0.2)

    Doc=Entry(frame2)
    Doc.place(relheight=0.0625, relwidth=0.3, rely=0.13, relx=0.45)
    Nom=Entry(frame2)
    Nom.place(relheight=0.0625, relwidth=0.3, rely=0.28, relx=0.45)
    Tel=Entry(frame2)
    Tel.place(relheight=0.0625, relwidth=0.3, rely=0.43, relx=0.45)
    Cub=Entry(frame2)
    Cub.place(relheight=0.0625, relwidth=0.3, rely=0.58, relx=0.45)


def Alojamiento():
    reiniciar()
    frame3.place_forget()

    Titulo.config(text="Reserva nueva de alojamiento")
    Descripcion.config(text="Realiza una nueva reserva de alojamiento")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad1", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Tour():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Reserva nueva de Tour")
    Descripcion.config(text="Realiza una nueva reserva de Tour")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad2", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Eventos():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Reserva nueva de eventos")
    Descripcion.config(text="Realiza una nueva reserva de evento en nuestras instalaciones")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad3", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Adicionales():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Adicion de servicios")
    Descripcion.config(text="Realiza una adicion de servicios")

    frame2.config(bg="lightpink")
    Documento=Label(frame2,text="No. Documento", font=("Arial", 10))
    Documento.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.02)
    Nombre=Label(frame2, text="Nombre", font=("Arial", 10))
    Nombre.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.4)
    Telefono=Label(frame2, text="Telefono", font=("Arial", 13))
    Telefono.place(relheight=0.125, relwidth=0.2, rely=0.40, relx=0.2)
    CuentaBancaria=Label(frame2, text="Cuenta Bancaria", font=("Arial", 13))
    CuentaBancaria.place(relheight=0.125, relwidth=0.2, rely=0.55, relx=0.2)

    Doc=Entry(frame2)
    Doc.place(relheight=0.0625, relwidth=0.3, rely=0.13, relx=0.45)
    Nom=Entry(frame2)
    Nom.place(relheight=0.0625, relwidth=0.3, rely=0.28, relx=0.45)
    Tel=Entry(frame2)
    Tel.place(relheight=0.0625, relwidth=0.3, rely=0.43, relx=0.45)
    Cub=Entry(frame2)
    Cub.place(relheight=0.0625, relwidth=0.3, rely=0.58, relx=0.45)

def Informacion():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Informacion")
    Descripcion.config(text="Consulta la informacion de nuestras instalaciones")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad5", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Cobro():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Generador de cobros")
    Descripcion.config(text="Genera el cobro del cliente a la hora de salir")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad6", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')




def AbrirFuncional():
    window.state(newstate = "normal")
    ventanaInicio.state(newstate = "withdraw")

def AbrirInicio():
    ventanaInicio.state(newstate = "normal")
    window.state(newstate = "withdraw")

def Cerrartodo():
    ventanaInicio.destroy()
    window.destroy()

def Carrusel(event):
    global indiceImagen
    global listImage

    if indiceImagen < 4:
        indiceImagen += 1
    else:
        indiceImagen = 1

    nextImagen=listImage[indiceImagen]
    botonCarrusel.config(image=nextImagen)

#CREACION DE LA VENTANA DE INICIO
ventanaInicio = Tk()
ventanaInicio.title ("Sistema de gestion hotelera")
ventanaInicio.geometry ("500x500")
ventanaInicio.protocol("WM_DELETE_WINDOW", Cerrartodo)

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

frame1 = Frame(ventanaInicio, bg="light steel blue", borderwidth=1, relief="solid")
frame1.grid(row=0, column=0, sticky="nsew", padx=3)

frame2 = Frame(ventanaInicio, bg="light steel blue",borderwidth=1, relief="solid")
frame2.grid(row=0, column=1, sticky="nsew", padx=3)


frameP3=Frame(frame1, bg="white", height=200, width=200, borderwidth=1, relief="solid")
frameP3.pack(side="top", fill="x", padx=3, pady=3)

frameP4=Frame(frame1, bg="white", height=200, width=200, borderwidth=1, relief="solid")
frameP4.pack(expand=True, fill="both", padx=3, pady=3)

frameP5=Frame(frame2, bg="white", height=200, width=200, borderwidth=1, relief="solid")
frameP5.pack(side="top", fill="x", padx=3, pady=3)

frameP6=Frame(frame2, bg="white", height=200, width=200, borderwidth=1, relief="solid")
frameP6.pack(expand=True, fill="both", padx=3, pady=3)

#Zona P3 Bienvenidad
Bienvenida=Label(frameP3,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion hotelera UN 3000 ", font=("Arial", 20))
Bienvenida.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.7, anchor='center')

#Zona P4 Carrusel de imagnes y Boton de incio
pathImgHotel=os.path.join(os.path.dirname(__file__), "img/hotel.png")
pathImgPiscina=os.path.join(os.path.dirname(__file__), "img/piscina.png")
pathImgDestino1=os.path.join(os.path.dirname(__file__), "img/destino1.png")
pathImgDestino2=os.path.join(os.path.dirname(__file__), "img/destino2.png")
pathImgDef=os.path.join(os.path.dirname(__file__), "img/def.png")

imgHotel=tk.PhotoImage(file=pathImgHotel)
imgPiscina=tk.PhotoImage(file=pathImgPiscina)
imgDestino1=tk.PhotoImage(file=pathImgDestino1)
imgDestino2=tk.PhotoImage(file=pathImgDestino2)
imgDef=tk.PhotoImage(file=pathImgDef)

listImage=[imgDef, imgHotel, imgPiscina, imgDestino1, imgDestino2]
indiceImagen=0

botonCarrusel=Button(frameP4,image=imgHotel, command=lambda:[AbrirFuncional(),bienvenido()])
botonCarrusel.pack(expand=True)
botonCarrusel.bind("<Enter>",Carrusel)


#CREACION DE LA VENTANA FUNCIONAL
window = Tk()
window.title("Gestion Hotelera UN3000")
window.geometry("700x480")
window.state(newstate="withdraw")
window.protocol("WM_DELETE_WINDOW", Cerrartodo)
menuBar=Menu(window)
window.config(menu=menuBar)

menuArchivo=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Aplicación",command=Aplicacion)
menuArchivo.add_command(label="Salir",command=AbrirInicio)

menuProcesos=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesos, )
menuProcesos.add_command(label="Registrar Usuario",command=Registro)
menuProcesos.add_command(label="Reservar Alojamiento",command=Alojamiento)
menuProcesos.add_command(label="Reservar Tour",command=Tour)
menuProcesos.add_command(label="Reservar evento",command=Eventos)
menuProcesos.add_command(label="Servicios Adicionales",command=Adicionales)
menuProcesos.add_command(label="Informacion",command=Informacion)
menuProcesos.add_command(label="Generar Cobro",command=Cobro)

menuAyuda=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Ayuda", menu=menuAyuda)

menuAyuda.add_command(label="Acerca de...", command=Acercade)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

frame1 = Frame(window, borderwidth=1, relief="solid")

Titulo=Label(frame1,text="", font=("Arial Bold", 20))
Titulo.place(relx=0.5, rely=0.35, anchor='center')
Descripcion=Label(frame1,text="", font=("Arial", 12))
Descripcion.place(relx=0.5, rely=0.7, anchor='center')
    
frame2 = Frame(window, borderwidth=1, relief="solid")
frame3 = Frame(window, borderwidth=1, relief="solid")

frame1.place(relheight=0.2, relwidth=1, rely=0)
frame2.place(relheight=0.8, relwidth=1, rely=0.2)


ventanaInicio.mainloop()
window.mainloop()
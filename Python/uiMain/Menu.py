import tkinter as tk
from tkinter import*

import os

def reiniciar():
    print("holas")
    frame1.destroy()
    frame2.destroy()
    Presentacion.place(relx=0.5, rely=0.4, anchor='center')


def Registro():
    
    Presentacion.place_forget()
    
    frame1.place(relheight=0.2, relwidth=1, rely=0)

    Titulo=Label(frame1,text="Registro de nuevos usuarios", font=("Arial Bold", 20))
    Titulo.place(relx=0.5, rely=0.35, anchor='center')
    Descripcion=Label(frame1,text="Realiza el registro del nuevo cliente. Por favor complete los siguentes datos", font=("Arial", 12))
    Descripcion.place(relx=0.5, rely=0.6, anchor='center')
    
    frame2 = Frame(window, borderwidth=1, relief="solid")
    frame2.place(relheight=0.8, relwidth=1, rely=0.2)

    Documento=Label(frame2,text="No. Documento")
    Documento.place(relheight=0.1, relwidth=0.2, rely=0.1, relx=0.2)
    Nombre=Label(frame2, text="Nombre")
    Nombre.place(relheight=0.1, relwidth=0.2, rely=0.2, relx=0.2)
    Telefono=Label(frame2, text="Telefono")
    Telefono.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.2)
    CuentaBancaria=Label(frame2, text="Cuenta Bancaria")
    CuentaBancaria.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

    Doc=Entry(frame2)
    Doc.place(relheight=0.06, relwidth=0.3, rely=0.12, relx=0.4)
    Nom=Entry(frame2)
    Nom.place(relheight=0.06, relwidth=0.3, rely=0.22, relx=0.4)
    Tel=Entry(frame2)
    Tel.place(relheight=0.06, relwidth=0.3, rely=0.32, relx=0.4)
    Cub=Entry(frame2)
    Cub.place(relheight=0.06, relwidth=0.3, rely=0.42, relx=0.4)

    Aceptar=Button(frame2, text="Aceptar")
    Aceptar.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.52)
    Cancelar=Button(frame2, text="Cancelar", command=reiniciar)
    Cancelar.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.75)

def Alojamiento():
    frame1.config(bg="lightgreen")
    Bienvenida.config(text="Aqui va\nReserva de Alojamiento", bg="lightgreen")

def Tour():
    frame1.config(bg="red")
    Bienvenida.config(text="Aqui va\nReserva de Tour", bg="red")

def Eventos():
    frame1.config(bg="lightblue")
    Bienvenida.config(text="Aqui va\nReserva de Eventos", bg="lightblue")

def Adicionales():
    frame1.config(bg="orange")
    Bienvenida.config(text="Aqui va\nReserva de S. Adicionale", bg="orange")

def Informacion():
    frame1.config(bg="purple")
    Bienvenida.config(text="Aqui va informacion", bg="purple")

def Cobro():
    frame1.config(bg="yellow")
    Bienvenida.config(text="Aqui va cobro", bg="yellow")




def AbrirFuncional():
    window.state(newstate = "normal")
    ventanaInicio.destroy()

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

botonCarrusel=Button(frameP4,image=imgHotel, command=AbrirFuncional)
botonCarrusel.pack(expand=True)
botonCarrusel.bind("<Enter>",Carrusel)


#CREACION DE LA VENTANA FUNCIONAL
window = Tk()
window.title("Gestion Hotelera UN3000")
window.geometry("700x600")
window.state(newstate="withdraw")

menuBar=Menu(window)
window.config(menu=menuBar)

menuArchivo=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Aplicación",)
menuArchivo.add_command(label="Salir",)

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

menuAyuda.add_command(label="Acerca de...",)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

frame1 = Frame(window, borderwidth=1, relief="solid")
frame1.place(relheight=1, relwidth=1)


Presentacion=Label(frame1,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion hotelera UN 3000 ", font=("Arial", 20), bg="light steel blue")
Presentacion.place(relx=0.5, rely=0.4, anchor='center')

ventanaInicio.mainloop()
window.mainloop()
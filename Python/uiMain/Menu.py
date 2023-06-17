import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.dirname(__file__) + "/../baseDatos")
from Almacenamiento import *
from datetime import datetime
import functools



def Aplicacion():
    messagebox.showinfo("Sistema de gestion del Hotel UN 2.0","Bienvenido, este es el nuevo sistema de gestion hotelera 3000.\nEste sistema cuenta con  las siguientes opciones:\n\n- Registro de usuarios\n\n- Reserva de alojamiento\n\n- Reserva Turistica\n\n- Reserva de eventos\n\n- Informacion de las instalaciones\n\n- Adicion de servicios\n\nGracias por preferirnos ;)")

def Acercade():
    messagebox.showinfo("Integrantes","Este es el nuevo sistema de gestion del Hotel UN 2.0\n(Ahora con Interfaz Grafica)\nCreada como proyecto para la materia POO 2023-1s por:\n\nJuan José Lotero Florez\n\nCarolina Humanez Urrego\n\nSebastian Mendoza Gonzalez\n\nAndrés Felipe Arismendi Alzate\n\nMiguel Angel Quiceno Hincapie\n\nBest Team Ever")

def reiniciar():
    for widgets in frame2.winfo_children():
      widgets.destroy()
    
    Cancelar=Button(frame2, text="Cancelar", command=lambda:[bienvenido(),reiniciar()], font=("Arial", 14), relief=RAISED)
    Cancelar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.75)

def bienvenido():
    frame3.place(relheight=1, relwidth=1)
    
    Presentacion=Label(frame3,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion del Hotel UN 2.0 ", font=("Arial", 20), bg="light steel blue")
    Presentacion.place(relx=0.5, rely=0.5, anchor='center')



def buscador():
    def Rellenar(Docu):
        global cliente
        cliente=Almacenamiento.buscarUsuario(Docu)
        Nom.config(state="normal")
        Tel.config(state="normal")
        Cub.config(state="normal")
        Doc.delete(0,END)
        Nom.delete(0,END)
        Tel.delete(0,END)
        Cub.delete(0,END)
        if cliente!=None:
            Doc.insert(0, cliente.getIdentificacion())
            Nom.insert(0, cliente.getNombre())
            Tel.insert(0, cliente.getTelefono())
            Cub.insert(0, cliente.get_cuenta_bancaria())
        else:
            messagebox.showerror("Usuario no encontrado","Este usuario no está registrado en la base de datos")
        Nom.config(state="disabled")
        Tel.config(state="disabled")
        Cub.config(state="disabled")
        return cliente


    Documento=Label(frame2,text="No. Documento", font=("Arial", 10), anchor="w")
    Documento.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.05)
    Nombre=Label(frame2, text="Nombre", font=("Arial", 10), anchor="w")
    Nombre.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.48)
    Telefono=Label(frame2, text="Telefono", font=("Arial", 10), anchor="w")
    Telefono.place(relheight=0.05, relwidth=0.15, rely=0.15, relx=0.05)
    CuentaBancaria=Label(frame2, text="Cuenta Bancaria", font=("Arial", 10), anchor="w")
    CuentaBancaria.place(relheight=0.05, relwidth=0.15, rely=0.15, relx=0.48)

    Doc=Entry(frame2)
    Doc.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.2)

    Buscar=Button(frame2, text="Buscar", font=("Arial", 10), command=lambda:Rellenar(Doc.get()))
    Buscar.place(relheight=0.05, relwidth=0.1, rely=0.05, relx=0.35)

    Nom=Entry(frame2)
    Nom.place(relheight=0.05, relwidth=0.25, rely=0.05, relx=0.65)
    Tel=Entry(frame2)
    Tel.place(relheight=0.05, relwidth=0.25, rely=0.15, relx=0.2)
    Cub=Entry(frame2)
    Cub.place(relheight=0.05, relwidth=0.25, rely=0.15, relx=0.65)



def Registro():
    def registrarUsuario(nombre, id, telefono, cuentaBan):
        cliente=Almacenamiento.buscarUsuario(id)
        if cliente!=None:
            messagebox.showerror("Usuario ya registrado","Este usuario ya se encuentra registrado en la base de datos del hotel")
        else:
            Almacenamiento.crearUsuario(nombre, id, telefono, cuentaBan)
            messagebox.showinfo("Usuario Registrado con Exito","Usuario Registrado con Exito.\n\nIdentificacion:\t"+id+"\n\nNombre:\t"+nombre+"\n\nTelefono:\t"+telefono+"\n\nCuenta Bancaria:\t"+cuentaBan+"\n\nBienvenido")
        Doc.delete(0,END)
        Nom.delete(0,END)
        Tel.delete(0,END)
        Cub.delete(0,END)

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

    Aceptar=Button(frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=lambda: registrarUsuario(Nom.get(), Doc.get(), Tel.get(), Cub.get()))
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)

def Alojamiento():
    listahabitaciones=[]
    def formarfecha(texto):
        if len(texto) > 10:
            return False
        fecha = []
        for i, char in enumerate(texto):
            if i in (2, 5):
                fecha.append(char == "/")
            else:
                fecha.append(char.isdecimal())
        return all(fecha)

    def dosDigitos(caracter, texto):
        if len(texto) > 2:
            return False
        return caracter.isdecimal()
    
    def seleccionar(num):
        txt.config(state="normal")
        for i in Almacenamiento.listaHabitaciones:
            if num==i.getNumero():
                if i not in listahabitaciones:
                    listahabitaciones.append(i)
                    txt.insert(END,"\nHabitacion:"+str(i.getNumero()))
                    txt.config(state="disabled")
                    break

    def verificar():
        if cliente!=None:
            txt.config(state="normal")
            txt.insert(END,"Habitaciones\nReservadas:")
            txt.config(state="disabled")
            global fen
            global fsa
            fen=datetime.strptime(fechaEntrada.get(), "%d/%m/%Y")
            fsa=datetime.strptime(fechaSalida.get(), "%d/%m/%Y")
            actual=datetime.now()
            cantidad=int(personas.get())
            if fsa<fen or fsa<actual or fen<actual:
                messagebox.showerror("Fechas invalidas","Las fechas ingresadas no son validas")
            else:
                hadis=[]
                for reservas in Almacenamiento.listaReservas:
                    if (fe>reservas.getFechaSalida()) or (fs<reservas.getFechaEntrada()):
                        for habitaciones in reservas.getHabitaciones():
                            hadis.append(habitaciones)


                for habis in Almacenamiento.listaHabitacionesDisponibles:
                    hadis.append(habis)
                x=0.4
                y=0.3
                cont=0
                for i in hadis:
                    boton=Button(frame2, text=i.getNombre(), font=("Arial", 14), relief=RAISED, command=functools.partial(seleccionar, i.getNumero()))
                    boton.place(relheight=0.1, relwidth=0.1, rely=y, relx=x)
                    cont+=1
                    x+=0.15
                    if cont==2:
                        cont=0
                        x=0.4
                        y+=0.15

        else:
            messagebox.showerror("Sin Usuario","No hay usuario registrado")
        
    def reservar():
        Almacenamiento.crearReserva(fen,fsa,listahabitaciones,0,cliente)
        Almacenamiento.crearFactura(cliente,emp,listahabitaciones,"Reserva")
        for i in listahabitaciones:
            if i in Almacenamiento.listaHabitacionesDisponibles:
                Almacenamiento.listaHabitacionesDisponibles.remove(i)

        print(Almacenamiento.listaReservas)
        print(Almacenamiento.listaFacturas)
        print(Almacenamiento.listaHabitacionesDisponibles)
        messagebox.showinfo("Reserva realizada", "Reserva realizada con exito")
        bienvenido()

    reiniciar()
    buscador()
    frame3.place_forget()

    Titulo.config(text="Reserva nueva de alojamiento")
    Descripcion.config(text="Realiza una nueva reserva de alojamiento")

    w=Label(frame2,text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    w.place(relheight=0.05, relwidth=1,rely=0.20)

    fe=Label(frame2, text="Fecha de entrada", font=("Arial", 10), anchor="w")
    fe.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.02)
    fs=Label(frame2, text="Fecha de salida", font=("Arial", 10), anchor="w")
    fs.place(relheight=0.1, relwidth=0.2, rely=0.45, relx=0.02)
    cp=Label(frame2, text="¿Para cuantas personas?", font=("Arial", 10), anchor="w")
    cp.place(relheight=0.1, relwidth=0.25, rely=0.6, relx=0.02)

    Buscar=Button(frame2, text="Buscar", font=("Arial", 10), command=verificar)
    Buscar.place(relheight=0.1, relwidth=0.2, rely=0.75, relx=0.08)

    fechaEntrada =Entry(frame2, font=("Arial", 14),justify="right",validate="key",validatecommand=(frame2.register(formarfecha), "%P"))
    fechaEntrada.place(relheight=0.1, relwidth=0.17, rely=0.3, relx=0.18)
    fechaSalida=Entry(frame2, font=("Arial", 14),justify="right",validate="key",validatecommand=(frame2.register(formarfecha), "%P"))
    fechaSalida.place(relheight=0.1, relwidth=0.17, rely=0.45, relx=0.18)
    personas=Entry(frame2, font=("Arial", 14),justify="center",validate="key",validatecommand=(frame2.register(dosDigitos), "%S", "%P"))
    personas.place(relheight=0.1, relwidth=0.05, rely=0.6, relx=0.30)
    txt=Text(frame2,state="disabled")
    txt.place(relheight=0.4, rely=0.3, relwidth=0.25, relx=0.7)

    adv=Label(frame2, text="*Ingrese las fechas en formato dd/mm/aaaa", font=("Arial", 8), anchor="center", state="disabled")
    adv.place(relheight=0.1, relwidth=0.35, rely=0.9, relx=0.02)

    Aceptar=Button(frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=reservar)
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)

def Tour():
    reiniciar()
    buscador()
    frame3.place_forget()
    
    Titulo.config(text="Reservar un Tour")
    Descripcion.config(text="crearemos una reserva de tour que estara encargada una empresa externa,\n solo nos encargaremos de agregar la lista de la reserva de Tour y la factura de costo")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad2", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Eventos():
    reiniciar()
    buscador()
    frame3.place_forget()
    
    Titulo.config(text="Reserva nueva de eventos")
    Descripcion.config(text="Realiza una nueva reserva de evento en nuestras instalaciones")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad3", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Adicionales():
    reiniciar()
    buscador()
    frame3.place_forget()
    
    Titulo.config(text="Adicion de servicios")
    Descripcion.config(text="Realiza una adicion de servicios")

def Informacion():
    reiniciar()
    frame3.place_forget()
    
    Titulo.config(text="Informacion")
    Descripcion.config(text="Consulta la informacion de nuestras instalaciones")

    info=Label(frame2,text="Aqui desarrollen su funcionalidad5", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor='center')

def Cobro():
    reiniciar()
    buscador()
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
Bienvenida=Label(frameP3,text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion del Hotel UN 2.0 ", font=("Arial", 20))
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
window.title("Gestion del Hotel UN 2.0")
window.geometry("1280x720")
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


#OBJETOS TEMPORALES PARA PRUEBAS
habitacion1=Almacenamiento.crearHabitacion(101,"Habitacion Individual",101,1)
habitacion2=Almacenamiento.crearHabitacion(102,"Habitacion Individual",102,1)
habitacion3=Almacenamiento.crearHabitacion(201,"Habitacion Doble",201,2)
habitacion4=Almacenamiento.crearHabitacion(202,"Habitacion Doble",202,2)
habitacion5=Almacenamiento.crearHabitacion(301,"Habitacion Familiar",301,4)
habitacion6=Almacenamiento.crearHabitacion(302,"Habitacion Familiar",302,4)

c1=Almacenamiento.crearUsuario("Carlos","1",1,1)

emp=Almacenamiento.crearEmpleado("Recepcion",0,0,"Recepcion")
print(Almacenamiento.listaHabitaciones)
print(Almacenamiento.listaUsuarios)


ventanaInicio.mainloop()
window.mainloop()


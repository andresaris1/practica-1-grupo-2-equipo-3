import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter.ttk import Combobox
sys.path.append(os.path.dirname(__file__) + "/../baseDatos")
from Almacenamiento import *
from datetime import datetime
import functools


"""Metodo Aplicacion crea un messagebox que se muestra a la hora de hacer clic en el boton
   Aplicacion en el submeú  "Archivo" del menú de la applicacion"""


def Aplicacion():
    messagebox.showinfo(
        "Sistema de gestion del Hotel UN 2.0",
        "Bienvenido, este es el nuevo sistema de gestion hotelera 3000.\nEste sistema cuenta con  las siguientes opciones:\n\n- Registro de usuarios\n\n- Reserva de alojamiento\n\n- Reserva Turistica\n\n- Reserva de eventos\n\n- Informacion de las instalaciones\n\n- Adicion de servicios\n\nGracias por preferirnos ;)",
    )


"""Metodo Acercade: crea un messagebox que se muestra a la hora de hacer clic en el boton
   "Acerca de.." en el submeú  "Ayuda" del menú de la aplicacion"""


def Acercade():
    messagebox.showinfo(
        "Integrantes",
        "Este es el nuevo sistema de gestion del Hotel UN 2.0\n(Ahora con Interfaz Grafica)\nCreada como proyecto para la materia POO 2023-1s por:\n\nJuan José Lotero Florez\n\nCarolina Humanez Urrego\n\nSebastian Mendoza Gonzalez\n\nAndrés Felipe Arismendi Alzate\n\nMiguel Angel Quiceno Hincapie\n\nBest Team Ever",
    )


""""Metodo reiniciar: borra todo lo que hay en el frame2 para formarlo desde 0 cada vez que se selecciona
    uno de los procesos que realiza la aplicacion """


def reiniciar():
    "Borrar todo lo que hay en el frame2"
    for widgets in frame2.winfo_children():
        widgets.destroy()

    """Agrega el boton "Cancelar" utilizado en cada una de las ventanas de procesos"""
    Cancelar = Button(
        frame2,
        text="Cancelar",
        command=lambda: [bienvenido(), reiniciar()],
        font=("Arial", 14),
        relief=RAISED,
    )
    Cancelar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.75)


""""Metodo bienvenid: posiciona el frame3 para volver a la pantalla de inicio"""


def bienvenido():
    frame3.place(relheight=1, relwidth=1)

    Presentacion = Label(
        frame3,
        text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion hotelera UN 3000 ",
        font=("Arial", 20),
        bg="light steel blue",
    )
    Presentacion.place(relx=0.5, rely=0.5, anchor="center")


# METODOS FUNCIONALES

"""Metodo formarfecha: formatea entrys para que la entrada solo sea en el formato dd/mm/aaaa"""


def formarfecha(texto):
    """Comprueba que todo lo que se ingrese sean numeros, que el texto no exceda de los 10
    carateres, a la vez que obliga a poner los "/" usados en el formato"""
    if len(texto) > 10:
        return False
    fecha = []
    for i, char in enumerate(texto):
        if i in (2, 5):
            fecha.append(char == "/")
        else:
            fecha.append(char.isdecimal())
    return all(fecha)


"""Metodo limitarCaracteres: limita la cantidad de caracteres que puede recibir un entry"""


def limitarCaracteres(caracter, texto, digitos: int):
    if int(len(texto)) > int(digitos):
        return False
    return caracter.isdecimal()


"""Metodo buscador: crea el buscador que se utiliza en la mayoria las paginas de procesos"""


def buscador():
    """Metodo encargado de buscar cliente y capturarlo en la variable con el mismo nombre
    para realizar los procesos que se deseen hacer y necesiten un cliente, a la vez que
    muestra los datos de este cliente en varios entry"""

    def Rellenar(Docu):
        global cliente
        cliente = Almacenamiento.buscarUsuario(Docu)
        Nom.config(state="normal")
        Tel.config(state="normal")
        Cub.config(state="normal")
        Doc.delete(0, END)
        Nom.delete(0, END)
        Tel.delete(0, END)
        Cub.delete(0, END)
        if cliente != None:
            Doc.insert(0, cliente.getIdentificacion())
            Nom.insert(0, cliente.getNombre())
            Tel.insert(0, cliente.getTelefono())
            Cub.insert(0, cliente.get_cuenta_bancaria())
        else:
            messagebox.showerror(
                "Usuario no encontrado",
                "Este usuario no está registrado en la base de datos",
            )
        Nom.config(state="disabled")
        Tel.config(state="disabled")
        Cub.config(state="disabled")
        return cliente

    """Crear todo lo que vemos en el formulario de busqueda y posicionarlo en el frame"""
    Documento = Label(frame2, text="No. Documento", font=("Arial", 10), anchor="w")
    Documento.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.05)
    Nombre = Label(frame2, text="Nombre", font=("Arial", 10), anchor="w")
    Nombre.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.48)
    Telefono = Label(frame2, text="Telefono", font=("Arial", 10), anchor="w")
    Telefono.place(relheight=0.05, relwidth=0.15, rely=0.15, relx=0.05)
    CuentaBancaria = Label(
        frame2, text="Cuenta Bancaria", font=("Arial", 10), anchor="w"
    )
    CuentaBancaria.place(relheight=0.05, relwidth=0.15, rely=0.15, relx=0.48)

    Doc = Entry(frame2)
    Doc.place(relheight=0.05, relwidth=0.15, rely=0.05, relx=0.2)

    Buscar = Button(
        frame2, text="Buscar", font=("Arial", 10), command=lambda: Rellenar(Doc.get())
    )
    Buscar.place(relheight=0.05, relwidth=0.1, rely=0.05, relx=0.35)

    Nom = Entry(frame2)
    Nom.place(relheight=0.05, relwidth=0.25, rely=0.05, relx=0.65)
    Tel = Entry(frame2)
    Tel.place(relheight=0.05, relwidth=0.25, rely=0.15, relx=0.2)
    Cub = Entry(frame2)
    Cub.place(relheight=0.05, relwidth=0.25, rely=0.15, relx=0.65)


"""Metodo Registro: reinicia el frame2 con el metodo reiniciar, luego forma el formulario
   necesario para crear un nuevo cliente y se dispara a la hora de seleccionar la opcion "registro"
   de "consultas y procesos" """


def Registro():
    """Método registrarUsuarios: se encarga de hacer una comprobacion para verificar que el
    usuario que se desea registrar, no esté en la base de datos, en caso de ser encontrado
    se cancela el registro, en caso de que no, procede a registrarlo"""

    def registrarUsuario(nombre, id, telefono, cuentaBan):
        cliente = Almacenamiento.buscarUsuario(id)
        if cliente != None:
            messagebox.showerror(
                "Usuario ya registrado",
                "Este usuario ya se encuentra registrado en la base de datos del hotel",
            )
        else:
            Almacenamiento.crearUsuario(nombre, id, telefono, cuentaBan)
            messagebox.showinfo(
                "Usuario Registrado con Exito",
                "Usuario Registrado con Exito.\n\nIdentificacion:\t"
                + id
                + "\n\nNombre:\t"
                + nombre
                + "\n\nTelefono:\t"
                + telefono
                + "\n\nCuenta Bancaria:\t"
                + cuentaBan
                + "\n\nBienvenido",
            )
        Doc.delete(0, END)
        Nom.delete(0, END)
        Tel.delete(0, END)
        Cub.delete(0, END)

    """Reinicia el frame 2 usando "reiniciar" y quita la pantalla de inicio"""
    reiniciar()
    frame3.place_forget()

    """Se posiciona el titulo y la descripcion de este proceso en especifico """
    Titulo.config(text="Registro de nuevos usuarios")
    Descripcion.config(
        text="Realiza el registro del nuevo cliente. Por favor complete los siguentes datos"
    )

    """Se forma todo el formulario de registro y se posiciona"""
    Documento = Label(frame2, text="No. Documento", font=("Arial", 13))
    Documento.place(relheight=0.125, relwidth=0.2, rely=0.10, relx=0.2)
    Nombre = Label(frame2, text="Nombre", font=("Arial", 13))
    Nombre.place(relheight=0.125, relwidth=0.2, rely=0.25, relx=0.2)
    Telefono = Label(frame2, text="Telefono", font=("Arial", 13))
    Telefono.place(relheight=0.125, relwidth=0.2, rely=0.40, relx=0.2)
    CuentaBancaria = Label(frame2, text="Cuenta Bancaria", font=("Arial", 13))
    CuentaBancaria.place(relheight=0.125, relwidth=0.2, rely=0.55, relx=0.2)

    Doc = Entry(frame2)
    Doc.place(relheight=0.0625, relwidth=0.3, rely=0.13, relx=0.45)
    Nom = Entry(frame2)
    Nom.place(relheight=0.0625, relwidth=0.3, rely=0.28, relx=0.45)
    Tel = Entry(frame2)
    Tel.place(relheight=0.0625, relwidth=0.3, rely=0.43, relx=0.45)
    Cub = Entry(frame2)
    Cub.place(relheight=0.0625, relwidth=0.3, rely=0.58, relx=0.45)

    """Se crea y se posiciona el boton aceptar encargado de disparar el metodo 
       de registrarUsuarios"""
    Aceptar = Button(
        frame2,
        text="Aceptar",
        font=("Arial", 14),
        relief=RAISED,
        command=lambda: registrarUsuario(Nom.get(), Doc.get(), Tel.get(), Cub.get()),
    )
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)


"""Metodo Alojamiento: reinicia el frame2 con el metodo reiniciar, luego forma el formulario
   necesario para realizar una nueva reserva de alojamiento
   y se dispara a la hora de seleccionar la opcion "Reservar Alojamiento"
   de "consultas y procesos" """


def Alojamiento():
    listahabitaciones = []

    """Metodo seleccionar: Envia la habitacion seleccionada con su boton a la lista
       listahabitaciones, para luego usarla como parametro para crear una nueva reserva
       a la vez que la pone en la lista al lado izquierdo donde veremos cuales se han reservado"""

    def seleccionar(num):
        txt.config(state="normal")
        for i in Almacenamiento.listaHabitaciones:
            if num == i.getNumero():
                if i not in listahabitaciones:
                    listahabitaciones.append(i)
                    txt.insert(END, "\nHabitacion:" + str(i.getNumero()))
                    txt.config(state="disabled")
                    break

    """Metodo verificar: Se encarga de verificar que no haya errores en las fechas
    en caso de no haberlas presenta los botones de las habitaciones disponbles"""

    def verificar():
        try:
            if cliente != None:
                global fen
                global fsa
                """Pasa las fechas ingresadas de str a tipo Date"""
                try:
                    fen = datetime.strptime(fechaEntrada.get(), "%d/%m/%Y")
                    fsa = datetime.strptime(fechaSalida.get(), "%d/%m/%Y")
                except ValueError:
                    """En caso de que no se pueda, responde con la invalidacion de las fechas
                    y reinicia los campos"""
                    messagebox.showerror(
                        "Error", "Las fechas ingresadas no son validas"
                    )
                    fechaEntrada.delete(0, END)
                    fechaSalida.delete(0, END)
                    personas.delete(0, END)
                actual = datetime.now()
                cantidad = int(personas.get())
                """Comprueba que la fecha de salida sea despues de la de entrada y que no sean anteriores
                  a la fecha actual"""
                if fsa < fen or fsa < actual or fen < actual:
                    messagebox.showerror(
                        "Fechas invalidas", "Las fechas ingresadas no son validas"
                    )
                else:
                    ra = Label(
                        frame2,
                        text="Habitaciones Reservadas",
                        font=("Arial", 10),
                        anchor="center",
                    )
                    ra.place(relheight=0.1, relwidth=0.25, rely=0.25, relx=0.7)
                    txt.place(relheight=0.4, rely=0.35, relwidth=0.25, relx=0.7)
                    hadis = []

                    """Busca las habitaciones disponibles para esa fecha, bsucando en las reservas
                       y en una lista que se llama habitaciones disponibles """
                    for reservas in Almacenamiento.listaReservas:
                        if (fen >= reservas.getFechaSalida()) or (
                            fsa <= reservas.getFechaEntrada()
                        ):
                            for habitaciones in reservas.getHabitaciones():
                                if habitaciones not in hadis:
                                    hadis.append(habitaciones)
                    for habis in Almacenamiento.listaHabitacionesDisponibles:
                        if habis not in hadis:
                            hadis.append(habis)

                    """Posiciona los botones de las habitaciones encontradas disponibles para esas fechas"""
                    x = 0.4
                    y = 0.3
                    cont = 0
                    for i in hadis:
                        boton = Button(
                            frame2,
                            text=i.getNombre(),
                            font=("Arial", 14),
                            relief=RAISED,
                            command=functools.partial(seleccionar, i.getNumero()),
                        )
                        boton.place(relheight=0.1, relwidth=0.1, rely=y, relx=x)
                        cont += 1
                        x += 0.15
                        if cont == 2:
                            cont = 0
                            x = 0.4
                            y += 0.15

            else:
                messagebox.showerror("Sin Usuario", "No hay usuario registrado")
        except NameError:
            messagebox.showerror("Sin Usuario", "No hay usuario registrado")

    """Metodo reservar: crea un objeto de la clase reserva, a esta le asocia un objeto de la clase
       factura y en caso de poderse realizar sin problemas la reserva nos muestra la informacion
       de la misma y la factura generada, este método se dispara cuando se da click en el boton 
       "Aceptar" """

    def reservar():
        try:
            reserva = Almacenamiento.crearReserva(
                fen, fsa, listahabitaciones, 0, cliente
            )
            factura = Almacenamiento.crearFactura(
                cliente, emp, listahabitaciones, "Reserva"
            )
            messagebox.showinfo("Reserva realizada con exito", reserva)
            messagebox.showinfo("Factura Asociada", factura)
            "Despues de reservar exitosamente se vuelve a la pantalla de inicio"
            bienvenido()
        except UnboundLocalError:
            messagebox.showinfo(
                "No se ha realizado la reserva", "Usted no ha seleccionado habitaciones"
            )
        for i in listahabitaciones:
            if i in Almacenamiento.listaHabitacionesDisponibles:
                Almacenamiento.listaHabitacionesDisponibles.remove(i)

    """Reinicia el frame 2 usando "reiniciar", posiciona el buscador y quita la pantalla de inicio"""
    reiniciar()
    buscador()
    frame3.place_forget()

    """Se posiciona el titulo y la descripcion de este proceso en especifico """
    Titulo.config(text="Reserva nueva de alojamiento")
    Descripcion.config(text="Realiza una nueva reserva de alojamiento")

    w = Label(
        frame2,
        text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",
    )
    w.place(relheight=0.05, relwidth=1, rely=0.20)

    """Se forma todos los componentes necesarios para realizar una reserva de alojaminento
       y se posicionan"""
    fe = Label(frame2, text="Fecha de entrada", font=("Arial", 10), anchor="w")
    fe.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.02)
    fs = Label(frame2, text="Fecha de salida", font=("Arial", 10), anchor="w")
    fs.place(relheight=0.1, relwidth=0.2, rely=0.45, relx=0.02)
    cp = Label(frame2, text="¿Para cuantas personas?", font=("Arial", 10), anchor="w")
    cp.place(relheight=0.1, relwidth=0.25, rely=0.6, relx=0.02)

    Buscar = Button(frame2, text="Buscar", font=("Arial", 10), command=verificar)
    Buscar.place(relheight=0.1, relwidth=0.2, rely=0.75, relx=0.08)

    fechaEntrada = Entry(
        frame2,
        font=("Arial", 14),
        justify="right",
        validate="key",
        validatecommand=(frame2.register(formarfecha), "%P"),
    )
    fechaEntrada.place(relheight=0.1, relwidth=0.17, rely=0.3, relx=0.18)
    fechaSalida = Entry(
        frame2,
        font=("Arial", 14),
        justify="right",
        validate="key",
        validatecommand=(frame2.register(formarfecha), "%P"),
    )
    fechaSalida.place(relheight=0.1, relwidth=0.17, rely=0.45, relx=0.18)
    personas = Entry(
        frame2,
        font=("Arial", 14),
        justify="center",
        validate="key",
        validatecommand=(frame2.register(limitarCaracteres), "%S", "%P", 2),
    )
    personas.place(relheight=0.1, relwidth=0.05, rely=0.6, relx=0.30)
    txt = Text(frame2, state="disabled")

    adv = Label(
        frame2,
        text="*Ingrese las fechas en formato dd/mm/aaaa",
        font=("Arial", 8),
        anchor="center",
        state="disabled",
    )
    adv.place(relheight=0.1, relwidth=0.35, rely=0.9, relx=0.02)

    """Se crea y se posiciona el boton aceptar encargado de disparar el metodo 
       de reservar"""
    Aceptar = Button(
        frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=reservar
    )
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)


def Tour():
    reiniciar()
    buscador()
    frame3.place_forget()

    Titulo.config(text="Reserva un Tour")
    Descripcion.config(
        text="crearemos una reserva de tour que estará encargada a una empresa externa,\nsolo nos encargaremos de agregar la lista de la reserva de Tour y la factura de costo"
    )

    destinos_seleccionados = []  # Lista para almacenar los destinos seleccionados por el cliente

    def agregarDestino(destino):
        destinos_seleccionados.append(destino)
        print(f"Destino agregado: {destino.get_nombre()}")

    def terminarReserva():
        if destinos_seleccionados:
            # Generar factura y asociarla al cliente
            factura = Almacenamiento.crearFactura(cliente, None, destinos_seleccionados, "Reserva de tour")
            Almacenamiento.listaFacturas.append(factura)
            messagebox.showinfo("Reserva finalizada", "La reserva de tour ha sido completada.")
        else:
            messagebox.showwarning("Reserva incompleta", "No has seleccionado ningún destino.")

    def cargarDestinos():
        for i, destino in enumerate(Destinos):
            if destino != Destinos.COMBO_COMPLETO:
                nombre_label = Label(frame2, text=destino.get_nombre(), font=("Arial", 12))
                nombre_label.grid(row=i+1, column=0, sticky="w")

                valor_label = Label(frame2, text=destino.get_valor(), font=("Arial", 12))
                valor_label.grid(row=i+1, column=1, sticky="w")

                boton = Button(frame2, text="Aceptar", command=lambda destino=destino: agregarDestino(destino))
                boton.grid(row=i+1, column=2)

        # Botón Combo Completo
        boton_combo = Button(frame2, text="COMBO COMPLETO", command=lambda: agregarDestino(Destinos.COMBO_COMPLETO))
        boton_combo.grid(row=len(Destinos), column=2)

        # Botón Terminar
        boton_terminar = Button(frame2, text="Terminar", command=terminarReserva)
        boton_terminar.grid(row=len(Destinos)+1, column=2)

    cargarDestinos()

def Eventos():
    reiniciar()
    buscador()
    frame3.place_forget()

    Titulo.config(text="Reserva nueva de eventos")
    Descripcion.config(
        text="Realiza una nueva reserva de evento en nuestras instalaciones"
    )

    info = Label(frame2, text="Aqui desarrollen su funcionalidad3", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor="center")


def Adicionales():
    reiniciar()
    buscador()
    frame3.place_forget()
    servicios = []

    def reservar():
        factura = Almacenamiento.crearFactura(
            cliente, emp, servicios, "Adicion de servicios"
        )
        mensaje = txt2.get(1.0, END)
        messagebox.showinfo(
            "Adicion realizada con exito", ("Se adicionaron: \n" + mensaje)
        )
        messagebox.showinfo("Factura Asociada", factura)
        "Despues de reservar exitosamente se vuelve a la pantalla de inicio"
        bienvenido()

    def agregar(event):
        txt2.config(state="normal")
        txt2.insert(END, opciones.get() + ":\n")
        txt2.config(state="disabled")
        for i in Almacenamiento.listaServicios:
            if opciones.get() == i.getNombre():
                servicios.append(i)
        txt3.config(state="normal")

    def agregardescripcion(event):
        txt2.config(state="normal")
        texto = txt3.get(1.0, END) + "\n"
        txt2.insert(END, texto)
        txt2.config(state="disabled")
        servicios[-1].setDescripcion(txt3.get(1.0, END))
        txt3.delete(1.0, END)
        txt3.config(state="disabled")

    def buscar():
        try:
            if cliente != None:
                txt.config(state="normal")
                for reservas in Almacenamiento.listaReservas:
                    if cliente == reservas.getCliente():
                        txt.insert(END, reservas)
                        txt.insert(END, "\n----------------------\n")
                txt.config(state="normal")
                txt.place(relheight=0.60, rely=0.35, relwidth=0.3, relx=0.05)
                ra1.place(relheight=0.1, relwidth=0.3, rely=0.25, relx=0.05)
                ra2.place(relheight=0.1, relwidth=0.25, rely=0.25, relx=0.7)
                txt2.place(relheight=0.4, rely=0.35, relwidth=0.25, relx=0.7)
                ra3.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.25)
                ra4.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.47)
                opciones.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.36)
                txt3.place(relheight=0.18, relwidth=0.25, relx=0.4, rely=0.57)
                Buscar.place_forget()
            else:
                messagebox.showerror("Error", "No hay usuario que buscar por else")
        except NameError:
            messagebox.showerror("Error", "No hay usuario que buscar")

    Titulo.config(text="Adicion de servicios")
    Descripcion.config(text="Realiza una adicion de servicios")

    w = Label(
        frame2,
        text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",
    )
    w.place(relheight=0.05, relwidth=1, rely=0.20)

    ra1 = Label(frame2, text="Reservas asociadas", font=("Arial", 10), anchor="center")
    ra3 = Label(
        frame2, text="Servicios disponibles", font=("Arial", 10), anchor="center"
    )
    ra4 = Label(frame2, text="Anotaciones", font=("Arial", 10), anchor="center")
    txt = Text(frame2, state="disabled")
    txt2 = Text(frame2, state="disabled")
    txt3 = Text(frame2, state="disabled")
    txt3.bind("<Return>", agregardescripcion)
    ra2 = Label(frame2, text="Servicios Tomados", font=("Arial", 10), anchor="center")
    opciones = Combobox(
        frame2,
        values=["Alimentacion", "Transporte", "Masaje"],
        textvariable="Servicios",
    )
    opciones.bind("<<ComboboxSelected>>", agregar)

    Buscar = Button(
        frame2, text="Buscar reservas asociadas", font=("Arial", 10), command=buscar
    )
    Buscar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.05)

    Aceptar = Button(
        frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=reservar
    )
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)


def Informacion():
    reiniciar()
    frame3.place_forget()

    Titulo.config(text="Informacion")
    Descripcion.config(text="Consulta la informacion de nuestras instalaciones")

    info = Label(frame2, text="Aqui desarrollen su funcionalidad5", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor="center")


def Cobro():
    reiniciar()
    buscador()
    frame3.place_forget()

    Titulo.config(text="Generador de cobros")
    Descripcion.config(text="Genera el cobro del cliente a la hora de salir")

    info = Label(frame2, text="Aqui desarrollen su funcionalidad6", font=("Arial", 20))
    info.place(relx=0.5, rely=0.5, anchor="center")


def AbrirFuncional():
    #Almacenamiento.Deserializar()
    window.state(newstate="normal")
    ventanaInicio.state(newstate="withdraw")
    


def AbrirInicio():
    ventanaInicio.state(newstate="normal")
    window.state(newstate="withdraw")


def Cerrartodo():
    ventanaInicio.destroy()
    window.destroy()
    Almacenamiento.Serializar()

def cambiarDescripcion():
    Descripcion = Label(
    frameP3,
    text="Este sistema de gestion hotelera se encarga de hacer diferentes \n tipos de reservaciones y el cobro de los servicios ofrecidos por el hotel",
    font=("Arial", 12),
    bg="white",
    )
    Descripcion.place(relx=0.5, rely=0.7, relheight=0.5, relwidth=0.9, anchor="center")

def Carrusel(event):
    global indiceImagen
    listImage

    if indiceImagen == 5:
        indiceImagen = 0

    nextImagen = listImage[indiceImagen]
    botonCarrusel.config(image=nextImagen)
    indiceImagen += 1


def descripciones(event):
    global persona

    if persona == 5:
        persona = 0

    nombre = Nombres[persona]
    descripcion = Descripciones[persona]
    Nombre.config(text=nombre)
    Descripcionactual.config(text=descripcion)
    foto1.config(image=listaFotos1[persona])
    foto2.config(image=listaFotos2[persona])
    foto3.config(image=listaFotos3[persona])
    foto4.config(image=listaFotos4[persona])
    persona += 1


# CREACION DE LA VENTANA DE INICIO
ventanaInicio = Tk()
ventanaInicio.title("Gestor del Hotel UN 2.0")
ventanaInicio.geometry("800x600")
ventanaInicio.protocol("WM_DELETE_WINDOW", Cerrartodo)

menuBar = Menu(ventanaInicio)
ventanaInicio.config(menu=menuBar)

menuInicio = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Inicio", menu=menuInicio)
menuInicio.add_command(label="Descripción", command=cambiarDescripcion)
menuInicio.add_command(label="Salir", command=Cerrartodo)

menuInicio.config(activebackground="sienna1")

ventanaInicio.rowconfigure(0, weight=1)
ventanaInicio.columnconfigure(0, weight=1)

ventanaInicio.columnconfigure(0, weight=1)
ventanaInicio.columnconfigure(1, weight=1)

frame1 = Frame(ventanaInicio, bg="light steel blue", borderwidth=1, relief="solid")
frame1.place(relheight=1, relwidth=0.5, rely=0, relx=0)

frame2 = Frame(ventanaInicio, bg="light steel blue", borderwidth=1, relief="solid")
frame2.place(relheight=1, relwidth=0.5, rely=0, relx=0.5)

frameP3 = Frame(
    frame1, bg="white", height=200, width=200, borderwidth=1, relief="solid"
)
frameP3.pack(side="top", fill="x", padx=3, pady=3)

frameP4 = Frame(
    frame1, bg="white", height=200, width=200, borderwidth=1, relief="solid"
)
frameP4.pack(expand=True, fill="both", padx=3, pady=3)

frameP5 = Frame(
    frame2, bg="white", height=200, width=200, borderwidth=1, relief="solid"
)
frameP5.pack(side="top", fill="x", padx=3, pady=3)

frameP6 = Frame(
    frame2, bg="white", height=200, width=200, borderwidth=1, relief="solid"
)
frameP6.pack(expand=True, fill="both", padx=3, pady=3)

# Zona P6 Fotografias

"""Se suben las fotos de Juan José"""
pathFJJ1 = os.path.join(os.path.dirname(__file__), "img/JJ1.png")
pathFJJ2 = os.path.join(os.path.dirname(__file__), "img/JJ2.png")
pathFJJ3 = os.path.join(os.path.dirname(__file__), "img/JJ3.png")
pathFJJ4 = os.path.join(os.path.dirname(__file__), "img/JJ4.png")
imgFJJ1 = tk.PhotoImage(file=pathFJJ1)
imgFJJ2 = tk.PhotoImage(file=pathFJJ2)
imgFJJ3 = tk.PhotoImage(file=pathFJJ3)
imgFJJ4 = tk.PhotoImage(file=pathFJJ4)

"""Se suben las fotos de Carolina"""
pathC1 = os.path.join(os.path.dirname(__file__), "img/C1.png")
pathC2 = os.path.join(os.path.dirname(__file__), "img/C2.png")
pathC3 = os.path.join(os.path.dirname(__file__), "img/C3.png")
pathC4 = os.path.join(os.path.dirname(__file__), "img/C4.png")
imgC1 = tk.PhotoImage(file=pathC1)
imgC2 = tk.PhotoImage(file=pathC2)
imgC3 = tk.PhotoImage(file=pathC3)
imgC4 = tk.PhotoImage(file=pathC4)

"""Se suben las fotos de Sebastian"""
pathS1 = os.path.join(os.path.dirname(__file__), "img/S1.png")
pathS2 = os.path.join(os.path.dirname(__file__), "img/S2.png")
pathS3 = os.path.join(os.path.dirname(__file__), "img/S3.png")
pathS4 = os.path.join(os.path.dirname(__file__), "img/S4.png")
imgS1 = tk.PhotoImage(file=pathS1)
imgS2 = tk.PhotoImage(file=pathS2)
imgS3 = tk.PhotoImage(file=pathS3)
imgS4 = tk.PhotoImage(file=pathS4)

"""Se suben las fotos de Andres"""
pathA1 = os.path.join(os.path.dirname(__file__), "img/A1.png")
pathA2 = os.path.join(os.path.dirname(__file__), "img/A2.png")
pathA3 = os.path.join(os.path.dirname(__file__), "img/A3.png")
pathA4 = os.path.join(os.path.dirname(__file__), "img/A4.png")
imgA1 = tk.PhotoImage(file=pathA1)
imgA2 = tk.PhotoImage(file=pathA2)
imgA3 = tk.PhotoImage(file=pathA3)
imgA4 = tk.PhotoImage(file=pathA4)

"""Se suben las fotos de Miguel"""
pathM1 = os.path.join(os.path.dirname(__file__), "img/M1.png")
pathM2 = os.path.join(os.path.dirname(__file__), "img/M2.png")
pathM3 = os.path.join(os.path.dirname(__file__), "img/M3.png")
pathM4 = os.path.join(os.path.dirname(__file__), "img/M4.png")
imgM1 = tk.PhotoImage(file=pathM1)
imgM2 = tk.PhotoImage(file=pathM2)
imgM3 = tk.PhotoImage(file=pathM3)
imgM4 = tk.PhotoImage(file=pathM4)

listaFotos1 = [imgFJJ1, imgC1, imgS1, imgA1, imgM1]
listaFotos2 = [imgFJJ2, imgC2, imgS2, imgA2, imgM2]
listaFotos3 = [imgFJJ3, imgC3, imgS3, imgA3, imgM3]
listaFotos4 = [imgFJJ4, imgC4, imgS4, imgA4, imgM4]
foto1 = Label(
    frameP6,
    text="",
    font=("Arial Bold", 20),
    anchor="center",
    bg="white",
    image=imgFJJ1,
)
foto1.place(relheight=0.425, relwidth=0.425, rely=0.05, relx=0.525)
foto2 = Label(
    frameP6,
    text="",
    font=("Arial Bold", 20),
    anchor="center",
    bg="white",
    image=imgFJJ2,
)
foto2.place(relheight=0.425, relwidth=0.425, rely=0.05, relx=0.05)
foto3 = Label(
    frameP6,
    text="",
    font=("Arial Bold", 20),
    anchor="center",
    bg="white",
    image=imgFJJ3,
)
foto3.place(relheight=0.425, relwidth=0.425, rely=0.525, relx=0.05)
foto4 = Label(
    frameP6,
    text="",
    font=("Arial Bold", 20),
    anchor="center",
    bg="white",
    image=imgFJJ4,
)
foto4.place(relheight=0.425, relwidth=0.425, rely=0.525, relx=0.525)


# Zona P5 Autobiografia
persona = 0
Nombres = [
    "Juan José Lotero Florez",
    "Carolina Humanez Urrego",
    "Sebastian Mendoza Gonzalez",
    "Andrés Felipe Arismendi Alzate",
    "Miguel Angel Quiceno Hincapie",
]
Descripciones = [
    "1.Estudiante de ing. en sistemas e informatica en la universidad Nacional",
    "2.Estudiante de ing. en sistemas e informatica en la universidad Nacional",
    "3.Estudiante de ciencias de la computación en la universidad Nacional",
    "4.Estudiante de ing. en sistemas e informatica en la universidad Nacional de dia, de noche dibujante Furro.",
    "5.Estudiante de ciencias de la computacion en la universidad Nacional",
]
Nombre = Label(
    frameP5, text="Juan José Lotero Florez", font=("Arial Bold", 20), anchor="w"
)
Nombre.place(relheight=0.5, relwidth=1, rely=0, relx=0)
Descripcionactual = Label(
    frameP5,
    wraplength=400,
    text="1.Estudiante de ing. en sistemas e informatica en la universidad Nacional",
    font=("Arial", 12),
    anchor="nw",
    
)
Descripcionactual.place(relheight=0.5, relwidth=1, rely=0.5, relx=0)
Nombre.bind("<Button-1>", descripciones)
Descripcionactual.bind("<Button-1>", descripciones)

# Zona P3 Bienvenidad
Bienvenida = Label(
    frameP3,
    text="¡Bienevenido! \n Este es el nuevo sistema\n de gestion del Hotel UN 2.0",
    font=("Arial", 12, "bold"),
    bg="white",
)
Bienvenida.place(relx=0.5, rely=0.3, relheight=0.5, relwidth=0.7, anchor="center")



# Zona P4 Carrusel de imagnes y Boton de incio
pathImgHotel = os.path.join(os.path.dirname(__file__), "img/hotel.png")
pathImgPiscina = os.path.join(os.path.dirname(__file__), "img/piscina.png")
pathImgDestino1 = os.path.join(os.path.dirname(__file__), "img/destino1.png")
pathImgDestino2 = os.path.join(os.path.dirname(__file__), "img/destino2.png")
pathImgDef = os.path.join(os.path.dirname(__file__), "img/def.png")

imgHotel = tk.PhotoImage(file=pathImgHotel)
imgPiscina = tk.PhotoImage(file=pathImgPiscina)
imgDestino1 = tk.PhotoImage(file=pathImgDestino1)
imgDestino2 = tk.PhotoImage(file=pathImgDestino2)
imgDef = tk.PhotoImage(file=pathImgDef)

listImage = [imgDef, imgHotel, imgPiscina, imgDestino1, imgDestino2]
indiceImagen = 0

botonCarrusel = Button(
    frameP4, image=imgDef, command=lambda: [AbrirFuncional(), bienvenido()]
)
botonCarrusel.pack(expand=True)
botonCarrusel.bind("<Enter>", Carrusel)


# CREACION DE LA VENTANA FUNCIONAL
window = Tk()
window.title("Gestion del Hotel UN 2.0")
window.geometry("700x500")
window.state(newstate="withdraw")
window.protocol("WM_DELETE_WINDOW", Cerrartodo)

menuBar = Menu(window)
window.config(menu=menuBar)

menuArchivo = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=menuArchivo)
menuArchivo.add_command(label="Aplicación", command=Aplicacion)
menuArchivo.add_command(label="Salir", command=AbrirInicio)

menuProcesos = Menu(menuBar, tearoff=0)
menuBar.add_cascade(
    label="Procesos y Consultas",
    menu=menuProcesos,
)
menuProcesos.add_command(label="Registrar Usuario", command=Registro)
menuProcesos.add_command(label="Reservar Alojamiento", command=Alojamiento)
menuProcesos.add_command(label="Reservar Tour", command=Tour)
menuProcesos.add_command(label="Reservar evento", command=Eventos)
menuProcesos.add_command(label="Servicios Adicionales", command=Adicionales)
menuProcesos.add_command(label="Informacion", command=Informacion)
menuProcesos.add_command(label="Generar Cobro", command=Cobro)

menuAyuda = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Ayuda", menu=menuAyuda)

menuAyuda.add_command(label="Acerca de...", command=Acercade)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

frame1 = Frame(window, borderwidth=1, relief="solid")

Titulo = Label(frame1, text="", font=("Arial Bold", 20))
Titulo.place(relx=0.5, rely=0.35, anchor="center")
Descripcion = Label(frame1, text="", font=("Arial", 12))
Descripcion.place(relx=0.5, rely=0.7, anchor="center")

frame2 = Frame(window, borderwidth=1, relief="solid")
frame3 = Frame(window, borderwidth=1, relief="solid")

frame1.place(relheight=0.2, relwidth=1, rely=0)
frame2.place(relheight=0.8, relwidth=1, rely=0.2)


# OBJETOS TEMPORALES PARA PRUEBAS
habitacion1 = Almacenamiento.crearHabitacion("101", "Habitacion Individual", 101, 1)
habitacion2 = Almacenamiento.crearHabitacion("102", "Habitacion Individual", 102, 1)
habitacion3 = Almacenamiento.crearHabitacion("201", "Habitacion Doble", 201, 2)
habitacion4 = Almacenamiento.crearHabitacion("202", "Habitacion Doble", 202, 2)
habitacion5 = Almacenamiento.crearHabitacion("301", "Habitacion Familiar", 301, 4)
habitacion6 = Almacenamiento.crearHabitacion("302", "Habitacion Familiar", 302, 4)

c1 = Usuario("Carlos", "1", "Cliente", "1", "1")
Almacenamiento.listaUsuarios.append(c1)
emp = Empleado("Recepcion", 0, 0, "Recepcion")
Almacenamiento.listaEmpleados.append(emp)
comida = Almacenamiento.crearServicio("Alimentacion", 50000, "")
masaje = Almacenamiento.crearServicio("Masaje", 30000, "")
transporte = Almacenamiento.crearServicio("Transporte", 70000, "")
fechaEntrada = "20/03/2023"
fechaSalida = "30/05/2023"
fen = datetime.strptime(fechaEntrada, "%d/%m/%Y")
fsa = datetime.strptime(fechaSalida, "%d/%m/%Y")
ba = []
ba.append(Almacenamiento.listaHabitaciones[0])

res1 = Reserva(fen, fsa, ba, 0, c1)
res2 = Reserva(fen, fsa, ba, 0, c1)
res3 = Reserva(fen, fsa, ba, 0, c1)
Almacenamiento.listaReservas.append(res1)
Almacenamiento.listaReservas.append(res2)
Almacenamiento.listaReservas.append(res3)

(Almacenamiento.listaHabitaciones)
(Almacenamiento.listaUsuarios)
(Almacenamiento.listaServicios)
(Almacenamiento.listaReservas)
(res1.getCliente())
(res2.getCliente())
(res3.getCliente())

ventanaInicio.mainloop()
window.mainloop()

import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import os
import sys
from tkinter.ttk import Combobox

sys.path.append(os.path.dirname(__file__) + "/../baseDatos")
sys.path.append(os.path.dirname(__file__)+ "/../uiMain/Exepciones")

from Almacenamiento import *
from datetime import datetime
import functools
from ExepcionC1 import ExepcionC1
from UsuarioNoEncontradoError import UsuarioNoEncontradoError
cliente=None

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
    global cliente
    cliente=None


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
    global cliente
    cliente=None


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

"""Metodo limitarCaracteres: limita a solo numeros los caracteres que puede recibir un entry"""
def solonumeros(numero):
    return numero.isdecimal()

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
        try:
            Docu=int(Docu)
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
                reg=messagebox.askyesno("Usuario no encontrado","¿Desea registrarlo?")
                if reg:
                    Registro()
            Nom.config(state="disabled")
            Tel.config(state="disabled")
            Cub.config(state="disabled")
            return cliente
        except ValueError:
            reg=messagebox.askyesno("Usuario no encontrado","¿Desea registrarlo?")
            if reg:
                Registro()

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
        print("si entro")
        print(num)
        txt.config(state="normal")
        print(Almacenamiento.listaHabitaciones)
        for i in Almacenamiento.listaHabitaciones:
            print("si entro")
            if num == i.getNumero():
                print("si entro")
                if i not in listahabitaciones:
                    listahabitaciones.append(i)
                    txt.insert(END, "\nHabitacion:" + str(i.getNumero()))
                    txt.config(state="disabled")
                    print(listahabitaciones)
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
                cliente, Almacenamiento.listaEmpleados[0], listahabitaciones, "Reserva"
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

    fechaEntrada = Entry(frame2,font=("Arial", 14),justify="right",validate="key",validatecommand=(frame2.register(formarfecha), "%P"),)
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
        if cliente!=None:
            destinos_seleccionados.append(destino)
            actualizarRecuadro()
        else:
            messagebox.showerror("Sin cliente","No existe un cliente asignado")

    def calcularValorTotal():
        valor_total = sum(destino.getValor() for destino in destinos_seleccionados)
        return valor_total

    def terminarReserva():
        try:
            if len(destinos_seleccionados) > 10:
                raise ValueError("Error: Has seleccionado más de 10 destinos.", bienvenido())

            if destinos_seleccionados:
                # Crear una lista de objetos Tour a partir de los destinos seleccionados
                # Generar factura y asociarla al cliente
                valor_total = calcularValorTotal()
                factura = Almacenamiento.crearFactura(cliente, Almacenamiento.listaEmpleados[0], destinos_seleccionados, "Tour") 
                mostrardestinos = ""

                for destino in destinos_seleccionados:
                    mostrardestinos += (destino.getNombre() + "\n")
                messagebox.showinfo("Reserva realizada con éxito", "Se realizó la reserva de Tour a nombre de: " + cliente.getNombre() + "\nA los destinos:\n" + mostrardestinos)
                messagebox.showinfo("Factura Asociada", factura)
                bienvenido()

            else:

                raise ValueError("Reserva incompleta: No has seleccionado ningún destino.")

        except Exception as ve:

            messagebox.showerror("Error en la reserva", str(ve))
        except Exception as e:

            messagebox.showerror("Error en la reserva", "Ocurrió un error al procesar la reserva: " + str(e))


    def actualizarRecuadro():
        listbox_destinos.delete(0, END)
        for destino in destinos_seleccionados:
            listbox_destinos.insert(END, destino.getNombre())
        actualizarValorTotal()

    def actualizarValorTotal():
        valor_total = calcularValorTotal()
        label_valor_total.config(text=f"Valor Total: {valor_total}")


    def cargarDestinos():
        nombre_label_1 = Label(frame2, text=Destinos.SANTA_FE_DE_ANTIOQUIA.getNombre(), font=("Arial", 12))
        nombre_label_1.place(relx=0.1, rely=0.27, anchor="center")

        valor_label_1 = Label(frame2, text=Destinos.SANTA_FE_DE_ANTIOQUIA.getValor(), font=("Arial", 12))
        valor_label_1.place(relx=0.3, rely=0.27, anchor="center")

        boton_1 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.SANTA_FE_DE_ANTIOQUIA))
        boton_1.place(relx=0.5, rely=0.27, anchor="center")


        nombre_label_2 = Label(frame2, text=Destinos.COMUNA_13.getNombre(), font=("Arial", 12))
        nombre_label_2.place(relx=0.1, rely=0.37, anchor="center")

        valor_label_2 = Label(frame2, text=Destinos.COMUNA_13.getValor(), font=("Arial", 12))
        valor_label_2.place(relx=0.3, rely=0.37, anchor="center")

        boton_2 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.COMUNA_13))
        boton_2.place(relx=0.5, rely=0.37, anchor="center")


        nombre_label_3 = Label(frame2, text=Destinos.JARDIN.getNombre(), font=("Arial", 12))
        nombre_label_3.place(relx=0.1, rely=0.47, anchor="center")

        valor_label_3 = Label(frame2, text=Destinos.JARDIN.getValor(), font=("Arial", 12))
        valor_label_3.place(relx=0.3, rely=0.47, anchor="center")

        boton_3 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.JARDIN))
        boton_3.place(relx=0.5, rely=0.47, anchor="center")

        nombre_label_4 = Label(frame2, text=Destinos.PARQUE_ARVI.getNombre(), font=("Arial", 12))
        nombre_label_4.place(relx=0.1, rely=0.57, anchor="center")

        valor_label_4 = Label(frame2, text=Destinos.PARQUE_ARVI.getValor(), font=("Arial", 12))
        valor_label_4.place(relx=0.3, rely=0.57, anchor="center")

        boton_4 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.PARQUE_ARVI))
        boton_4.place(relx=0.5, rely=0.57, anchor="center")

        nombre_label_5 = Label(frame2, text=Destinos.SANTA_ELENA.getNombre(), font=("Arial", 12))
        nombre_label_5.place(relx=0.1, rely=0.67, anchor="center")

        valor_label_5 = Label(frame2, text=Destinos.SANTA_ELENA.getValor(), font=("Arial", 12))
        valor_label_5.place(relx=0.3, rely=0.67, anchor="center")

        boton_5 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.SANTA_ELENA))
        boton_5.place(relx=0.5, rely=0.67, anchor="center")

        nombre_label_6 = Label(frame2, text=Destinos.PEÑOL_GUADELOUPE.getNombre(), font=("Arial", 12))
        nombre_label_6.place(relx=0.1, rely=0.77, anchor="center")


        valor_label_6 = Label(frame2, text=Destinos.PEÑOL_GUADELOUPE.getValor(), font=("Arial", 12))
        valor_label_6.place(relx=0.3, rely=0.77, anchor="center")

        boton_6 = Button(frame2, text="Aceptar", command=lambda: agregarDestino(Destinos.PEÑOL_GUADELOUPE))
        boton_6.place(relx=0.5, rely=0.77, anchor="center")

        valor_label_7 = Label(frame2, text=Destinos.COMBO_COMPLETO.getValor(), font=("Arial", 12))
        valor_label_7.place(relx=0.1, rely=0.87, anchor="center")


        boton_combo = Button(frame2, text="COMBO COMPLETO", command=lambda: agregarDestino(Destinos.COMBO_COMPLETO))
        boton_combo.place(relx=0.3, rely=0.87, anchor="center")

        Aceptar = Button(frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=terminarReserva)
        Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)
        
    
    listbox_destinos = Listbox(frame2, width=25, height=10)
    listbox_destinos.place(relx=0.8, rely=0.5, anchor="center")

    label_valor_total = Label(frame2, text="Valor Total: 0", font=("Arial", 12))
    label_valor_total.place(relx=0.8, rely=0.7, anchor="center")

    cargarDestinos()

def Eventos():
    reiniciar()
    buscador()
    frame3.place_forget()
        
        
        
    def solicitarEmpleados():
        
        new = Toplevel(frame2)
        new.geometry("400x330")
        new.title("Solicitar Empleados")
        
        empleados = dict( zip(["Meseros", "Cocineros", "Bartenders"], [0,0,0]) )
        
        Label(new, text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 10)).place(relheight=0.05, relwidth=1, rely=0.01)
        titulo = Label(new, text="Solicitar Empleados", font=("Arial Bold", 10), anchor="w")
        titulo.place(relheight=0.05, relwidth=0.5, rely=0.07, relx=0.3)
        
        subtitulo = Label(new, text="Elija los empleados", font=("Arial",8), anchor="w")
        subtitulo.place(relheight=0.05, relwidth=0.5, rely=0.12, relx=0.34)
        Label(new, text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 10)).place(relheight=0.05, relwidth=1, rely=0.20)
        
        lblServiciosExt = Label(new, text="¿Qué empleados necesita?", font=("Arial", 9), anchor="w")
        lblServiciosExt.place(relheight=0.1, relwidth=1, rely=0.28, relx=0.02)
        
        
        a0 = Label(new, text="Cocineros: ", font=("Arial", 9), anchor="w")
        a0.value = 0
        a0.place(relheight=0.1, relwidth=0.5, rely=0.45, relx=0.02)
        
        a1 = Label(new, text="Meseros: ", font=("Arial", 9), anchor="w")
        a1.value = 0
        a1.place(relheight=0.1, relwidth=0.5, rely=0.55, relx=0.02)
        
        a2 = Label(new, text="Bartenders: ", font=("Arial", 9), anchor="w")
        a2.value = 0
        a2.place(relheight=0.1, relwidth=0.5, rely=0.65, relx=0.02)
        
        b0 = Combobox(new, values=[0,1,2,3,4], state="readonly")
        b0.place(relheight=0.08, relwidth=0.1, rely=0.45, relx=0.2)
        
        b1 = Combobox(new, values=[0,1,2,3,4], state="readonly")
        b1.place(relheight=0.08, relwidth=0.1, rely=0.55, relx=0.2)
        
        b2 = Combobox(new, values=[0,1,2,3], state="readonly")
        b2.place(relheight=0.08, relwidth=0.1, rely=0.65, relx=0.2)
        
        aceptar = Button(new, text="Aceptar", command = lambda: terminar())
        aceptar.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.7)
        
        def terminar():
            empleados["Cocineros"] = b0.get()
            empleados["Meseros"] = b1.get()
            empleados["Bartenders"] = b2.get()
            new.destroy()
            
        return empleados
    
    def solicitarServiciosExternos():
        
        serviciosExt = dict(zip(["Sonido","Entretenimiento","DJ"],[False,False,False]))
        
        new = Toplevel(frame2)
        new.geometry("400x400")
        new.title("Solicitar Servicios Externos")
        
        Label(new, text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 10)).place(relheight=0.05, relwidth=1, rely=0.001)
        titulo = Label(new, text="Servicios Externos", font=("Arial Bold", 10), anchor="w")
        titulo.place(relheight=0.1, relwidth=0.5, rely=0.07, relx=0.3)
        
        subtitulo = Label(new, text="Elija los Servicios externos", font=("Arial",8), anchor="w")
        subtitulo.place(relheight=0.1, relwidth=0.5, rely=0.14, relx=0.3)
        
        Label(new, text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 10)).place(relheight=0.05, relwidth=1, rely=0.20)
        
        lblServiciosExt = Label(new, text="¿Qué servicios externos desea?", font=("Arial", 8), anchor="w")
        lblServiciosExt.place(relheight=0.1, relwidth=1, rely=0.28, relx=0.02)
      
        frameEleccion = Frame(new)
        frameEleccion.place(relheight=0.08, relwidth=0.7, rely=0.35, relx=0.02)
        
        vars = [False]*3
        
        cb1 = Checkbutton(frameEleccion, text='Sonido', anchor="w", command= lambda: f0() )
        cb1.pack(side="left")
        
        cb2 = Checkbutton(frameEleccion, text='Entretenimiento', anchor="w", command= lambda: f1() )
        cb2.pack(side="left")
        
        cb3 = Checkbutton(frameEleccion, text='DJ', anchor="w", command= lambda: f2() )
        cb3.pack(side="left")
        
        txtDisplay = Text(new)
        txtDisplay.config(state="disabled")
        txtDisplay.place(relheight=0.3, relwidth=0.8, rely=0.5, relx=0.02)
        
        def f0():
            vars[0] = not(vars[0])
            actualizarDisplay()
            
        def f1():
            vars[1] = not(vars[1])
            actualizarDisplay()
        
        def f2():
            vars[2] = not(vars[2])
            actualizarDisplay()
            
            
        def actualizarDisplay():
            valor = dict(zip( [True,False],["Sí","No"] ))
            s = "Los servicios contratados son:\n"
            s += "Sonido: " + valor[vars[0]] + "\n"
            s += "Entretenimiento: " + valor[vars[1]] + "\n"
            s += "DJ: " + valor[vars[2]] + "\n"
            
            txtDisplay.config(state="normal")
            txtDisplay.delete("1.0", END)   
            txtDisplay.insert(END, s)
            txtDisplay.config(state="disabled")
            
          
        aceptar = Button(new, text="Aceptar", font=("Arial", 10), command= lambda: terminar())
        aceptar.place(relheight=0.1, relwidth=0.2, rely=0.85, relx=0.7)
        
        def terminar():
            serviciosExt["Sonido"] = vars[0]
            serviciosExt["Entretenimiento"] = vars[1]
            serviciosExt["DJ"] = vars[2]
            new.destroy()
        
        return serviciosExt
    
    
    Titulo.config(text="Reserva nueva de eventos")
    Descripcion.config(
        text="Realiza una nueva reserva de evento en nuestras instalaciones"
    )

    w = Label(
        frame2,
        text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",
    )
    w.place(relheight=0.05, relwidth=1, rely=0.20)
    
    # Se pregunta por la Fecha de realización del evento
    lblFecha = Label(frame2, text="Fecha Evento", font=("Arial", 10), anchor="w")
    lblFecha.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.02)
    
    fechaEvento = Entry(
        frame2,
        font=("Arial", 14),
        justify="right",
        validate="key",
        validatecommand=(frame2.register(formarfecha), "%P"),
    )
    fechaEvento.place(relheight=0.1, relwidth=0.17, rely=0.3, relx=0.2)    
    
    #Se pregunta por duración del evento
    lblDuracion = Label(frame2, text="Duración Evento", font=("Arial", 10), anchor="w")
    lblDuracion.place(relheight = 0.1, relwidth = 0.2, rely = 0.5, relx = 0.02)
    
    
    desicionDuracion = Combobox(
        frame2,
        values=["4 Horas", "6 Horas", "8 Horas"],
        textvariable="Duración en horas",
    )
    desicionDuracion.place(relheight=0.1, relwidth=0.17, rely=0.5, relx=0.2)
    
    #Se pregunta por el número de personas que asistirán al evento
    
    lblAsistentes = Label(frame2, text="Número de asistentes", font=("Arial", 10), anchor="w")
    lblAsistentes.place(relheight = 0.1, relwidth = 0.17, rely = 0.7, relx = 0.02)
    
    entryAsistentes = Entry(
        frame2,
        font=("Arial", 14),
        justify="right"
    )
    entryAsistentes.place(relheight=0.1, relwidth=0.17, rely=0.7, relx=0.2)
    
    
    #Se pregunta por el lugar de realización del evento
    lblLugar = Label(frame2, text="Lugar Evento", font=("Arial", 10), anchor="w")
    lblLugar.place(relheight = 0.1, relwidth = 0.2, rely = 0.3, relx = 0.4)
    
    desicionLugar = Combobox(
        frame2,
        values=["Terraza", "Salón de Eventos", "Piscina"],
        textvariable="Lugar del evento"
    )
    desicionLugar.place(relheight=0.1, relwidth=0.17, rely=0.3, relx=0.55)
    
    #Botón para añadir servicios externos
    
    serviciosExt = Button(frame2, text="Servicios Externos",font=("Arial", 10), command=solicitarServiciosExternos)
    serviciosExt.place(relheight=0.1, relwidth=0.18, rely=0.87, relx=0.02)
    #Botón para añadir empleados
    
    empleados = Button(frame2, text="Empleados",font=("Arial", 10), command=solicitarEmpleados)
    empleados.place(relheight=0.1, relwidth=0.18, rely=0.87, relx=0.22)
    
    aceptar = Button(frame2, text="Aceptar", font=("Arial Bold", 11), command= lambda: terminarEvento())
    aceptar.place(relheight=0.11, relwidth=0.18, rely=0.87, relx=0.47)
    
    def terminarEvento():
        fecha = fechaEvento.get()
        duracion = desicionDuracion.get()
        lugar = desicionLugar.get()
        asistentes = entryAsistentes.get()
        if fecha == "" or duracion == "" or lugar == "" or asistentes == "":
            messagebox.showerror("Error", "Por favor llene todos los campos")
        else:
            if messagebox.askyesno("Confirmación", "¿Desea confirmar la reserva?"):
                messagebox.showinfo("Confirmación", "Reserva realizada con éxito")
                bienvenido()
            else:
                messagebox.showinfo("Confirmación", "Reserva cancelada")
                bienvenido()



def Adicionales():
    reiniciar()
    buscador()
    frame3.place_forget()
    servicios = []

    def reservar():
        factura = Almacenamiento.crearFactura(cliente, Almacenamiento.listaEmpleados[0], servicios, "Adicion de servicios")
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

    #Pa buscar reservas asociadas al cliente
    def buscar():
        try:
            if cliente != None:
                txt.config(state="normal")
                for reservas in Almacenamiento.listaReservas:
                    if cliente.getIdentificacion() == reservas.getCliente().getIdentificacion():
                        txt.insert(END, reservas)
                        txt.insert(END, "\n----------------------\n")
                txt.config(state="disabled")
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

    w = Label(frame2,text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",)
    w.place(relheight=0.05, relwidth=1, rely=0.20)

    ra1 = Label(frame2, text="Reservas asociadas", font=("Arial", 10), anchor="center")
    ra3 = Label(frame2, text="Servicios disponibles", font=("Arial", 10), anchor="center")
    ra4 = Label(frame2, text="Anotaciones", font=("Arial", 10), anchor="center")
    txt = Text(frame2, state="disabled")
    txt2 = Text(frame2, state="disabled")
    txt3 = Text(frame2, state="disabled")
    txt3.bind("<Return>", agregardescripcion)
    ra2 = Label(frame2, text="Servicios Tomados", font=("Arial", 10), anchor="center")
    opciones = Combobox(frame2,values=["Alimentacion", "Transporte", "Masaje"],textvariable="Servicios",)
    opciones.bind("<<ComboboxSelected>>", agregar)

    Buscar = Button(frame2, text="Buscar reservas asociadas", font=("Arial", 10), command=buscar)
    Buscar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)

    Aceptar = Button(frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=reservar)
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)


def Informacion():
    reiniciar()
    frame3.place_forget()

    Titulo.config(text="Informacion de habitaciones")
    Descripcion.config(text="Consulta la Sobre las diferentes habitaciones")

    forma = Label(frame2, text="Informacion de habitaciones", font=("Arial", 10))
    forma.place(relheight=0.1, relwidth=0.3, relx=0.1, rely=0.2, anchor="w")
    
    
    """GLabel_581=tk.Label(frame2)
    ft = tkFont.Font(family='Arial',size=5)
    GLabel_581["font"] = ft
   # GLabel_581["fg"] = "#333333"
    GLabel_581["justify"] = "center"
    GLabel_581["text"] = "Organizar por tipo de busqueda"
    GLabel_581.place(relx=0.2,rely=0.3)"""
    
    
    var1 = IntVar()
    
    def seleccion():
        #print(var1.get())
        if var1.get()==1:
            var1.set(0) 
        else:
            var1.set(1) 
        return
    
    
    def infoprint(event):
        
        caja.config(state = "normal")
        #print(seleccion())
        caja.delete("1.0", END) 
        
        if var1.get()==1:
            caja.insert(END, "Informacion de habitaciones y clientes asociados\n")
            
            hab = []
            for i in Almacenamiento.listaHabitaciones:
                caja.insert(END, "________________________________________________\n")
                caja.insert(END, "Habitacion numero: " + str(i.getNumero()) + "\n" + "Capacidad: " + str(i.getCapacidad()))
                caja.insert(END, "\n")
            #var1.set(0) 
        else:
            caja.insert(END, "Informacion de habitaciones\n")
            
            hab = []
            for i in Almacenamiento.listaHabitaciones:
                caja.insert(END, "________________________________________________\n")
                caja.insert(END, "Habitacion numero: " + str(i.getNumero()) + "\n" + "Capacidad: " + str(i.getCapacidad()))
                caja.insert(END, "\n")
            #var1.set(1) 
            
        caja.config(state = "disabled")
        
        
    
    
    cb1 = Checkbutton(frame2, text = "Informacion con clientes", anchor = "w", font = ("Arial", 10), variable = var1, command  = lambda: seleccion())
    cb1.place(relx = 0.1, rely = 0.4)
    
    
    """def cambio(event):
        cliente = not(cliente)
        return None"""
    #b1.bind("<Button-1>", cambio)
    
    
    b = Button(frame2, text = "Mostrar", font = ("Arial", 10), anchor = "center")
    b.place(relx = 0.1, rely = 0.46, relheight = 0.12, relwidth = 0.16)
    
    caja = Text(frame2, state = "disabled")
    caja.place(relheight=0.6, relwidth=0.5, relx=0.45,rely=0.19)
    
    #caja.insert("Informacion de habitaciones")
    b.bind("<Button-1>", infoprint)
    

    



valor=0
def Cobro():
    reiniciar()
    buscador()
    frame3.place_forget()
    facturasencontradas=[]
    combofacturas=[]
    facturaseleccionadas=[]


    Titulo.config(text="Generador de cobros")
    Descripcion.config(text="Genera el cobro del cliente a la hora de salir")

    def cobrar():
        valorTotal=valor
        ValorPagado=int(txt4.get())
        texto="Facturas pendientes:\n"
        if valorTotal>ValorPagado:
            messagebox.showerror("Falta dinero","El valor pagado es inferior a el valor total")
        else:
            for factura in facturaseleccionadas:
                Almacenamiento.listaFacturas.remove(factura)
            for factura in Almacenamiento.listaFacturas:
                if cliente==factura.getUsuario():
                    texto+=("Factura #"+str(factura.getCodigo())+"\n")
            messagebox.showinfo("Cobro exitoso","El pago se realizó satisfactoriamente\n"+texto)
            bienvenido()
        txt4.delete(0,END)
        "Despues de reservar exitosamente se vuelve a la pantalla de inicio"

    def pasar(event):
        txt2.config(state="normal")
        for factura in facturasencontradas:
            facturacomparable="Factura #"+str(factura.getCodigo())
            if opciones.get() == facturacomparable:
                txt2.insert(END, "Factura #" + str(factura.getCodigo())+"\n")
                txt2.insert(END,  str(factura.getFecha_y_hora())+"\n")
                txt2.insert(END,  "Concepto:" +str(factura.getConcepto())+"\n")
                txt2.insert(END,  "Valor:" + factura.getValorTotal()+"\n")
                txt2.insert(END, "\n-------------------\n")
                txt2.config(state="disabled")
                facturaseleccionadas.append(factura)
                facturasencontradas.remove(factura)
                global valor
                valor1=(factura.getValorTotal()).replace(",",".")
                valor+=float(valor1)*1000
                combofacturas.remove("Factura #"+str(factura.getCodigo()))
        txt.delete(1.0,END)
        for i in facturasencontradas:
            txt.insert(END, "Factura #" + str(i.getCodigo())+"\n")
            txt.insert(END,  str(i.getFecha_y_hora())+"\n")
            txt.insert(END,  "Concepto:" +str(i.getConcepto())+"\n")
            txt.insert(END,  "Valor:" + i.getValorTotal()+"\n")
            txt.insert(END, "\n----------------------\n")
        opciones.config(values=combofacturas)
        txt3.config(text=str(valor))
            

    def buscar():
        try:
            if cliente != None:
                txt.config(state="normal")
                for factura in Almacenamiento.listaFacturas:
                    if cliente.getIdentificacion() == factura.getUsuario().getIdentificacion():
                        facturasencontradas.append(factura)
                        txt.insert(END, "Factura #" + str(factura.getCodigo())+"\n")
                        txt.insert(END,  str(factura.getFecha_y_hora())+"\n")
                        txt.insert(END,  "Concepto:" +str(factura.getConcepto())+"\n")
                        txt.insert(END,  "Valor:" + factura.getValorTotal()+"\n")
                        txt.insert(END, "\n----------------------\n")
                        combofacturas.append("Factura #"+str(factura.getCodigo()))
                txt.config(state="disabled")
                ra1.place(relheight=0.1, relwidth=0.3, rely=0.25, relx=0.05)
                txt.place(relheight=0.60, rely=0.35, relwidth=0.3, relx=0.05)
                ra2.place(relheight=0.1, relwidth=0.25, rely=0.25, relx=0.7)
                txt2.place(relheight=0.4, rely=0.35, relwidth=0.25, relx=0.7)
                ra3.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.25)
                ra4.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.46)
                txt3.place(relheight=0.05, relwidth=0.25, relx=0.4, rely=0.56)
                ra5.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.60)
                txt4.place(relheight=0.05, relwidth=0.25, relx=0.4, rely=0.70)
                opciones.place(relheight=0.1, relwidth=0.25, relx=0.4, rely=0.36)
                opciones.config(values=combofacturas)
                Buscar.place_forget()
            else:
                messagebox.showerror("Error", "No hay usuario que buscar por else")
        except NameError:
            messagebox.showerror("Error", "No hay usuario que buscar")

    w = Label(
        frame2,
        text="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________",
    )
    w.place(relheight=0.05, relwidth=1, rely=0.20)

    ra1 = Label(frame2, text="Facturas Asociadas", font=("Arial", 10), anchor="center")
    ra3 = Label(frame2, text="Selecione Facturas\na pagar", font=("Arial", 10), anchor="center")
    ra4 = Label(frame2, text="Valor Total", font=("Arial", 10), anchor="center")
    txt = Text(frame2, state="disabled")
    txt2 = Text(frame2, state="disabled",)
    txt3= Label(frame2,text="0", font=("Arial", 10))
    ra2 = Label(frame2, text="Facturas seleccionadas", font=("Arial", 10), anchor="center")
    txt4= Entry(frame2,font=("Arial", 10),justify="center",validate="key",validatecommand=(frame2.register(solonumeros), "%P"))
    ra5=Label(frame2, text="Valor Pagado", font=("Arial", 10), anchor="center")
    opciones = Combobox(frame2,textvariable="facturas")
    opciones.bind("<<ComboboxSelected>>", pasar)

    Buscar = Button(frame2, text="Buscar facturas asociadas", font=("Arial", 10), command=buscar)
    Buscar.place(relheight=0.1, relwidth=0.3, rely=0.5, relx=0.35)

    Aceptar = Button( frame2, text="Aceptar", font=("Arial", 14), relief=RAISED, command=cobrar)
    Aceptar.place(relheight=0.125, relwidth=0.2, rely=0.8, relx=0.52)


def AbrirFuncional():
    window.state(newstate="normal")
    ventanaInicio.state(newstate="withdraw")
    


def AbrirInicio():
    ventanaInicio.state(newstate="normal")
    window.state(newstate="withdraw")


def Cerrartodo():
    Almacenamiento.Serializar()
    ventanaInicio.destroy()
    window.destroy()
    

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
    "3.Estudiante de Matemáticas en la universidad Nacional",
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



Almacenamiento.Deserializar()



ventanaInicio.mainloop()
window.mainloop()

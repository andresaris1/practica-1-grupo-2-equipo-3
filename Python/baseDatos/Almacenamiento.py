import sys
import os
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/modelos")
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/reservacion")
sys.path.append(os.path.dirname(__file__)+ "/../uiMain/Exepciones")

import pickle
from Usuario import *
from Lugar import *
from Empleado import *
from Reserva import *
from Evento import *
from Servicio import *
from Factura import *
from ServicioExterno import *
from ExepcionC1 import *

class Almacenamiento():

    #Inicializar las listas para almacenado
    listaUsuarios = []
    listaEmpleados = []
    listaHabitaciones = []
    listaLugares = []
    listaReservas = []
    listaEventos = []
    listaServicios = []
    listaFacturas = []
    listaServiciosExternos = []
    listaHabitacionesDisponibles = []


    #Metodos de serializar y deserializar
    @classmethod
    def Serializar(cls):
        pathUsuarios = os.path.join(os.path.dirname(__file__), "temp/usuarios.txt")
        fileUsuarios=open(pathUsuarios , "wb")
        pickle.dump(Almacenamiento.listaUsuarios, fileUsuarios)
        fileUsuarios.close()

        pathEmpleados = os.path.join(os.path.dirname(__file__), "temp/empleados.txt")
        fileEmpleados = open(pathEmpleados, "wb")
        pickle.dump(Almacenamiento.listaEmpleados, fileEmpleados)
        fileEmpleados.close()

        pathHabitaciones = os.path.join(os.path.dirname(__file__), "temp/habitaciones.txt")
        fileHabitaciones = open(pathHabitaciones, "wb")
        pickle.dump(Almacenamiento.listaHabitaciones, fileHabitaciones)
        fileHabitaciones.close()

        pathHabitacionesDisponibles = os.path.join(os.path.dirname(__file__), "temp/habitacionesDisponibles.txt")
        fileHabitacionesDisponibles = open(pathHabitacionesDisponibles, "wb")
        pickle.dump(Almacenamiento.listaHabitacionesDisponibles, fileHabitacionesDisponibles)
        fileHabitacionesDisponibles.close()

        pathLugares = os.path.join(os.path.dirname(__file__), "temp/lugares.txt")
        fileLugares = open(pathLugares, "wb")
        pickle.dump(Almacenamiento.listaLugares, fileLugares)
        fileLugares.close()

        pathReservas = os.path.join(os.path.dirname(__file__), "temp/reservas.txt")
        fileReservas = open(pathReservas, "wb")
        pickle.dump(Almacenamiento.listaReservas, fileReservas)
        fileReservas.close()

        pathEventos = os.path.join(os.path.dirname(__file__), "temp/eventos.txt")
        fileEventos = open(pathEventos, "wb")
        pickle.dump(Almacenamiento.listaEventos, fileEventos)
        fileEventos.close()

        pathServicios = os.path.join(os.path.dirname(__file__), "temp/servicios.txt")
        fileServicios = open(pathServicios, "wb")
        pickle.dump(Almacenamiento.listaServicios, fileServicios)
        fileServicios.close()

        pathFacturas = os.path.join(os.path.dirname(__file__), "temp/facturas.txt")
        fileFacturas = open(pathFacturas, "wb")
        pickle.dump(Almacenamiento.listaFacturas, fileFacturas)
        fileFacturas.close()

        pathServiciosExternos = os.path.join(os.path.dirname(__file__), "temp/serviciosExternos.txt")
        fileServiciosExternos = open(pathServiciosExternos, "wb")
        pickle.dump(Almacenamiento.listaServiciosExternos, fileServiciosExternos)
        fileServiciosExternos.close()

        pathcontador = os.path.join(os.path.dirname(__file__), "temp/contadorFacturas.txt")
        filecontador = open(pathcontador, "wb")
        pickle.dump(Factura.contador, filecontador)
        filecontador.close()








    
    @classmethod
    def Deserializar(cls):
        pathUsuarios = os.path.join(os.path.dirname(__file__), "temp/usuarios.txt")
        fileUsuarios=open(pathUsuarios , "rb")
        Almacenamiento.listaUsuarios=pickle.load(fileUsuarios)
        fileUsuarios.close()

        pathEmpleados = os.path.join(os.path.dirname(__file__), "temp/empleados.txt")
        fileEmpleados = open(pathEmpleados, "rb")
        Almacenamiento.listaEmpleados = pickle.load(fileEmpleados)
        fileEmpleados.close()

        pathHabitaciones = os.path.join(os.path.dirname(__file__), "temp/habitaciones.txt")
        fileHabitaciones = open(pathHabitaciones, "rb")
        Almacenamiento.listaHabitaciones = pickle.load(fileHabitaciones)
        fileHabitaciones.close()

        pathHabitacionesDisponibles = os.path.join(os.path.dirname(__file__), "temp/habitacionesDisponibles.txt")
        fileHabitacionesDisponibles = open(pathHabitacionesDisponibles, "rb")
        Almacenamiento.listaHabitacionesDisponibles = pickle.load(fileHabitacionesDisponibles)
        fileHabitacionesDisponibles.close()

        pathLugares = os.path.join(os.path.dirname(__file__), "temp/lugares.txt")
        fileLugares = open(pathLugares, "rb")
        Almacenamiento.listaLugares = pickle.load(fileLugares)
        fileLugares.close()

        pathReservas = os.path.join(os.path.dirname(__file__), "temp/reservas.txt")
        fileReservas = open(pathReservas, "rb")
        Almacenamiento.listaReservas = pickle.load(fileReservas)
        fileReservas.close()

        pathEventos = os.path.join(os.path.dirname(__file__), "temp/eventos.txt")
        fileEventos = open(pathEventos, "rb")
        Almacenamiento.listaEventos = pickle.load(fileEventos)
        fileEventos.close()

        pathServicios = os.path.join(os.path.dirname(__file__), "temp/servicios.txt")
        fileServicios = open(pathServicios, "rb")
        Almacenamiento.listaServicios = pickle.load(fileServicios)
        fileServicios.close()

        pathFacturas = os.path.join(os.path.dirname(__file__), "temp/facturas.txt")
        fileFacturas = open(pathFacturas, "rb")
        Almacenamiento.listaFacturas = pickle.load(fileFacturas)
        fileFacturas.close()

        pathServiciosExternos = os.path.join(os.path.dirname(__file__), "temp/serviciosExternos.txt")
        fileServiciosExternos = open(pathServiciosExternos, "rb")
        Almacenamiento.listaServiciosExternos = pickle.load(fileServiciosExternos)
        fileServiciosExternos.close()

        pathcontador = os.path.join(os.path.dirname(__file__), "temp/contadorFacturas.txt")
        filecontador = open(pathcontador, "rb")
        Factura.contador= pickle.load(filecontador)
        filecontador.close()




    def crearUsuario(nombre, identificacion:int, telefono, cuentaBancaria):
        cliente=Usuario(nombre,identificacion,telefono,"Cliente",cuentaBancaria)
        Almacenamiento.listaUsuarios.append(cliente)

    def buscarUsuario(id:int) -> Usuario:
        usuario=None
        for cli in Almacenamiento.listaUsuarios:
            if (id==int(cli.getIdentificacion())):
                usuario=cli
                break
        return usuario         

    def crearHabitacion(nombre:str,descripcion,numero,capacidad):
        valor=Lugar.valorSegunTipo(descripcion)
        habitacion=Lugar(nombre,descripcion,valor,numero,capacidad)
        Almacenamiento.listaHabitaciones.append(habitacion)
        Almacenamiento.listaHabitacionesDisponibles.append(habitacion)

    def buscarHabitacion(numero) -> Lugar:
        habitacion=None
        for hab in Almacenamiento.listaHabitaciones:
            if (numero==hab.getNumero()):
                habitacion=hab
                break
        return habitacion
    
    def crearLugar(nombre:str,descripcion,numero,capacidad):
        valor=Lugar.valorSegunTipo(descripcion)
        lugar=Lugar(nombre,descripcion,valor,numero,capacidad)
        Almacenamiento.listaLugares.append(lugar)

    def buscarLugar(numero) -> Lugar:
        lugar=None
        for lug in Almacenamiento.listaLugares:
            if (numero==lug.getNumero()):
                lugar=lug
                break
        return lugar
    
    def crearEmpleado(nombre: str, identificacion, telefono, cargo):
        empleado=Empleado(nombre,identificacion,telefono,cargo)
        Almacenamiento.listaEmpleados.append(empleado)

    def buscarEmpleado(id) -> Empleado:
        Empleado=None
        for emp in Almacenamiento.listaEmpleados:
            if (id==emp.getIdentificacion()):
                Empleado=emp
                break
        return Empleado
    
    def crearReserva(fentrada,fsalida,habitaciones:list,aporte,cliente:Usuario):
        reserva=Reserva(fentrada,fsalida,habitaciones,aporte,cliente)
        Almacenamiento.listaReservas.append(reserva)
        return(reserva.__str__())

    def buscarReserva(cliente:Usuario) -> Reserva:
        Reserva=None
        for res in Almacenamiento.listaReservas:
            if (cliente==res.getCliente()):
                Reserva=res
                break
        return Reserva
    
    def crearEvento(codigo,lugar, cliente: Usuario, servicios:list, fecha, duracion, numeroAsistentes, empleados:Empleado,descripcion):
        evento=Evento(codigo,lugar,cliente,servicios,fecha,duracion,numeroAsistentes,empleados,descripcion)
        Almacenamiento.listaEventos.append(evento)

    def buscarEvento(cliente) -> Evento:
        Evento=None
        for even in Almacenamiento.listaEventos:
            if (cliente==even.getCliente()):
                Evento=even
                break
        return Evento
    
    def crearServicio(nombre, valor, descripcion):
        servicio=Servicio(nombre,valor,descripcion)
        Almacenamiento.listaServicios.append(servicio)

    def buscarServicio(nombre) -> Servicio:
        Servicio=None
        for ser in Almacenamiento.listaServicios:
            if (nombre==ser.getNombre()):
                Servicio=ser
                break
        return Servicio
    
    def crearServicioExterno(nombre, cliente: Usuario, descripcion):
        sExterno=ServicioExterno(nombre,cliente,descripcion)
        Almacenamiento.listaServiciosExternos.append(sExterno)

    def BuscarServicioExterno(cliente:Usuario) -> ServicioExterno:
        sExterno=None
        for ser in Almacenamiento.listaServiciosExternos:
            if (cliente==ser.getCliente()):
                sExterno=ser
                break
        return sExterno
    
    def crearFactura(cliente:Usuario, empleado: Empleado, listaItems: list, concepto):
        factura=Factura(cliente,empleado,listaItems,concepto)
        Almacenamiento.listaFacturas.append(factura)
        return (factura.imprimirFactura())
    
    def buscarFactura(cliente: Usuario) -> Factura:
        factura=None
        for fac in Almacenamiento.listaFacturas():
            if (cliente==fac.getUsuario()):
                factura=fac
                break
        return factura
    





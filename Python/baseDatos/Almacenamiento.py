import sys
import os
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/modelos")
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/reservacion")

import pickle
from Usuario import *
from Lugar import *
from Empleado import *
from Reserva import *
from Evento import *
from Servicio import *
from Factura import *
from ServicioExterno import *

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
        path = os.path.join(os.path.dirname(__file__), "temp/usuarios.txt")
        fileUsuarios=open(path , "wb")
        pickle.dump(Almacenamiento.listaUsuarios, fileUsuarios)
        fileUsuarios.close()

        path = os.path.join(os.path.dirname(__file__), "temp/empleados.txt")
        fileEmpleados = open(path, "wb")
        pickle.dump(Almacenamiento.listaEmpleados, fileEmpleados)
        fileEmpleados.close()

        path = os.path.join(os.path.dirname(__file__), "temp/habitaciones.txt")
        fileHabitaciones = open(path, "wb")
        pickle.dump(Almacenamiento.listaHabitaciones, fileHabitaciones)
        fileHabitaciones.close()

        path = os.path.join(os.path.dirname(__file__), "temp/lugares.txt")
        fileLugares = open(path, "wb")
        pickle.dump(Almacenamiento.listaLugares, fileLugares)
        fileLugares.close()

        path = os.path.join(os.path.dirname(__file__), "temp/reservas.txt")
        fileReservas = open(path, "wb")
        pickle.dump(Almacenamiento.listaReservas, fileReservas)
        fileReservas.close()

        path = os.path.join(os.path.dirname(__file__), "temp/eventos.txt")
        fileEventos = open(path, "wb")
        pickle.dump(Almacenamiento.listaEventos, fileEventos)
        fileEventos.close()

        path = os.path.join(os.path.dirname(__file__), "temp/servicios.txt")
        fileServicios = open(path, "wb")
        pickle.dump(Almacenamiento.listaServicios, fileServicios)
        fileServicios.close()

        path = os.path.join(os.path.dirname(__file__), "temp/serviciosExternos.txt")
        fileServiciosExternos = open(path, "wb")
        pickle.dump(Almacenamiento.listaServiciosExternos, fileServiciosExternos)
        fileServiciosExternos.close()






    
    @classmethod
    def Deserializar(cls):
        path = os.path.join(os.path.dirname(__file__), "temp/usuarios.txt")
        fileUsuarios=open(path , "rb")
        Almacenamiento.listaUsuarios=pickle.load(fileUsuarios)
        fileUsuarios.close()

        path = os.path.join(os.path.dirname(__file__), "temp/empleados.txt")
        fileEmpleados = open(path, "rb")
        Almacenamiento.listaEmpleados = pickle.load(fileEmpleados)
        fileEmpleados.close()

        path = os.path.join(os.path.dirname(__file__), "temp/habitaciones.txt")
        fileHabitaciones = open(path, "rb")
        Almacenamiento.listaHabitaciones = pickle.load(fileHabitaciones)
        fileHabitaciones.close()

        path = os.path.join(os.path.dirname(__file__), "temp/lugares.txt")
        fileLugares = open(path, "rb")
        Almacenamiento.listaLugares = pickle.load(fileLugares)
        fileLugares.close()

        path = os.path.join(os.path.dirname(__file__), "temp/reservas.txt")
        fileReservas = open(path, "rb")
        Almacenamiento.listaReservas = pickle.load(fileReservas)
        fileReservas.close()

        path = os.path.join(os.path.dirname(__file__), "temp/eventos.txt")
        fileEventos = open(path, "rb")
        Almacenamiento.listaEventos = pickle.load(fileEventos)
        fileEventos.close()

        path = os.path.join(os.path.dirname(__file__), "temp/servicios.txt")
        fileServicios = open(path, "rb")
        Almacenamiento.listaServicios = pickle.load(fileServicios)
        fileServicios.close()

        path = os.path.join(os.path.dirname(__file__), "temp/facturas.txt")
        fileFacturas = open(path, "rb")
        Almacenamiento.listaFacturas = pickle.load(fileFacturas)
        fileFacturas.close()

        path = os.path.join(os.path.dirname(__file__), "temp/serviciosExternos.txt")
        fileServiciosExternos = open(path, "rb")
        Almacenamiento.listaServiciosExternos = pickle.load(fileServiciosExternos)
        fileServiciosExternos.close()


    def crearUsuario(nombre, identificacion, telefono, cuentaBancaria):
        cliente=Usuario(nombre,identificacion,telefono,"Cliente",cuentaBancaria)
        Almacenamiento.listaUsuarios.append(cliente)

    def buscarUsuario(id) -> Usuario:
        usuario=None
        for cli in Almacenamiento.listaUsuarios:
            if (id==cli.getIdentificacion()):
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
    
    def crearServicioExterno(nombre, cliente: Usuario, eventoAsociado, descripcion):
        sExterno=ServicioExterno(nombre,cliente,eventoAsociado,descripcion)
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
    





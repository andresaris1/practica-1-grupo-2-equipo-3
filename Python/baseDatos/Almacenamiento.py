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
        path = os.path.join(os.path.dirname(__file__), "temp/usuario.txt")
        fileUsuarios=open(path , "wb")
        pickle.dump(Almacenamiento.listaUsuarios, fileUsuarios)
        print("Metodo serializar")
        fileUsuarios.close()
    
    @classmethod
    def Deserializar(cls):
        path = os.path.join(os.path.dirname(__file__), "temp/usuario.txt")
        fileUsuarios=open(path , "rb")
        Almacenamiento.listaUsuarios=pickle.load(fileUsuarios)
        fileUsuarios.close()
    
    def crearUsuario(nombre, identificacion, telefono, cuentaBancaria):
        cliente=Usuario(nombre,identificacion,telefono,"Cliente",cuentaBancaria)
        Almacenamiento.listaUsuarios.append(cliente)

    def buscarUsuario(id) -> Usuario:
        usuario=None
        for cliente in Almacenamiento.listaUsuarios:
            if (id==cliente.getIdentificacion()):
                usuario=cliente
                break
        return usuario         

    def crearHabitacion(nombre,descripcion,numero,capacidad):
        habitacion=Lugar(nombre, descripcion,numero,capacidad)
        Almacenamiento.listaHabitaciones.append(habitacion)

    def buscarHabitacion(numero) -> Lugar:
        habitacion=None
        for hab in Almacenamiento.listaHabitaciones:
            if (numero==hab.getNumero()):
                habitacion=hab
                break
        return habitacion
    
    def crearEmpleado(nombre, identificacion, telefono, cargo):
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

    def buscarReserva(cliente) -> Reserva:
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
        
    def buscarFactura(cliente: Usuario) -> Factura:
        factura=None
        for fac in Almacenamiento.listaFacturas():
            if (cliente==fac.getUsuario()):
                factura=fac
                break
        return factura





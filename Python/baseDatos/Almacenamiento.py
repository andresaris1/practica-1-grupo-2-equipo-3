import sys
import os
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/modelos")
sys.path.append(os.path.dirname(__file__)+ "/../gestorAplicacion/reservacion")

import pickle
from Usuario import *
from Lugar import *

class Almacenamiento():
    from Empleado import Empleado
    from Reserva import Reserva
    from Evento import Evento
    from Servicio import Servicio
    from ServicioExterno import ServicioExterno

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

    def buscarUsuario(id):
        usuario=None
        for cliente in Almacenamiento.listaUsuarios:
            if (id==cliente.getIdentificacion()):
                usuario=cliente
                break
        return usuario
                

    def crearHabitacion(nombre,descripcion,numero,capacidad):
        habitacion=Lugar(nombre, descripcion,numero,capacidad)
        Almacenamiento.listaHabitaciones.append(habitacion)


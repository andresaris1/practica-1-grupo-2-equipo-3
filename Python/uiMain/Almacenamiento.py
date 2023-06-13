import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/modelos"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/reservacion"))

import pickle

class Almacenamiento():

    from Usuario import Usuario
    from Empleado import Empleado
    from Lugar import Lugar
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
        fileUsuarios=open('../usuario' , "wb")
        pickle.dump(Almacenamiento.listaUsuarios, fileUsuarios)
        print("Metodo serializar")
        fileUsuarios.close()
    
    @classmethod
    def Deserializar(cls):
        fileUsuarios=open('../usuario' , "rb")
        Almacenamiento.listaUsuarios=pickle.load(fileUsuarios)
        fileUsuarios.close()




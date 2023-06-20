from datetime import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../modelos"))
from Usuario import Usuario

from Lugar import Lugar


class Reserva:
    def __init__(self, fechaEntrada:datetime, fechaSalida:datetime, habitaciones:list, aporte, cliente: Usuario):
        self._fechaEntrada = fechaEntrada
        self._fechaSalida = fechaSalida
        self._habitaciones = habitaciones
        self._aporte = aporte
        self._cliente = cliente
    
    def __str__(self):
        habitaciones = ""
        for habitacion in self._habitaciones:
            h=habitacion.getNumero()
            habitaciones+=("Habitacion: "+str(h)+"\n")
        fe = self._fechaEntrada.strftime('%d/%m/%Y')
        fs = self._fechaSalida.strftime('%d/%m/%Y')
        return f"Nombre:\n{self._cliente.getNombre()}\n\nFechas:\n{fe} \n{fs}\n\nHabitaciones:\n{habitaciones}"
    
    def getFechaSalida(self):
        return self._fechaSalida
    
    def setFechaSalida(self, fechaSalida):
        self._fechaSalida = fechaSalida
        
    def getCliente(self):
        return self._cliente
    
    def getFechaEntrada(self):
        return self._fechaEntrada
    
    def setFechaEntrada(self, fechaEntrada):
        self._fechaEntrada = fechaEntrada
        
    def getAporte(self):
        return self._aporte
    
    def setAporte(self, aporte):
        self._aporte = aporte
        
    def getHabitaciones(self):
        return self._habitaciones
    
    def setHabitaciones(self, habitaciones):
        self._habitaciones = habitaciones
        


    

    
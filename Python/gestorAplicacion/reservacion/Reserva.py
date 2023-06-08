import datetime

from Python.gestorAplicacion.modelos.Usuario import Usuario
from Python.gestorAplicacion.reservacion.Lugar import Lugar



class Reserva:
    def __init__(self, fechaEntrada, fechaSalida, habitaciones, aporte, cliente):
        self._fechaEntrada = self.parsear_fecha(fechaEntrada)
        self._fechaSalida = self.parsear_fecha(fechaSalida)
        self._habitaciones = habitaciones
        self._aporte = aporte
        self._cliente = cliente
        self._fe = fechaEntrada
        self._fs = fechaSalida

    def parsear_fecha(self, fecha):
        formato = "%d/%m/%Y"
        return datetime.strptime(fecha, formato).date()
    
    def listaHabitaciones(self):
        lista = ""
        for habitacion in self._habitaciones:
            lista += f"{habitacion.getNumero()} {habitacion.getTipo()}\n"
        return lista
    
    def __str__(self):
        habitaciones = self.listaHabitaciones()
        return f"La reserva se hizo a nombre de: {self.cliente.nombre} Entre los días: {self.fe} y {self.fs} para las habitaciones:\n{habitaciones}"
    
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
        
    def getFe(self):
        return self._fe
    
    def setFe(self, fe):
        self._fe = fe
        
    def getFs(self):
        return self._fs
    
    def setFs(self, fs):
        self._fs = fs


    

    
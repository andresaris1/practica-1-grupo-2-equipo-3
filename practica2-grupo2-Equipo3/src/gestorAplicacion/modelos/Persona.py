import abc

class Persona(abc.ABC):
    def __init__(self, nombre, identificacion, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono

    @abc.abstractmethod
    def informacion(self):
        pass

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getIdentificacion(self):
        return self.identificacion

    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

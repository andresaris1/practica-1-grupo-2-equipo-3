import abc

class Persona(abc.ABC):
    def __init__(self, nombre, identificacion, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono

    @abc.abstractmethod
    def informacion(self):
        pass

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_identificacion(self):
        return self.identificacion

    def set_identificacion(self, identificacion):
        self.identificacion = identificacion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

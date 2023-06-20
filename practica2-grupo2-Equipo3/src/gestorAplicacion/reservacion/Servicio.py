

"""
Clase Servicio:
Clase encargada de crear y serializar los objetos de tipo Servicio.
De esta clase heredan otras subclases, tales como ServicioExterno,
Evento, Reserva, etc.  
"""
class Servicio:
    
    """
    Constructor de la clase Servicio:
    Parámetros:
        nombre: Nombre del servicio.
        valor: Valor monetario del servicio.
    """
    def __init__(self, nombre, valor,descripcion=""):
        self.nombre = nombre
        self.valor = valor
        self.descripcion = descripcion
        
    #Getters y Setters
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
        
    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

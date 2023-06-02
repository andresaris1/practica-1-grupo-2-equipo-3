import Servicio

"""
Clase ServicioExterno encargada de crear los servicios externos que se le ofrecen
a los clientes dentro de la reserva de eventos.
Estos servicios externos pueden ser de diferentes tipos,
como por ejemplo: Sonido, Entretenimiento, Decoración, etc.
"""

class ServicioExterno(Servicio):
    
    
    """
    Constructor de la clase ServicioExterno:
    Parámetros:
        nombre: Nombre del servicio externo.
        cliente: Cliente (objeto de tipo Usuario) que solicita el servicio externo.
        eventoAsociado: Evento (objeto de tipo Evento) al que se le solicita el servicio externo.
        descripcion (opcional): Descripción del servicio externo.
    """
    def __init__(self, nombre, cliente, eventoAsociado, descripcion=""):
        super().__init__(nombre, self.valorSegunTipo(nombre),descripcion)
        self.empresaContratada = self.empresaSegunTipo(nombre)
        self.descripcion = descripcion
        self.cliente = cliente
        self.eventoAsociado = eventoAsociado
        
        
    """
    Este método estático retorna el valor monetario de un
    servicio externo según el tipo de servicio externo.
    """
    @staticmethod
    def valorSegunTipo(nombre):
        if nombre == "entretenimiento":
            return 100000
        elif nombre == "sonido":
            return 50000
        elif nombre == "decoracion":
            return 200000
        else:
            return -1
        
        
    """
    Este método estático se encarga de decidir qué empresa se contratará para
    brindar el servicio externo. Esta decisión se tomará en función del tipo de
    servicio externo.
    """
    @staticmethod
    def empresaSegunTipo(nombre):
        if nombre == "entretenimiento":
            return "Entretenimiento S.A.S"
        elif nombre == "sonido":
            return "Sonido S.A.S"
        elif nombre == "decoracion":
            return "Decoracion S.A.S"
        else:
            return None


    # Getters y Setters
    def getEmpresaContratada(self):
        return self.empresaContratada

    def setEmpresaContratada(self, empresaContratada):
        self.empresaContratada = empresaContratada

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente
        
    def getEventoAsociado(self):
        return self.eventoAsociado
    
    def setEventoAsociado(self, eventoAsociado):
        self.eventoAsociado = eventoAsociado
        
    

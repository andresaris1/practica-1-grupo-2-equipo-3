
"""
Clase Evento encargada de crear los eventos, los cuales son un tipo de servicio
que se le ofrece a los clientes, estos eventos pueden ser de diferentes tipos,
como por ejemplo: bodas, cumpleaños, fiestas, etc.
El evento puede usar diferentes servicios externos, como por ejemplo:
Sonido, Entretenimiento, etc.
El evento también puede realizarse en distintos lugares del Hotel:
Piscina, Salón, Terraza.
"""

class Evento(Servicio):
    
    """
    Constructor de la clase Evento:
    Parámetros:
        lugar: Lugar donde se realizará el evento.
        cliente: Cliente (objeto de tipo Usuario) que solicita el evento.
        servicios: Lista de servicios externos (objetos de tipo ServicioExterno que se usarán en el evento.
        fecha: Fecha en la que se realizará el evento en formato (dd/mm/aaaa).
        duracion: Duración del evento en minutos.
        numeroAsistentes: Número de asistentes al evento.
        empleados: Lista de empleados (objetos de clase Empleado) necesarios para el evento.
        codigo: Código del evento.
        descripcion (opcional): Descripción del evento.
    """
    def __init__(self, codigo, lugar, cliente, servicios, fecha, duracion, numeroAsistentes, empleados,descripcion=""):
        super().__init__(f"Evento en {lugar}" , self.calcularValor(lugar, servicios, duracion, numeroAsistentes, empleados))
        self.lugar = lugar
        self.cliente = cliente
        self.servicios = servicios
        self.duracion = duracion
        self.numeroAsistentes = numeroAsistentes
        self.empleados = empleados
        self.fecha = fecha
        self.codigo = codigo
        self.descripcion = descripcion
        
    
    """
    Método para calcular el valor monetario de evento en función
    de los servicios externos, el lugar, la duración, el número de asistentes.
    """
    @staticmethod
    def calcularValor(lugar, servicios, duracion, numeroAsistentes, empleados):
        valor = 0
        valor += lugar.getValor()
        for servicioExterno in servicios:
            valor += servicioExterno.getValor()
        valor += duracion * 10000
        valor += numeroAsistentes * 10000
        for empleado in empleados:
            valor += empleado.getNomina()
        return valor
    
    
    """
    ToString de la clase Evento.
    """
    def __str__(self):
        return "Lugar del evento: " + str(self.getLugar()) + "\n" + "Cliente asociado: " + str(self.getCliente()) + "\n" + "Fecha: " + str(self.getFecha()) + "\n" + "Duracion: " + str(self.getDuracion()) + "Numero de asistentes: " + str(self.getNumeroAsistentes())
    
    
    #Getters y Setters
    
    def getLugar(self):
        return self.lugar
    
    def setLugar(self, lugar):
        self.lugar = lugar
        
    def getCliente(self):
        return self.cliente
    
    def setCliente(self, cliente):
        self.cliente = cliente
        
    def getServicios(self):
        return self.servicios
    
    def setServicios(self, servicios):
        self.servicios = servicios
        
    def getDuracion(self):
        return self.duracion
    
    def setDuracion(self, duracion):
        self.duracion = duracion
        
    def getNumeroAsistentes(self):
        return self.numeroAsistentes
    
    def setNumeroAsistentes(self, numeroAsistentes):
        self.numeroAsistentes = numeroAsistentes
        
    def getEmpleados(self):
        return self.empleados
    
    def setEmpleados(self, empleados):
        self.empleados = empleados
        
    def getFecha(self):
        return self.fecha
    
    def setFecha(self, fecha):
        self.fecha = fecha
        
    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, codigo):
        self.codigo = codigo
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
        
    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
        
    """
    Este es un getter no tan obvio: se encarga de recorrer cada uno de los 
    servicios externos, de modo que obtiene una lista con las empresas contratadas
    para cada uno de ellos y posteriormente la retorna.
    """
    def getEmpresasContratadas(self):
        lista = []

        for servicio in self.servicios:
            lista.append(servicio.getEmpresaContratada())

        return lista

        
        
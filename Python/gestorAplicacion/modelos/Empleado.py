from Persona import Persona

class Empleado(Persona):

    _nomina = 560000

    def __init__(self, nombre, identificacion, telefono, cargo):
        super().__init__(nombre, identificacion, telefono)
        self._cargo = cargo
        self._comision = 1000 # Valor inicial para todos los empleados

    def informacion(self):
        return ("Nombre: " + self.getNombre() + "\n" +
            "Documento: " + self.getIdentificacion() + "\n" +
            "Cargo: " + self.getCargo() + "\n" +
            "Nomina: " + str(self.getNomina()) + "\n")
    
    def calcularComision(self, valorPagado):
        x = 0.02 * valorPagado
        self._comision += x

    
    def getCargo(self):
        return self._cargo
    
    def setCargo(self, cargo):
        self._cargo = cargo
        
    def getComision(self):
        return self._comision
    
    def setComision(self, comision):
        self._comision = comision
        
    def getNomina(self):
        return self._nomina
from Persona import Persona

class Usuario(Persona):
    
    def __init__(self, nombre, identificacion, telefono, tipo, cuenta_bancaria):
        super().__init__(nombre, identificacion, telefono)
        self.tipo = tipo
        self.cuenta_bancaria = cuenta_bancaria
        self.lista_facturas = []

    def informacion(self):
        return f"Nombre: {self.nombre}\nTelefono: {self.telefono}\nDocumento: {self.identificacion}"

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def getLista_facturas(self):
        return self.lista_facturas

    def setLista_facturas(self, lista_facturas):
        self.lista_facturas = lista_facturas

    def get_cuenta_bancaria(self):
        return self.cuenta_bancaria

    def set_cuenta_bancaria(self, cuenta_bancaria):
        self.cuenta_bancaria = cuenta_bancaria

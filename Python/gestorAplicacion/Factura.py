import datetime

class Factura:
    contador=0
    def __init__(self,usuario,empleado,listaItems,destino,concepto):
        Factura.contador+=1
        self._codigo = Factura.contador
        self._fecha_y_hora =datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time())
        self._usuario = usuario
        self._empleado = empleado
        self._items = []
        self._valorTotal = 0
        self._estado = 0
        self._destinos = []
        self._concepto = ""

        usuario.listaFacturas.append(self)
        empleado.calcularComision(100)

def sumarDeuda(usuario):
        valorDeuda=0
        for factura in user.listaFacturas:
                if (factura.get_estado()==0):
                        valorDeuda = valorDeuda + factura.get_valorTotal()
        return valorDeuda

def facturasEnDeuda(usuario):
        print("Terminar")



#GETERS AND SETERRS
def getCodigo(self):
        return self._codigo

def setCodigo(self, codigo):
        self._codigo = codigo

def getFecha_y_hora(self):
        return self._fecha_y_hora

def setFecha_y_hora(self, fecha_y_hora):
        self._fecha_y_hora = fecha_y_hora

def get_usuario(self):
        return self._usuario

def set_usuario(self, usuario):
        self._usuario = usuario

def get_empleado(self):
        return self._empleado

def set_empleado(self, empleado):
        self._empleado = empleado

def get_items(self):
        return self._items

def set_items(self, items):
        self._items = items

def get_valorTotal(self):
        return self._valorTotal

def set_valorTotal(self, valorTotal):
        self._valorTotal = valorTotal

def get_estado(self):
        return self._estado

def set_estado(self, estado):
        self._estado = estado

def get_destinos(self):
        return self._destinos

def set_destinos(self, destinos):
        self._destinos = destinos

def get_concepto(self):
        return self._concepto

def set_concepto(self, concepto):
        self._concepto = concepto
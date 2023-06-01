import datetime

class Factura:
    contador=0
    def __init__(self,user,empleado,listaItems,destino,concepto):
        self.estado=0
        self.cliente=user
        self.empleado=empleado        
        self.utems=listaItems
        self.destinos=destino
        self.concepto=concepto
        self.valorTotal=100

        self.fecha_y_hora = datetime.datetime.combine(datetime.date.today(), datetime.datetime.now().time())
        Factura.contador+=1
        self.codigo=Factura.contador

        user.listaFacturas.append(self)
        empleado.calcularComision(valorTotal)

    def 


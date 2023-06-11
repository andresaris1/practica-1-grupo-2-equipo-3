import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../modelos"))
from Persona import Persona
from Empleado import Empleado
from Usuario import Usuario

from Servicio import Servicio
from Destinos import Destinos


class Factura():
        contador = 0
        def __init__(self, usuario, empleado, listaItems, concepto):
            Factura.contador += 1
            self._codigo = Factura.contador

            self._fecha_y_hora = datetime.datetime.combine(
                datetime.date.today(), datetime.datetime.now().time())

            self._usuario = usuario
            self._empleado = empleado
            self._items = listaItems
            self._valorTotal=self.valorTotal()
            self._estado = 0
            #self._destinos = destinos
            self._concepto = concepto

            self._usuario.lista_facturas.append(self)


        def valorTotal(self):
            total=0
            servicios_iter = iter(self._items)
            while True:
                try:
                    servicio = next(servicios_iter)
                    total=total+servicio.valor
                except StopIteration:
                    break
            total=format(total, ',')
            return(total)

        @classmethod
        def sumarDeuda(cls,usuario):
            total=0
            facturas_iter = iter(usuario.getLista_facturas())
            while True:
                try:
                    factura = next(facturas_iter)
                    if (factura.getEstado!=0):
                        total=total+int(factura.getValorTotal())
                except StopIteration:
                    break
            total=format(total, ',')
            return(total)


        @classmethod
        def facturasEnDeuda(cls,usuario):
            facturasDeudas = []
            for factura in usuario.get_lista_facturas():
                if factura.getEstado() == 0:
                    facturasDeudas.append(factura)
            return facturasDeudas

        @classmethod 
        def imprimirCodigos(cls, facturas):
            codigos = []
            for factura in facturas:
                codigos.append(factura.getCodigo())
            return ", ".join(codigos)

        @classmethod 
        def realizarCobro(cls, facturas,suma,valorIngresado):

            if (valorIngresado<suma):
                    print("No le alcanza")
            else:
                d=valorIngresado
                for factura in facturas:
                    factura.setEstado(1)
                    factura.getEmpleado().calcularComision(factura.getValor)
                    d=d-factura.getValorTotal()
            return d

        def imprimirFactura(self):
            #Creando la lista de columnas de los servicios y sus precios
            servicios_iter = iter(self._items)
            lista = []
            lista.append("Concepto \t Valor"+"\n")
            while True:
                try:
                    servicio = next(servicios_iter)
                    lista.append(servicio.nombre + " \t" + str(servicio.valor) + "\n")
                except StopIteration:
                    break
                servicioValor = ''
                for elemento in lista:
                    servicioValor += str(elemento) 
            
            #Crear zona de informacion principal
            infoP=[]
            infoP.append("-------------------------------------------")
            infoP.append("Codigo de factura: " + str(self._codigo) )
            infoP.append("Fecha y Hora: " + self._fecha_y_hora.strftime('%d/%m/%Y %H:%M:%S'))
            infoP.append("Empleado: " + self._empleado.nombre )
            infoP.append("Cliente: " + self._usuario.nombre  +"\n" )
            infoP.append(servicioValor)
            infoP.append("Valor total:  " + str(self._valorTotal) )
            infoP.append("-------------------------------------------")

            facturaFinal=''
            for elemento in infoP:
                facturaFinal += str(elemento) + "\n"

            return(facturaFinal)






        # GETERS AND SETERRS
        def getCodigo(self):
            return self._codigo


        def setCodigo(self, codigo):
            self._codigo = codigo


        def getFecha_y_hora(self):
            return self._fecha_y_hora


        def setFecha_y_hora(self, fecha_y_hora):
            self._fecha_y_hora = fecha_y_hora


        def getUsuario(self):
            return self._usuario


        def setUsuario(self, usuario):
            self._usuario = usuario


        def getEmpleado(self):
            return self._empleado


        def setEmpleado(self, empleado):
            self._empleado = empleado


        def getItems(self):
            return self._items


        def setItems(self, items):
            self._items = items


        def getValorTotal(self):
            return self._valorTotal


        def setValorTotal(self, valorTotal):
            self._valorTotal = valorTotal


        def getEstado(self):
            return self._estado


        def setEstado(self, estado):
            self._estado = estado


        def getDestinos(self):
            return self._destinos


        def setDestinos(self, destinos):
            self._destinos = destinos


        def getConcepto(self):
            return self._concepto


        def setConcepto(self, concepto):
            self._concepto = concepto


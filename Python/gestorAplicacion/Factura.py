import datetime
from gestorAplicacion.Servicio import Servicio
from Usuario import Usuario


class Factura:
        contador = 0
        def __init__(self, usuario, empleado, listaItems, destino, concepto):
            Factura.contador += 1
            self._codigo = Factura.contador
            self._fecha_y_hora = datetime.datetime.combine(
                datetime.date.today(), datetime.datetime.now().time()
            )
            self._usuario = usuario
            self._empleado = empleado
            self._items = []
            self._valorTotal = 0 #crear metodo
            self._estado = 0
            self._destinos = []
            self._concepto = ""

            self._usuario.lista_facturas.append(self)


        def valorTotal(self):
            total = 0
            for servicio in self._items:
                x = servicio.getValor()
                total += x
            
            if self._destinos is not None:
                for destino in self._destinos:
                    x = destino.get_valor()
                    total += x
            
            return total

        def sumarDeuda(usuario):
            valorDeuda = 0
            for factura in usuario.get_lista_facturas:
                if factura.getEstado() == 0:
                    valorDeuda = valorDeuda + factura.getValorTotal()
            return valorDeuda


        def facturasEnDeuda(usuario):
            facturasDeudas = []
            for factura in usuario.get_lista_facturas():
                if factura.getEstado() == 0:
                    facturasDeudas.append(factura)
            return facturasDeudas
        
        def imprimirCodigos(facturas):
            codigos = []
            for factura in facturas:
                codigos.append(factura.getCodigo())
            return ", ".join(codigos)
        
        def realizarCobro(facturas,suma,valorIngresado):
                
            if (valorIngresado<suma):
                    print("No le alcanza")
            else:
                d=valorIngresado
                for factura in facturas:
                    factura.setEstado(1)
                    factura.getEmpleado().calcularComision(factura.getValor)
                    d=d-factura.getValorTotal()
            return d




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

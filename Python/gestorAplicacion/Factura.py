import datetime
from gestorAplicacion.Servicio import Servicio

class Factura:
        contador = 0
        def __init__(self, usuario, empleado, listaItems, destinos, concepto):
            Factura.contador += 1
            self._codigo = Factura.contador

            self._fecha_y_hora = datetime.datetime.combine(
                datetime.date.today(), datetime.datetime.now().time())
            
            self._usuario = usuario
            self._empleado = empleado
            self._items = listaItems
            self._valorTotal = 0 #crear metodo
            self._estado = 0
            self._destinos = destinos
            self._concepto = concepto

            self._usuario.lista_facturas.append(self)


        def valorTotal(self):
            total = 0
            for servicio in self._items:
                x = servicio.getValor()
                total = total + x
            
            if self._destinos is not None:
                for destino in self._destinos:
                    x = destino.get_valor()
                    total = total + x
            
            return total

        def sumarDeuda(self,usuario):
            valorDeuda = 0
            for factura in usuario.get_lista_facturas:
                if factura.getEstado() == 0:
                    valorDeuda = valorDeuda + factura.getValorTotal()
            return valorDeuda


        def facturasEnDeuda(self,usuario):
            facturasDeudas = []
            for factura in usuario.get_lista_facturas():
                if factura.getEstado() == 0:
                    facturasDeudas.append(factura)
            return facturasDeudas
        
        def imprimirCodigos(slef, facturas):
            codigos = []
            for factura in facturas:
                codigos.append(factura.getCodigo())
            return ", ".join(codigos)
        
        def realizarCobro(self, facturas,suma,valorIngresado):
                
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
            sb = []
            lista = []
            empleado = ""
            lista.append("Concepto \t Valor")
            iterator = iter(self.items)
            if self.empleado is not None:
                empleado = self.empleado.getNombre()
            else:
                empleado = "Recepcion"
            while True:
                try:
                    servicio = next(iterator)
                    lista.append(servicio.nombre + " \t" + servicio.valor + "\n")
                except StopIteration:
                    break

            sb.append("-------------------------------------------\n")
            sb.append("Codigo de factura: " + str(self.codigo) + "\n")
            sb.append("Fecha y Hora: " + str(self.date) + "\n")
            sb.append("Empleado: " + empleado + "\n")
            sb.append("Cliente: " + self.cliente.getNombre() + "\n")
            sb.append(lista)
            sb.append("Valor total:  " + str(self.valorTotal) + "\n")
            sb.append("-------------------------------------------")
            return ''.join(sb)





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


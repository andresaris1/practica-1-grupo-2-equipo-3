from Servicio import Servicio


class Lugar(Servicio):
    
    def __init__(self,nombre,descripcion,valor,numero,capacidad):
        valor=valor
        super().__init__(nombre, valor, descripcion)
        self._capacidad=capacidad
        self._numero=numero

        #El valor no se ingresa porque es calculado mediante la funcion ValorSegunTipo y el numero de los lugares de eventos es 0 por defecto

    def valorSegunTipo(nombre):
        if nombre == "Habitacion Familiar":
            return 100000
        elif nombre == "Habitacion Doble":
            return 80000
        elif nombre == "Habitacion Individual":
            return 50000
        elif nombre == "Terraza":
            return 200000
        elif nombre == "Piscina":
            return 300000
        elif nombre == "Salon":
            return 500000
        else:
            return -1

    def toString(self):
        return "Habitacion: " + str(self._numero) + " " + str(super().getNombre()) + " con capacidad para " + str(self._capacidad) + " personas"
    

    def setNumero(self, numero):
        self._numero = numero

    def getNumero(self):
        return self._numero

    def setCapacidad(self, capacidad):
        self._capacidad = capacidad

    def getCapacidad(self):
        return self._capacidad
from gestorAplicacion.Servicio import Servicio


class Lugar(Servicio):
    
    def __init__(self,nombre, valor,descripcion, numero,capacidad):
        super().__init__(nombre, valor, descripcion)
        self._numero=0
        self._capacidad=capacidad
        #El valor no se ingresa porque es calculado mediante la funcion ValorSegunTipo y el numero de los lugares de eventos es 0 por defecto


        super().setValor(self.valorSegunTipo(nombre))

    def valorSegunTipo(nombre):
        if nombre == "Habitación familiar":
            return 100000
        elif nombre == "Habitación doble":
            return 80000
        elif nombre == "Habitación individual":
            return 50000
        elif nombre == "Terraza":
            return 200000
        elif nombre == "Piscina":
            return 300000
        elif nombre == "Salon":
            return 500000
        else:
            return -1


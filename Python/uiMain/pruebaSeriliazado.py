import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/modelos"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/reservacion"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../baseDatos"))

if __name__ == '__main__':
    from Empleado import Empleado
    from Usuario import Usuario
    from Factura import Factura
    from Servicio import Servicio
    from Almacenamiento import Almacenamiento


    ser1 = Servicio( "Comida", 10,"dsrfvdfvg")
    ser2 = Servicio( "Limpieza", 10,"dsrfvdfvg")
    ser3 = Servicio( "Piscina", 10,"dsrfvdfvg")
    emo1 = Empleado("Carla", 123456789, 135, "Bar")
    use1 = Usuario( "juan", 6543, 321, "tipo", 678)
    fac1 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")
    fac2 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")
    fac3 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")

    print("PRUEBA DE SERIALIZADO")
    Almacenamiento.Deserializar()

    Almacenamiento.listaUsuarios.append(use1)

    habitacion1 = Almacenamiento.crearHabitacion("101", "Habitacion Individual", 101, 1)
habitacion2 = Almacenamiento.crearHabitacion("102", "Habitacion Individual", 102, 1)
habitacion3 = Almacenamiento.crearHabitacion("201", "Habitacion Doble", 201, 2)
habitacion4 = Almacenamiento.crearHabitacion("202", "Habitacion Doble", 202, 2)
habitacion5 = Almacenamiento.crearHabitacion("301", "Habitacion Familiar", 301, 4)
habitacion6 = Almacenamiento.crearHabitacion("302", "Habitacion Familiar", 302, 4)


    

Almacenamiento.Serializar()
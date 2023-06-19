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


    print("PRUEBA DE SERIALIZADO")
    Almacenamiento.Deserializar()


    habitacion1 = Almacenamiento.crearHabitacion("101", "Habitacion Individual", 101, 1)
    habitacion2 = Almacenamiento.crearHabitacion("102", "Habitacion Individual", 102, 1)
    habitacion3 = Almacenamiento.crearHabitacion("201", "Habitacion Doble", 201, 2)
    habitacion4 = Almacenamiento.crearHabitacion("202", "Habitacion Doble", 202, 2)
    habitacion5 = Almacenamiento.crearHabitacion("301", "Habitacion Familiar", 301, 4)
    habitacion6 = Almacenamiento.crearHabitacion("302", "Habitacion Familiar", 302, 4)

    empleado= Almacenamiento.crearEmpleado("Carlos", 410, 1, "Cocinero")

    #Almacenamiento.Serializar()




        

    Almacenamiento.Serializar()
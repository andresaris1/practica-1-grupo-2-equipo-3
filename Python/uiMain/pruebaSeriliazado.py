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

    empleado1= Almacenamiento.crearEmpleado("Carla",110,1,"Recepcion")
    empleado2= Almacenamiento.crearEmpleado("Lina",120,1,"Recepcion")
    empleado3= Almacenamiento.crearEmpleado("Mario",130,1,"Recepcion")
    empleado4= Almacenamiento.crearEmpleado("Juan",140,1,"Recepcion")

    empleado4= Almacenamiento.crearEmpleado("Luisa",210,1,"Mesero")
    empleado6= Almacenamiento.crearEmpleado("Valentina",220,1,"Mesero")
    empleado7= Almacenamiento.crearEmpleado("Mateo",230,1,"Mesero")
    empleado8= Almacenamiento.crearEmpleado("Jorge",240,1,"Mesero")

    empleado9= Almacenamiento.crearEmpleado("Pedro",310,1,"Cocinero")
    empleado10= Almacenamiento.crearEmpleado("Julian",320,1,"Cocinero")
    empleado11= Almacenamiento.crearEmpleado("Kevin",330,1,"Cocinero")
    empleado12= Almacenamiento.crearEmpleado("Martin",340,1,"Cocinero")

    empleado9= Almacenamiento.crearEmpleado("Camila",410,1,"Bartender")
    empleado10= Almacenamiento.crearEmpleado("Patricia",420,1,"Bartender")
    empleado11= Almacenamiento.crearEmpleado("Paula",430,1,"Bartender")
    empleado12= Almacenamiento.crearEmpleado("Elena",440,1,"Bartender")





    empleado= Almacenamiento.crearEmpleado("Carlos", 410, 1, "Cocinero")

    #Almacenamiento.Serializar()




        

    Almacenamiento.Serializar()
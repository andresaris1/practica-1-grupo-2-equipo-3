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
    fac1 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto1")
    fac2 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto2")
    fac3 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto3")

    print("PRUEBA DE SERIALIZADO")
    Almacenamiento.Deserializar()
    
    empleado1= Almacenamiento.crearEmpleado("Carla",110,1,"Recepcion")
    empleado2= Almacenamiento.crearEmpleado("Lina",120,1,"Recepcion")
    empleado3= Almacenamiento.crearEmpleado("Mario",130,1,"Recepcion")
    empleado4= Almacenamiento.crearEmpleado("Juan",140,1,"Recepcion")

    empleado5= Almacenamiento.crearEmpleado("Luisa",210,1,"Mesero")
    empleado6= Almacenamiento.crearEmpleado("Valentina",220,1,"Mesero")
    empleado7= Almacenamiento.crearEmpleado("Mateo",230,1,"Mesero")
    empleado8= Almacenamiento.crearEmpleado("Jorge",240,1,"Mesero")

    empleado9= Almacenamiento.crearEmpleado("Pedro",310,1,"Cocinero")
    empleado10= Almacenamiento.crearEmpleado("Julian",320,1,"Cocinero")
    empleado11= Almacenamiento.crearEmpleado("Kevin",330,1,"Cocinero")
    empleado12= Almacenamiento.crearEmpleado("Martin",340,1,"Cocinero")
    
    empleado13= Almacenamiento.crearEmpleado("Camila",410,1,"Bartender")
    empleado14= Almacenamiento.crearEmpleado("Patricia",420,1,"Bartender")
    empleado15= Almacenamiento.crearEmpleado("Paula",430,1,"Bartender")
    empleado16= Almacenamiento.crearEmpleado("Elena",440,1,"Bartender")


    for a in Almacenamiento.listaEmpleados:
        print(a.nombre + "   " + str(a.identificacion))

    

    Almacenamiento.Serializar()
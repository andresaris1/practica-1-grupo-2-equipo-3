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
    #Almacenamiento.Deserializar()
    c1 = Usuario("Carlos", "1", "Cliente", "1", "1")

    emp = Empleado("Recepcion", 0, 0, "Recepcion")

    
    masaje = Almacenamiento.crearServicio("Masaje", 30000, "")

    fac1=Almacenamiento.crearFactura(c1, emp, [masaje], "concepto")

    

    Almacenamiento.Serializar()


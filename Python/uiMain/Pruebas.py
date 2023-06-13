import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/modelos"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/reservacion"))

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
    use1 = Usuario( "luis", 6543, 321, "tipo", 678)
    fac1 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")
    fac2 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")
    fac3 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")

    print("PRUEBA DE SERIALIZADO")
    Almacenamiento.Deserializar()

    for usuario in Almacenamiento.listaUsuarios:
        print(usuario.nombre)

    Almacenamiento.listaUsuarios.append(use1)

    Almacenamiento.Serializar()

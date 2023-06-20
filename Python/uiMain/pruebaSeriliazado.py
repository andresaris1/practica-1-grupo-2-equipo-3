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
    '''
    Almacenamiento.crearServicio("Alimentacion", 30000, "descripcion")
    Almacenamiento.crearServicio("Transporte", 15000, "descripcion")
    Almacenamiento.crearServicio("Masaje", 20000, "descripcion")
    

    Almacenamiento.crearLugar("Terraza","descripcion",101,20000)
    Almacenamiento.crearLugar("Salón de Eventos","descripcion",202,20000)
    Almacenamiento.crearLugar("Piscina","descripcion",303,20000)
    '''
    for a in Almacenamiento.listaLugares:
        print(a.nombre)

    

    Almacenamiento.Serializar()
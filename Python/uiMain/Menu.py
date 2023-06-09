import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/modelos"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/reservacion"))

if __name__ == '__main__':
    from Empleado import Empleado
    from Usuario import Usuario
    from Factura import Factura
    from Servicio import Servicio

    print("Prueba de factura")
    ser1 = Servicio( "Comida", 20330,"dsrfvdfvg")
    ser2 = Servicio( "Limpieza", 2123,"dsrfvdfvg")
    ser3 = Servicio( "Piscina", 836,"dsrfvdfvg")
    emo1 = Empleado("Carla", 123456789, 135, "Bar")
    use1 = Usuario( "Kevin", 6543, 321, "tipo", 678)
    fac1 = Factura(use1, emo1, [ser1,ser2,ser3], "concepto")

    print(fac1.valorTotal())
    print("FIN DE PRUEBA FACTURA")

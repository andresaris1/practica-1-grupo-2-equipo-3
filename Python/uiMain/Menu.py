from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Factura import Factura
from gestorAplicacion.Servicio import Servicio
from gestorAplicacion.Usuario import Usuario


if __name__ == '__Menu__':
    print("Prueba de factura")
    ser1 = Servicio( "Cocina", 200,"dsrfvdfvg")
    emo1 = Empleado("Carla", 123456789, 135, "Bar")
    use1 = Usuario( "Kevin", 6543, 321, "tipo", 678)
    fac1 = Factura(use1, emo1, [ser1], [], "concepto")

    fac1.imprimirFactura()
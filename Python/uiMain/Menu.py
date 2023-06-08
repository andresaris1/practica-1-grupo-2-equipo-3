if __name__ == '__Menu__':
    print("dfg")
    from Python.gestorAplicacion.modelos.Empleado import Empleado
    from Python.gestorAplicacion.modelos.Usuario import Usuario
    from Python.gestorAplicacion.reservacion.Factura import Factura
    from Python.gestorAplicacion.reservacion.Servicio import Servicio

    print("Pruebas")


    print("Prueba de factura")
    ser1 = Servicio( "Cocina", 200,"dsrfvdfvg")
    emo1 = Empleado("Carla", 123456789, 135, "Bar")
    use1 = Usuario( "Kevin", 6543, 321, "tipo", 678)
    fac1 = Factura(use1, emo1, [ser1], [], "concepto")

    fac1.imprimirFactura()
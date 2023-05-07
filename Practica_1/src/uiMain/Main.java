package uiMain;

import gestorAplicacion.*;

public class Main {
    public static void main(String[] args) {
        Usuario usuario1 = new Usuario("carlos", 0, 0, null, 0);
        Empleado empleado1 = new Empleado("luis", 0, 0, null, 0);
        Habitacion hab1 = new Habitacion(0, 0, null);
        Servicio ser1 = new Servicio("piscina", 34);

        Factura f1 = new Factura(usuario1, empleado1, new Object[] { hab1, ser1 });
        System.out.println(f1.PrintFactura());
        
    }
}

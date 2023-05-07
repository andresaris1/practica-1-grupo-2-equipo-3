package uiMain;


import gestorAplicacion.*;

public class Main {
  static Usuario usuario1 = new Usuario("carlos", 1234, 0, null, 0);
  static Usuario usuario2 = new Usuario("Maria", 345, 0, null, 0);
  static Usuario usuario3 = new Usuario("Ximena", 763, 0, null, 0);
  static  Usuario usuario4 = new Usuario("Valentin", 2468, 0, null, 0);
  Empleado empleado1 = new Empleado("luis pedro", 0, 0, null, 0, 0);
  Habitacion hab1 = new Habitacion(0, 0, null, 0);
  Servicio ser1 = new Servicio("piscina", 34);
  Factura f1 = new Factura(usuario1, empleado1, new Servicio[] { hab1, ser1 });

public static  Usuario[] ListaUsuarios = {usuario1,usuario2,usuario3,usuario4};

}


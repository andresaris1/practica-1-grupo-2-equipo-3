package gestorAplicacion;


public class Main {
    public static void main(String[] args) {

        Usuario usuario1 = new Usuario("carlos", 0, 0, null, 0);
        Empleado empleado1 = new Empleado("luis", 0, 0, null, 0);
        Factura f1 = new Factura(123, 345, 1205, usuario1, empleado1, null, 0);

        System.out.print(f1.toString());
    }
}

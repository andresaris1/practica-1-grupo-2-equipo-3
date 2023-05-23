package gestorAplicacion;

/*Clase Empleado hereda de Persona los atributos nombre, identificacion y telefono*/

public class Empleado extends Persona {

    private String cargo;
    private double comision;
    private final int nomina=560000; // Valor prestablecido para cada uno de los empleados

    // METODOS
    /*
     * Metod sobreescrito de Persona que devuelve la impormacion mas importante el
     * empleado
     */
    @Override
    public String informacion() {
        return ("Nombre: " + this.getNombre() + "\n" +
                "Documento: " + this.getIdentificacion() + "\n" +
                "Cargo: " + this.getCargo() +
                "Nomina: " + this.getNomina() + "\n");
    }

    /*
     * Metodo calcularComision se encarga de modificar la comision de cada empleado
     * en funcion de
     * sus ventas, cada que se realiza una factura a su nombre y recibe por paramtro
     * valor total de dicha factura
     */
    public void calcularComision(int valorPagado) {
        double x = 0.02 * valorPagado;
        this.comision = +x;
    }

    // CONSTRUCTOR
    public Empleado(String nombre, int identificacion, int telefono, String cargo, int comision, int nomina) {
        super(nombre, identificacion, telefono);
        this.cargo = cargo;
        this.comision = comision;
    }

    // GETTERS AND SETTERS
    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public double getComision() {
        return comision;
    }

    public void setComision(double comision) {
        this.comision = comision;
    }

    public int getNomina() {
        return nomina;
    }


}

package gestorAplicacion;

//crear una clase abstracta llamada persona que tenga los atributos abstractos nombrey valor, ademas que tenga un metodo abstracto llamado obtener

public class Empleado extends Persona {
    private String cargo;
    private double comision;
    private int nomina; // Valor prestablecido

    // METODOS
    @Override
    public String obtenerInformacion() {
        return "Empleado " + nombre;
    }

    public void calcularComision(int valorPagado){
        double x=0.02*valorPagado;
        this.comision=+x;
    }

    // CONSTRUCTOR
    public Empleado(String nombre, int identificacion, int telefono, String cargo, int comision, int nomina) {
        super(nombre, identificacion, telefono);
        this.cargo = cargo;
        this.comision = comision;
        this.nomina = nomina;
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

    public void setNomina(int nomina) {
        this.nomina = nomina;
    }

}

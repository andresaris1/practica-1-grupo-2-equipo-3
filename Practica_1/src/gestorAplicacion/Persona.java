package gestorAplicacion;

abstract public class Persona {
    protected String nombre;
    protected int identificacion;
    protected int telefono;

    // METODOS

    public abstract String obtenerInformacion();

    // CONSTRUCTOR
    public Persona(String nombre, int identificacion, int telefono) {
        this.nombre = nombre;
        this.identificacion = identificacion;
        this.telefono = telefono;
    }

    // GETTERS AND SETTERS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(int identificacion) {
        this.identificacion = identificacion;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

}

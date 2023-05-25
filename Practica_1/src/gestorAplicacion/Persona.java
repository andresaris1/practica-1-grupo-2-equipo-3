package gestorAplicacion;

import java.io.Serializable;

/*Clase  abstracta creada para la herencia de Usuario y empleado*/
abstract public class Persona implements Serializable{
private static final long serialVersionUID = 1L;
    protected String nombre;
    protected int identificacion;
    protected int telefono;

    // METODOS
    /* Metodo a heredar que muestra la imformacion importante del objeto */
    public abstract String informacion();

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

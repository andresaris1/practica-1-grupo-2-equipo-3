package gestorAplicacion;

import java.io.Serializable;

/*Clase Servio se usa para crear los diferentes servicios que puedo reserva un cliente (comida,masajes)*/
public class Servicio implements Serializable {
    private static final long serialVersionUID = 1L;

    protected String nombre;
    protected int valor;

    //METODOS
    @Override
    public String toString() {
        return (this.nombre+"--------"+this.valor);
    }

    //CONSTRUCTOR
	public Servicio(String nombre, int valor) {
		this.nombre = nombre;
		this.valor = valor;
    }

    //GETTERS AND SETTERS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getValor() {
        return this.valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }

    

    
    
}

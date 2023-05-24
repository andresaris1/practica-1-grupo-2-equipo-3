package gestorAplicacion;

import java.io.Serializable;

/*Clase lugar hereda de servicio y se usa para crear los diferentes lugares ofrecidos(habitaciones y zonas sociales) */
public class Lugar extends Servicio {
    int numero;
    String tipo;
    int capacidad;

    // METODOS

    /*
     * Metodo encargado de consultar el valor de una habitacion segun el tipo que es
     * ingresado como parametro
     */
    public static int valorSegunTipo(String tipo) {
        if (tipo.equals("Habitación familiar")) {
            return 100000;
        } else if (tipo.equals("Habitación doble")) {
            return 80000;
        } else if (tipo.equals("Habitación individual")) {
            return 50000;
        } else if (tipo == "Terraza") {
            return 200000;
        } else if (tipo == "Piscina") {
            return 300000;
        } else if (tipo == "Salon") {
            return 500000;
        } else {
            return -1;
        }
    }

    /*
     * Metodo toString imprime toda la impormacion importante de la habitacion sobre
     * la que se ejecute el metodo
     */
    public String toString() {
        return "Habitacion: " + numero + " " + tipo + " con capacidad para " + capacidad + " personas";
    }

	// CONSTRUCTORES

    /*
     * Constructor para habitaciones
     * tipos: Habitación familiar, Habitación doble, Habitación individual
     */
    public Lugar(int numero, String tipo, int capacidad) {
        super("Habitacion " + tipo, valorSegunTipo(tipo));
        this.numero = numero;
        this.tipo = tipo;
        this.capacidad = capacidad;
    }

    /*
     * Constructor para Salas de eventos
     * tipos: Terraza, Piscina, Salon
     */

    public Lugar(String tipo) {
        super(tipo, valorSegunTipo(tipo));
        this.tipo = tipo;
    }

    // GETTERS AND SETTERS
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(int capacidad) {
        this.capacidad = capacidad;
    }

}
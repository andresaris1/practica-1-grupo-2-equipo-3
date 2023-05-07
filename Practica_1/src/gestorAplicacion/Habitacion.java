package gestorAplicacion;

public class Habitacion extends Servicio {
    int numero;
    String tipo;
    int capacidad;


    //METODOS

    //verificar disponibilidad

    //CONTRUCTOR
    public Habitacion(int valor, int numero, String tipo, int capacidad) {
        super("Habitacion "+tipo, valor);
        this.numero = numero;
        this.tipo = tipo;
        this.capacidad = capacidad;
    }

    //GETTERS AND SETTERS
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
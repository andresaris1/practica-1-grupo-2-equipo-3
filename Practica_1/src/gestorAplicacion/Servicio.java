package gestorAplicacion;

public class Servicio {
    
    //clase para los servicios adicionales(jacuzzi, lavado de ropa,etc)

    String nombre;
    int Valor;

    //CONSTRUCTOR
    public Servicio(String nombre, int valor) {
        this.nombre = nombre;
        Valor = valor;
    }

    //GETTERS AND SETTERS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getValor() {
        return Valor;
    }

    public void setValor(int valor) {
        Valor = valor;
    }

    

    
    
}

package gestorAplicacion;

public class Habitacion {
    int numero;
    String tipo;
    int valor;
    String nombre;

    //CONSTRUCTOR
    public Habitacion(int numero, String tipo, int valor) {
        this.numero = numero;
        this.tipo = tipo;
        this.valor = valor;
        this.nombre = "Habitacion"+tipo;
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

    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
}

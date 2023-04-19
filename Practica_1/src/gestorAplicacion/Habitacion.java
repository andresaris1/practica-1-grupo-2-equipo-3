package gestorAplicacion;

public class Habitacion {
    String nombre;
    int valor;
    int numero;
    String tipo;

    //METODOS

    //CONTRUCTOR
    public Habitacion(int valor, int numero, String tipo) {
        this.valor = valor;
        this.numero = numero;
        this.tipo = tipo;
        this.nombre="Habitacion"+this.tipo;
    }

    //GETTERS AND SETTERS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }

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

    

}
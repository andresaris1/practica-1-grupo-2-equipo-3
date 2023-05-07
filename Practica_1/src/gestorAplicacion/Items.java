package gestorAplicacion;

//Clse de caul geredan habitacion y servicio

abstract public class Items {
    String nombre;
    int valor;

    abstract public {}
    
    public String toString() {
        return (this.nombre+"--------"+this.valor);
    }
    
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

    
    
}

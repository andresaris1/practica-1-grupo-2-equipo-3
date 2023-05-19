package gestorAplicacion;

public class ServicioExterno extends Servicio {
    String nombre;
    int valor;
    String empresaContratada;
    String descripcion;

    @Override
    public String toString() {
        return("Servicio de "+ this.nombre +" contratado con la empresa "
        + this.empresaContratada +" por un valor de "+this.valor+" COP"  );
    }


    ServicioExterno(String nombre, int valor, String empresaContratada) {
        super(nombre, valor);
        this.empresaContratada = empresaContratada;
    }

    //Getters y setters
    public String getEmpresaContratada() {
        return empresaContratada;
    }
    public void setEmpresaContratada(String empresaContratada) {
        this.empresaContratada = empresaContratada;
    }

    public String getDescripcion(){
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}

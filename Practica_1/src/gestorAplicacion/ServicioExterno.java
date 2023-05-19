package gestorAplicacion;

public class ServicioExterno extends Servicio {
    String nombre;
    int valor;
    String empresaContratada;

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
}

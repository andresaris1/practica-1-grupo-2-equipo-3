package gestorAplicacion;




import gestorAplicacion.*;
import java.util.ArrayList;



public class Evento extends Servicio{
    //ATRIBUTOS
    private Lugar lugar;
    private Usuario cliente;
    private ServicioExterno[] servicios;
    private String fecha;
    private int duracion;
    private int numeroAsistentes;

    //Constructor
    public Evento(Lugar lugar, Usuario Cliente, ServicioExterno[] servicios, String fecha, int duracion, int numeroAsistentes) {
        super("Evento en "+lugar, calcularValor(lugar, servicios, duracion, numeroAsistentes));
        this.lugar = lugar;
    }

    //Métodos relevantes -----------------------------------------------------
    public static int calcularValor(Lugar lugar, ServicioExterno[] servicios, int duracion, int numeroAsistentes)
    {
        int valor = 0;
        valor += lugar.getValor();
        for (ServicioExterno servicioExterno : servicios) {
            valor += servicioExterno.getValor();
        }
        valor += duracion*10000;
        valor += numeroAsistentes*10000;
        return valor;
    }

    

    //-----------------------------------------------
    //GETTERS AND SETTERS
    public Lugar getLugar() {
        return lugar;
    }

    public void setLugar(Lugar lugar) {
        this.lugar = lugar;
        this.setNombre("Evento en "+lugar.getNombre());
    }

    public Usuario getCliente() {
        return cliente;
    }

    public void setCliente(Usuario cliente) {
        this.cliente = cliente;
        this.setNombre("Evento de "+cliente.getNombre());
    }

    public ServicioExterno[] getServicios() {
        return servicios;
    }

    public void setServicios(ServicioExterno[] servicios) {
        this.servicios = servicios;
    }

    //getter fecha
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha){
        this.fecha = fecha;
    }

    public int getDuracion(){
        return duracion;
    }

    public void setDuracion(int duracion){
        this.duracion = duracion;
    }

    public int getNumeroAsistentes(){
        return numeroAsistentes;
    }

    public void setNumeroAsistentes(int numeroAsistentes){
        this.numeroAsistentes = numeroAsistentes;
    }


    //otros getters no tan obvios
    public ArrayList<String> getEmpresasContratadas(){
        ArrayList<String> lista = new ArrayList<String>();
    
        for (ServicioExterno servicio: servicios)
        {
            lista.add(servicio.getEmpresaContratada()); 
        }

        return lista;
    }
}

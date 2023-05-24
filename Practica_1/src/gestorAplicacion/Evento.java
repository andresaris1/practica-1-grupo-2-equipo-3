package gestorAplicacion;

import java.util.ArrayList;

/*
 * Clase Evento encargada de crear los eventos, los cuales son un tipo de servicio
 * que se le ofrece a los clientes, estos eventos pueden ser de diferentes tipos,
 * como por ejemplo: bodas, cumpleaños, fiestas, etc.
 * El evento puede usar diferentes servicios externos, como por ejemplo:
 * Sonido, Entretenimiento, etc.
 * El evento también puede realizarse en distintos lugares del Hotel:
 * Piscina, Salón, Terraza.
 * 
 */
public class Evento extends Servicio {
    // ATRIBUTOS
    private Lugar lugar;
    private Usuario cliente;
    private ArrayList<ServicioExterno> servicios;
    private String fecha;
    private int duracion;
    private int numeroAsistentes;
    private ArrayList<Empleado> empleados;

    // CONSTRUCTOR
    public Evento(Lugar lugar, Usuario cliente, ArrayList<ServicioExterno> servicios, String fecha, int duracion,
            int numeroAsistentes, ArrayList<Empleado> empleados) {
        super("Evento en " + lugar, calcularValor(lugar, servicios, duracion, numeroAsistentes));
        this.lugar = lugar;
        this.cliente = cliente;
        this.servicios = servicios;
        this.duracion = duracion;
        this.numeroAsistentes = numeroAsistentes;
        this.empleados = empleados;
    }

    // Métodos relevantes -----------------------------------------------------
    /*
     * Este método se encarga de calcular el valor monetario de un evento.
     * Este valor lo calcula sumando el valor del lugar en el que se realizará, el
     * valor individual
     * de cada uno de los servicios externos que se contrataron, la duración del
     * evento
     * y los asistentes a este.
     */
    public static int calcularValor(Lugar lugar, ArrayList<ServicioExterno> servicios, int duracion, int numeroAsistentes) {
        int valor = 0;
        valor += lugar.getValor();
        for (ServicioExterno servicioExterno : servicios) {
            valor += servicioExterno.getValor();
        }
        valor += duracion * 10000;
        valor += numeroAsistentes * 10000;
        return valor;
    }

    // -----------------------------------------------
    // GETTERS AND SETTERS
    public Lugar getLugar() {
        return lugar;
    }

    public void setLugar(Lugar lugar) {
        this.lugar = lugar;
        this.setNombre("Evento en " + lugar.getNombre());
    }

    public Usuario getCliente() {
        return cliente;
    }

    public void setCliente(Usuario cliente) {
        this.cliente = cliente;
        this.setNombre("Evento de " + cliente.getNombre());
    }

    public ArrayList<ServicioExterno> getServicios() {
        return servicios;
    }

    public void setServicios(ArrayList<ServicioExterno> servicios) {
        this.servicios = servicios;
    }

    // getter fecha
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public int getNumeroAsistentes() {
        return numeroAsistentes;
    }

    public void setNumeroAsistentes(int numeroAsistentes) {
        this.numeroAsistentes = numeroAsistentes;
    }
    
    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }

    // otros getters no tan obvios
    /*
     * Este método se encarga de retornar un ArrayList con los nombres de cada una
     * de las
     * empresas externas cuyos servicios fueron contratados para el evento.
     */
    public ArrayList<String> getEmpresasContratadas() {
        ArrayList<String> lista = new ArrayList<String>();

        for (ServicioExterno servicio : servicios) {
            lista.add(servicio.getEmpresaContratada());
        }

        return lista;
    }
}

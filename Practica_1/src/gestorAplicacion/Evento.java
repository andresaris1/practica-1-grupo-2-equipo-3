package gestorAplicacion;

import gestorAplicacion.*;

public class Evento extends Servicio{
    //ATRIBUTOS
    private Lugar lugar;
    private Usuario cliente;
    private ServicioExterno[] servicios;
    private String fecha;
    private int duracion;
    private int numeroAsistentes;

    //METODOS
    public Evento(Lugar lugar, Usuario Cliente, ServicioExterno[] servicios, String fecha, int duracion, int numeroAsistentes) {
        super("Evento en "+lugar, calcularValor(lugar, servicios, duracion, numeroAsistentes));
        this.lugar = lugar;
    }
}

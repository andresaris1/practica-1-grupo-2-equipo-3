package gestorAplicacion;

import java.util.ArrayList;



/*
 * Esta clase es la encargada de crear los eventos, los cuales son un tipo de servicio
 * que se le ofrece a los clientes, estos eventos pueden ser de diferentes tipos,
 * como por ejemplo: bodas, cumpleaños, fiestas, etc.
 * El evento puede usar diferentes servicios externos, como por ejemplo:
 * Sonido, Entretenimiento, etc.
 * El evento también puede realizarse en distintos lugares del Hotel:
 * Piscina, Salón, Terraza.
 * 
 */
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
    /*
     * Este método se encarga de calcular el valor monetario de un evento.
     * Este valor lo calcula sumando el valor del lugar en el que se realizará, el valor individual
     * de cada uno de los servicios externos que se contrataron, la duración del evento
     * y los asistentes a este.
     */
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

    

    //otros getters no tan obvios
    /*
     * Este método se encarga de retornar un ArrayList con los nombres de cada una de las
     * empresas externas cuyos servicios fueron contratados para el evento.
     */
    public ArrayList<String> getEmpresasContratadas(){
        ArrayList<String> lista = new ArrayList<String>();
    
        for (ServicioExterno servicio: servicios)
        {
            lista.add(servicio.getEmpresaContratada()); 
        }

        return lista;
    }
}

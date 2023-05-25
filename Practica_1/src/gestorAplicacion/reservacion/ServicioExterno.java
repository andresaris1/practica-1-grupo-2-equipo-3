package gestorAplicacion.reservacion;




import gestorAplicacion.modelos.*;



/*
 * Clase ServicioExterno encargada de crear los servicios externos que se le ofrecen
 * a los clientes dentro de la reserva de eventos.
 * Estos servicios externos pueden ser de diferentes tipos,
 * como por ejemplo: Sonido, Entretenimiento, Decoración, etc.
 * 
 */
public class ServicioExterno extends Servicio {


    //ATRIBUTOS
    private int valor;
    private String empresaContratada;
    private String descripcion;
    private Usuario cliente;


    //toString del ServicioExterno
    @Override
    public String toString() {
        return("Servicio de "+ this.nombre +" contratado con la empresa "
        + this.empresaContratada +" por un valor de "+this.valor+" COP"  );
    }

    

    //CONSTRUCTORES

    /*
     * Constructor con descripción
     */
    public ServicioExterno(String nombre, Usuario cliente, String descripcion) {
        super(nombre, valorSegunTipo(nombre));
        this.empresaContratada = empresaSegunTipo(nombre);
        this.descripcion = descripcion;
        this.cliente = cliente;
    }


    /*
     * Constructor sin descripción
     */
    public ServicioExterno(String nombre, Usuario cliente) {
        this(nombre, cliente, null);
    }




    //MÉTODOS
    /*
     * Este método se encargará de calcular el valor monetario de un servicio
     * externo en función de el tipo de servicio externo que sea.
     */
    private static int valorSegunTipo(String nombre){
        if(nombre.equals("entretenimiento")){
            return 100000;
        }else if (nombre.equals("sonido")){
            return 50000;
        }else if (nombre.equals("decoracion")){
            return 200000;
        }else{return -1;}
    }


    /*
     * Este método se encargará de designar la empresa que se contratará en función
     * del tipo de servicio externo que sea.
     */
    private static String empresaSegunTipo(String nombre){
        if(nombre.equals("entretenimiento")){
            return "Entretenimiento S.A.S";
        }else if (nombre.equals("sonido")){
            return "Sonido S.A.S";
        }else if (nombre.equals("decoracion")){
            return "Decoracion S.A.S";
        }else{return null;}
    }








    //GETTERS Y SETTERS
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


    public Usuario getCliente() {
        return cliente;
    }

    public void setCliente(Usuario cliente) {
        this.cliente= cliente;
    }
}

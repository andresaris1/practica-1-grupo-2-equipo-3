package gestorAplicacion;

public class ServicioExterno extends Servicio {
    int valor;
    String empresaContratada;
    String descripcion;

    @Override
    public String toString() {
        return("Servicio de "+ this.nombre +" contratado con la empresa "
        + this.empresaContratada +" por un valor de "+this.valor+" COP"  );
    }

    

    public ServicioExterno(String nombre, String descripcion) {
        super(nombre, valorSegunTipo(nombre));
        this.empresaContratada = empresaSegunTipo(nombre);
        this.descripcion = descripcion;
    }

    private static int valorSegunTipo(String nombre){
        if(nombre.equals("entretenimiento")){
            return 100000;
        }else if (nombre.equals("sonido")){
            return 50000;
        }else if (nombre.equals("decoracion")){
            return 200000;
        }else{return -1;}
    }
    private static String empresaSegunTipo(String nombre){
        if(nombre.equals("entretenimiento")){
            return "Entretenimiento S.A.S";
        }else if (nombre.equals("sonido")){
            return "Sonido S.A.S";
        }else if (nombre.equals("decoracion")){
            return "Decoracion S.A.S";
        }else{return null;}
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

package gestorAplicacion;

import java.util.ArrayList;

public class Usuario extends Persona {
    String tipo;
    int cuentaBancaria;
    ArrayList<Factura> listaFacturas;
    
    //METODOS

    @Override
    public String obtenerInformacion() {
        return "d";
    }

    //CONSTRUCTOR
    public Usuario(String nombre, int identificacion, int telefono, String tipo, int cuentaBancaria) {
        super(nombre, identificacion, telefono);
        this.tipo = tipo;
        this.cuentaBancaria = cuentaBancaria;
    }

    //GETTERS AND SETTERS
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getCuentaBancaria() {
        return cuentaBancaria;
    }

    public void setCuentaBancaria(int cuentaBancaria) {
        this.cuentaBancaria = cuentaBancaria;
    }

    public ArrayList<Factura> getListaFacturas() {
        return listaFacturas;
    }

    public void setListaFacturas(ArrayList<Factura> listaFacturas) {
        this.listaFacturas = listaFacturas;
    }



    


    
}

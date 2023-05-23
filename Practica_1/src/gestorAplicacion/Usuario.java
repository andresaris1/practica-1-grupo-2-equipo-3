package gestorAplicacion;
/*Clase Usuario se usa para crear los clientes que realizen reservas en el hotel */

import java.util.ArrayList;

public class Usuario extends Persona {
    String tipo;
    ArrayList<Factura> listaFacturas;

    // METODOS

    /*
     * Metod sobreescrito de Persona que devuelve la impormacion mas importante el
     * usurio
     */
    @Override
    public String informacion() {
        return ("Nombre: " + this.getNombre() + "\n" +
                "Telefono: " + this.getTelefono() + "\n" +
                "Documento: " + this.getIdentificacion() + "\n");
    }

    // CONSTRUCTOR
    public Usuario(String nombre, int identificacion, int telefono, String tipo) {
        super(nombre, identificacion, telefono);
        this.tipo = tipo;
    }

    // GETTERS AND SETTERS
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public ArrayList<Factura> getListaFacturas() {
        return listaFacturas;
    }

    public void setListaFacturas(ArrayList<Factura> listaFacturas) {
        this.listaFacturas = listaFacturas;
    }

}

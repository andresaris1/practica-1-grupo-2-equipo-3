package gestorAplicacion;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.ArrayList;

public class Factura {
    private int codigo;
    private String date;
    private Usuario cliente;
    private Empleado empleado;
    private Servicio[] items;
    private int valorTotal;
    private int estado; // 0 Deudo 1 Pago
    static int contador = 0;

    // METODOS

    /*Metodo generarFactura se encarga de crear las facturas ademas de almacenar 
    la misma en la lista de cada cliente, recibe como parametro objetos de tipo 
    usuario, empleado y una array con los servicios escogidos--
     */
    public void generarFactura(Usuario cliente, Empleado empleado, Servicio[] items){
        
        
    }

    // Met RealizarCobro con sobrecarga de la opcion efectivo y tarjeta
    // Met CobrarDeuda
    // Metodo para imprimir codigos
    


    /*
     * Metodo para sumar el valor total que debe un cliente, recibe como parametro
     * un objeto de tipo usuario y regresa en entero el valor total de la deuda
     */
    public int sumarDeuda(Usuario user) {
        int valorDeuda = 0;
        for (int i = 0; i < user.listaFacturas.size(); i++) {
            if (user.listaFacturas.get(i).getEstado() == 0) {
                valorDeuda = +user.listaFacturas.get(i).getValorTotal();
            }
        }
        return valorDeuda;
    }

    /*
     * Metodo FacturasEnDeuda se encarga de recopilar totas las facturas no pagas de
     * un cliente
     * recibe como parametro usuario y regresa un array con todas las facturas no
     * pagas
     */
    public ArrayList<Factura> facturasEnDeuda(Usuario user) {
        ArrayList<Factura> facturasDeudas = new ArrayList<Factura>();
        for (Factura factura : user.listaFacturas) {
            if (factura.getEstado() == 0) {
                facturasDeudas.add(factura);
            }
        }
        return facturasDeudas;
    }

    /* Metodo que calcula el valor o precio total de cada factura */
    public void valorTotal() {
        int total = 0;

        for (int i = 0; i < items.length; i++) {
            int x = items[i].getValor();
            total = +x;
        }
        this.valorTotal = total;
    }

    /*
     * Metodo imprimir factura se engarda de imprimir la imformacion principal
     * de la factura con formato de interfaz
     */
    public String imprimirFactura() {

        String lista = "";
        for (int i = 0; i < items.length; i++) {
            String cadena = items[i].toString();
            lista = lista + cadena + "\n";
        }

        String PrintFactura = ("-------------------------------------------" + "\n" +
                "Codigo de factura: " + this.codigo + "\n" +
                "Fecha y Hora: " + this.date + "\n" +
                "Empleado: " + this.empleado.getNombre() + "\n" +
                "Cliente: " + this.cliente.getNombre() + "\n" +

                "Cosa                        Valor" + "\n" +
                lista + "\n" +
                "Valor total:  " + valorTotal + "\n" +

                "-------------------------------------------");

        return PrintFactura;
    }

    // CONSTRUCTOR
    public Factura(Usuario cliente, Empleado empleado, Servicio[] items) {
        this.cliente = cliente;
        this.empleado = empleado;
        this.items = items;

        DateFormat dateFormat = new SimpleDateFormat("d MMM yyyy, HH:mm:ss ");
        this.date = dateFormat.format(new Date());

        Factura.contador = +1;
        this.codigo = Factura.contador;

    }

    // GETERS AND SETTERS
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Usuario getCliente() {
        return cliente;
    }

    public void setCliente(Usuario cliente) {
        this.cliente = cliente;
    }

    public Empleado getEmpleado() {
        return empleado;
    }

    public void setEmpleado(Empleado empleado) {
        this.empleado = empleado;
    }

    public int getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(int valorTotal) {
        this.valorTotal = valorTotal;
    }

    public Servicio[] getItems() {
        return items;
    }

    public void setItems(Servicio[] items) {
        this.items = items;
    }

    public static int getContador() {
        return contador;
    }

    public static void setContador(int contador) {
        Factura.contador = contador;
    }

    public int getEstado() {
        return estado;
    }

    public void setEstado(int estado) {
        this.estado = estado;
    }

}

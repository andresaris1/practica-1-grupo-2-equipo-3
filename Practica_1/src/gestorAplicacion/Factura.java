package gestorAplicacion;

import java.util.ArrayList;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Factura {
    int codigo;
    String date;
    Usuario cliente;
    Empleado empleado;
    Object[] items;
    int valorTotal;
    static int contador = 0;

    // METODOS
    public String toString() {
        ArrayList elementos = new ArrayList();

        for(int i = 0;i<=this.items.length;i++){
            String a=items

            
        }



        String PrintFactura = 
        ("-------------------------------------------" + "\n" +
        "Codigo de factura: " + this.codigo + "\n" +
        "Fecha y Hora: " + this.date + "\n" +
        "Empleado: " + this.empleado.getNombre() + "\n" +
        "Cliente: " + this.cliente.getNombre() + "\n" +

        "Cosa                        Valor" + "\n" +

        "-------------------------------------------");

        return PrintFactura;

    }

    int calcularTotal(){
        return codigo;
        
    }

    public Factura(Usuario cliente, Empleado empleado, Object[] items) {
        this.cliente = cliente;
        this.empleado = empleado;
        this.items = items;

        DateFormat dateFormat = new SimpleDateFormat("d MMM yyyy, HH:mm:ss ");
        this.date = dateFormat.format(new Date());

        Factura.contador = +1;
        this.codigo = this.contador;

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

    public Object[] getItems() {
        return items;
    }

    public void setItems(Object[] items) {
        this.items = items;
    }

    public static int getContador() {
        return contador;
    }

    public static void setContador(int contador) {
        Factura.contador = contador;
    }

}

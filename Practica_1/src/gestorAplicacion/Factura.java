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
    ArrayList items;
    int valorTotal;

    public String toString(){
        String PrintFactura=(
            "-------------------"+"\n"+
            "Codigode factura: "+this.codigo+"\n"+
            "Fecha y Hora: "+this.date+"\n"+
            "Empleado: "+this.empleado.getNombre()+"\n"+
            "-------------------"+"\n"+
            "Cliente: "+this.cliente.getNombre()
        );


        
        return PrintFactura;
        
    }

    //CONTRUCTOR
    public Factura(int codigo, Usuario cliente, Empleado empleado, ArrayList items,
            int valorTotal) {
        this.codigo = codigo;
        this.cliente = cliente;
        this.empleado = empleado;
        this.items = items;
        this.valorTotal = valorTotal;

        DateFormat dateFormat = new SimpleDateFormat("d MMM yyyy, HH:mm:ss ");
        this.date = dateFormat.format(new Date());
    }

    //GETERS AND SETTERS
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
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

    public ArrayList getItems() {
        return items;
    }

    public void setItems(ArrayList items) {
        this.items = items;
    }

    public int getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(int valorTotal) {
        this.valorTotal = valorTotal;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    
}

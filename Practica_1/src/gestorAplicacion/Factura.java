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
    private Destinos destino;

    // METODOS

    /*
     * Metodo generarFactura se encarga de crear las facturas ademas de almacenar
     * la misma en la lista de cada cliente, recibe como parametro objetos de tipo
     * usuario, empleado y una array con los servicios escogidos--
     */
    public void generarFactura(Usuario cliente, Empleado empleado, Servicio[] items) {
        int x = Factura.contador + 1;
        String name = "Fac" + Integer.toString(x);
        
        // Encontrar la manera que todos los objetos queden con nombre diferente??
    }

    /* Metodo que calcula el valor o precio total de cada factura */
    public void valorTotal() {
        int total = 0;

        for (int i = 0; i < items.length; i++) {
            int x = items[i].getValor();
            total += x;
        }
        this.valorTotal = total;
    }

    // Metodo para imprimir codigos

    /*
     * Metodo para sumar el valor total que debe un cliente, recibe como parametro
     * un objeto de tipo usuario y regresa en entero el valor total de la deuda
     */
    static public int sumarDeuda(Usuario user) {
        int valorDeuda = 0;
        for (int i = 0; i < user.listaFacturas.size(); i++) {
            if (user.listaFacturas.get(i).getEstado() == 0) {
                valorDeuda += user.listaFacturas.get(i).getValorTotal();
            }
        }
        return valorDeuda;
    }

    /*
     * Metodo FacturasEnDeuda se encarga de recopilar totas las facturas no pagas de
     * un cliente recibe como parametro usuario y regresa un array con todas las
     * facturas no pagas
     */
    static public ArrayList<Factura> facturasEnDeuda(Usuario user) {
        ArrayList<Factura> facturasDeudas = new ArrayList<Factura>();
        for (Factura factura : user.listaFacturas) {
            if (factura.getEstado() == 0) {
                facturasDeudas.add(factura);
            }
        }
        return facturasDeudas;
    }

    /*
     * Metodo realizarCobro realizar el cobro mediante Efectivo de la factura que
     * recibe por parametro
     */
    static public int realizarCobro(Factura factura, int valorIngresado) {
        int vuelto = valorIngresado - factura.getValorTotal();
        factura.setEstado(1);
        factura.getEmpleado().calcularComision(factura.getValorTotal());
        return vuelto;
    }
//en pruebas
    public static int realizarCobro(ArrayList<Factura> facturasDeudas, int valorIngresado) {
        for (Factura factura : facturasDeudas) {
            int vuelto = Factura.realizarCobro(factura, valorIngresado);
            
            valorIngresado = vuelto;
            System.out.println(valorIngresado);
            System.out.println(vuelto);
        
        }
        return 2;
    }

    /*
     * Metodo imprimirFactura se encarga de imprimir la imformacion principal
     * de la factura con formato de interfaz
     */
    public String imprimirFactura() {
        StringBuilder sb = new StringBuilder();
        String lista = "";
        for (int i = 0; i < items.length; i++) {
            String cadena = items[i].toString();
            lista = lista + cadena + "\n";
        }

        sb.append("-------------------------------------------").append("\n");
        sb.append("Codigo de factura: ").append(this.codigo).append("\n");
        sb.append("Fecha y Hora: ").append(this.date).append("\n");
        sb.append("Empleado: ").append(this.empleado.getNombre()).append("\n");
        sb.append("Cliente: ").append(this.cliente.getNombre()).append("\n");
        sb.append("Cosa                        Valor").append("\n");
        sb.append(lista).append("\n");
        sb.append("Valor total:  ").append(valorTotal).append("\n");
        sb.append("-------------------------------------------");

        return sb.toString();
    }

    //Metodo imrpimir codigos
    static public String imprimirCodigos(ArrayList<Factura> facturas) {
        StringBuilder sb = new StringBuilder();
        for (Factura factura : facturas) {
            String x = Integer.toString(factura.getCodigo());
            sb.append(x);
        }
        return sb.toString();
    }

    // CONSTRUCTOR
    public Factura(Usuario cliente, Empleado empleado, Servicio[] items, Destinos destino) {
        this.cliente = cliente;
        this.empleado = empleado;
        this.items = items;
        this.destino = destino;

        DateFormat dateFormat = new SimpleDateFormat("d MMM yyyy, HH:mm:ss ");
        this.date = dateFormat.format(new Date());

        Factura.contador += 1;
        this.codigo = Factura.contador;
    }

    // GETTERS AND SETTERS
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
    
    public Destinos getDestino() {
        return destino;
    }

    public void setDestino(Destinos destino) {
        this.destino = destino;
    }

}

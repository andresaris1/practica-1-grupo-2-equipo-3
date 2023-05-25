package gestorAplicacion;

import java.io.Serializable;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

/*Clase Factura encargada de gaurdar cada una de las compras de los usurios, cada que un usrurio realiza 
la compra o contato de un servicio diferente ser realiza una factura diferente gestionar los cobros */

public class Factura implements Serializable {
	private int codigo;
	private String date;
	private Usuario cliente;
	private Empleado empleado;
	private List<Servicio> items;
	private int valorTotal;
	private int estado; // 0 Deuda 1 Paga
	static int contador = 0;
	private List<Destinos> destino;
	private String concepto;

	// METODOS

	/* Metodo valorTotal se encarga de calcula el valor total de cada factura */
	public void valorTotal() {
		int total = 0;
		Iterator<Servicio> iterator = items.iterator();
		while (iterator.hasNext()) {
			Servicio servicio = (Servicio) iterator.next();
			total += (servicio.valor);
		}
		this.valorTotal = total;
	}

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
	 * Metodo realizarCobro realizar el cobro mediante Efectivo, recibe como
	 * parametro la factura a pagar y el valor del dinero ingresado por el usurio
	 */
	static public int realizarCobro(Factura factura, int valorIngresado) {
		int vuelto = valorIngresado - factura.getValorTotal();
		factura.setEstado(1);
		factura.getEmpleado().calcularComision(factura.getValorTotal());
		return vuelto;
	}

	/*
	 * Segundo metodo realizarCobro recibe como parametro la lista de facturas
	 * deudas por un usuario mas el dinero ingresado y se encarga de cancelar cada
	 * un de esta
	 */
	// Esta en pruebas
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
	 * Metodo imprimirFactura se encarga de imprimir la informacion principal de la
	 * factura con formato entendible por el usuario
	 */
	public String imprimirFactura() {
		StringBuilder sb = new StringBuilder();
		StringBuffer lista = new StringBuffer();
		String empleado = "";
		lista.append("Concepto \t Valor\n");
		Iterator<Servicio> iterator = items.iterator();
		if (this.empleado != null) {
			empleado = this.empleado.getNombre();
		} else {
			empleado = "Recepcion";
		}
		while (iterator.hasNext()) {
			Servicio servicio = (Servicio) iterator.next();
			lista.append(servicio.nombre + " \t" + servicio.valor + "\n");
		}

		sb.append("-------------------------------------------").append("\n");
		sb.append("Codigo de factura: ").append(this.codigo).append("\n");
		sb.append("Fecha y Hora: ").append(this.date).append("\n");
		sb.append("Empleado: ").append(empleado).append("\n");
		sb.append("Cliente: ").append(this.cliente.getNombre()).append("\n");
		sb.append(lista).append("\n");
		sb.append("Valor total:  ").append(valorTotal).append("\n");
		sb.append("-------------------------------------------");

		return sb.toString();
	}

	/*
	 * Metodo impimir codigos se encarga de imprimir los codigos de las facturas
	 * ingresadas como parametro en una rray, primcipalmente para las facturas
	 * deudas
	 */
	static public String imprimirCodigos(ArrayList<Factura> facturas) {
		StringBuilder sb = new StringBuilder();
		for (Factura factura : facturas) {
			String x = Integer.toString(factura.getCodigo());
			sb.append(x);
		}
		return sb.toString();
	}

	// CONSTRUCTOR
	public Factura(Usuario cliente, Empleado empleado, List<Servicio> items, List<Destinos> destino, String concepto) {
		this.estado = 0;
		this.cliente = cliente;
		this.empleado = empleado;
		this.items = items;
		this.destino = destino;
		this.setConcepto(concepto);
		// this.valorTotal(); // Se ejecuta el metodo de valor total para la factura
		// creada COMENTARIO PROVISIONAL

		// Establece la fecha en la que se creo la factura
		DateFormat dateFormat = new SimpleDateFormat("d MMM yyyy, HH:mm:ss ");
		this.date = dateFormat.format(new Date());

		// Estalece el codigo de factura en funcion del numero total de facturas creadas
		// hasta el momento
		Factura.contador += 1;
		this.codigo = Factura.contador;

		// Se agrega la factura al usuario y empleado correspondiente
		cliente.listaFacturas.add(this);
		if (empleado != null) {
			empleado.calcularComision(valorTotal);
		}

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

	public String getConcepto() {
		return concepto;
	}

	public void setConcepto(String concepto) {
		this.concepto = concepto;
	}

	public List<Servicio> getItems() {
		return items;
	}

	public void setItems(List<Servicio> items) {
		this.items = items;
	}

}

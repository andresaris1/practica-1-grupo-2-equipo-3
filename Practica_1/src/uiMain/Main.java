package uiMain;

import gestorAplicacion.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import baseDatos.Deserializador;

public class Main implements Serializable {

	private static final long serialVersionUID = 1L;

	private static List<Reserva> reservas = new ArrayList<Reserva>();
	private static List<Factura> facturas = new ArrayList<Factura>();
	private static List<Usuario> clientes = new ArrayList<Usuario>();
	
	static Scanner sc = new Scanner(System.in);
	static Usuario usuario1 = new Usuario("carlos", 1234, 0, null, 0);
	static Usuario usuario2 = new Usuario("Maria", 345, 0, null, 0);
	static Usuario usuario3 = new Usuario("Ximena", 763, 0, null, 0);
	static Usuario usuario4 = new Usuario("Valentin", 2468, 0, null, 0);
	static Empleado empleado1 = new Empleado("luis pedro", 0, 0, null, 0, 0);
	static Lugar hab1 = new Lugar(0, null, 0);
	static Servicio ser1 = new Servicio("piscina", 34);
	static Factura f1 = new Factura(usuario1, empleado1, null, null);
	static Reserva r1 = new Reserva(f1, "23/04/2023", "35/07/2024", 5000, usuario1);
	
	public Main() {
		Deserializador.deserializar(this);
	}
	
	public static List<Reserva> getReservas() {
		return  reservas;
	}

	public static void setReservas(List<Reserva> reservas) {
		Main.reservas = reservas;
	}

	public static List<Usuario> getClientes() {
		return clientes;
	}

	public static void setClientes(List<Usuario> clientes) {
		Main.clientes = clientes;
	}

	public static List<Factura> getFacturas() {
		return facturas;
	}

	public static void setFacturas(List<Factura> facturas) {
		Main.facturas = facturas;
	}
	
	public static Usuario registro(String nombre, int id, int telefono, String tipo, int cuentaBancaria) {
		Usuario cliente= new Usuario(nombre,id,telefono,tipo,cuentaBancaria);
		clientes.add(cliente);
		return cliente;
	}
	
	public static Usuario buscar(int id) {
		Iterator<Usuario> iterator = clientes.iterator();
		while (iterator.hasNext()) {
			Usuario cliente = (Usuario) iterator.next();
			if (cliente.getIdentificacion() == id) {
				return cliente;

			}
		}
		return null;
	}
	
	public static Factura nuevaFactura(Usuario cliente, Empleado empleado, Servicio[] items, Destinos destino) {
		Factura factura= new Factura(cliente,empleado,items,destino);
		facturas.add(factura);
		return factura;
	}
	
	public static Factura buscarFactura(int id) {
		Iterator<Factura> iterator = facturas.iterator();
		while (iterator.hasNext()) {
			Factura factura = (Factura) iterator.next();
			if (factura.getCliente().getIdentificacion() == id) {
				return factura;

			}
		}
		return null;
	}
	
	public static Reserva nuevaReserva(Factura factura, String fechaEntrada, String fechaSalida, float aporte, Usuario cliente) {
		Reserva reserva= new Reserva(factura, fechaEntrada, fechaSalida, aporte, cliente);
		reservas.add(reserva);
		return reserva;
	}
	
	public static Reserva buscarReserva(int id) {
		Iterator<Reserva> iterator = reservas.iterator();
		while (iterator.hasNext()) {
			Reserva reserva = (Reserva) iterator.next();
			if (reserva.getCliente().getIdentificacion() == id) {
				return reserva;

			}
		}
		return null;
	}

	public static String listaClientes() {
		Iterator<Usuario> iterator = clientes.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Usuario usuario = (Usuario) iterator.next();
			lista.append(usuario.informacion()+"\n");
		}
		return lista.toString();
	}
	
	public static String listaReservas() {
		Iterator<Reserva> iterator = reservas.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Reserva reserva = (Reserva) iterator.next();
			lista.append(reserva.toString()+"\n");
		}
		return lista.toString();
	}
	
	public static String listaFacturas() {
		Iterator<Factura> iterator = facturas.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Factura factura = (Factura) iterator.next();
			lista.append(factura.toString()+"\n");
		}
		return lista.toString();
	}
	

	static public Usuario[] ListaUsuarios = { usuario1, usuario2, usuario3, usuario4 };

	public static Usuario registro() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite el numero de documento:\n");
		int id = sc.nextInt();
		System.out.println("Ingrese el nombre:\n");
		String nombre = sc.next();
		System.out.print("Ingrese un numero de telefono:\n");
		int tel = sc.nextInt();
		System.out.print("Ingrese una cuenta bancaria:\n");
		int cb = sc.nextInt();
		Usuario cliente = new Usuario(nombre, id, tel, null, cb);
		clientes.add(cliente);
		return cliente;
	}


	static public Usuario buscarUsuario(int documento) {
		for (Usuario usuario : ListaUsuarios) {
			if (usuario.getIdentificacion() == documento) {
				return usuario;
			}
		}
		return null;
	}


}

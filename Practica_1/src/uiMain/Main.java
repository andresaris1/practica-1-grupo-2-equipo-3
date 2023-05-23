package uiMain;

import gestorAplicacion.Destinos;
import gestorAplicacion.Empleado;
import gestorAplicacion.Factura;
import gestorAplicacion.Lugar;
import gestorAplicacion.Reserva;
import gestorAplicacion.Servicio;
import gestorAplicacion.Usuario;

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

	static Lugar h1 = new Lugar(101, "Habitación individual", 1);
	static Lugar h2 = new Lugar(102, "Habitación individual", 1);
	static Lugar h3 = new Lugar(201, "Habitación doble", 2);
	static Lugar h4 = new Lugar(202, "Habitación doble", 2);
	static Lugar h5 = new Lugar(301, "Habitación familiar", 4);
	static Lugar h6 = new Lugar(302, "Habitación familiar", 4);

	private static List<Lugar> habitaciones = new ArrayList<Lugar>();
	private static List<Lugar> habitacionesocupadas = new ArrayList<Lugar>();

	static Scanner sc = new Scanner(System.in);
	static Usuario usuario1 = new Usuario("carlos", 1234, 0, null);
	static Usuario usuario2 = new Usuario("Maria", 345, 0, null);
	static Usuario usuario3 = new Usuario("Ximena", 763, 0, null);
	static Usuario usuario4 = new Usuario("Valentin", 2468, 0, null);
	static Empleado empleado1 = new Empleado("luis pedro", 0, 0, null, 0, 0);

	static public Usuario[] ListaUsuarios = { usuario1, usuario2, usuario3, usuario4 };

	public Main() {
		Deserializador.deserializar(this);
		clientes.add(usuario1);
		habitaciones.add(h1);
		habitaciones.add(h2);
		habitaciones.add(h3);
		habitaciones.add(h4);
		habitaciones.add(h5);
		habitaciones.add(h6);

	}
	
	public static List<Lugar> getHabitaciones(){
		return habitaciones;
	}

	public static List<Reserva> getReservas() {
		return reservas;
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

	public static Usuario registrarUsuario(String nombre, int id, int telefono, String tipo, int cuentaBancaria) {
		Usuario cliente = new Usuario(nombre, id, telefono, tipo);
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

	public Factura nuevaFactura(Usuario cliente, Empleado empleado, Servicio[] items, Destinos destino) {
		Factura factura = new Factura(cliente, empleado, items, destino);
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

	public static Reserva nuevaReserva(Factura factura, String fechaEntrada, String fechaSalida,
			List<Lugar> habitaciones, float aporte, Usuario cliente) {
		Reserva reserva = new Reserva(factura, fechaEntrada, fechaSalida, habitaciones, aporte, cliente);
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

	public static Lugar nuevaHabitacion(int numero, String tipo, int capacidad) {
		Lugar habitacion = new Lugar(numero, tipo, capacidad);
		habitaciones.add(habitacion);
		return habitacion;
	}

	public static Lugar buscarHabitacion(int id) {
		Iterator<Lugar> iterator = habitaciones.iterator();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			if (habitacion.getNumero() == id) {
				return habitacion;

			}
		}
		return null;
	}

	public static Lugar buscarHabitacionocupadas(int id) {
		Iterator<Lugar> iterator = habitacionesocupadas.iterator();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			if (habitacion.getNumero() == id) {
				return habitacion;

			}
		}
		return null;
	}

	public static String listaClientes() {
		Iterator<Usuario> iterator = clientes.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Usuario usuario = (Usuario) iterator.next();
			lista.append(usuario.informacion() + "\n");
		}
		return lista.toString();
	}

	public static String listaReservas() {
		Iterator<Reserva> iterator = reservas.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Reserva reserva = (Reserva) iterator.next();
			lista.append(reserva.toString() + "\n");
		}
		return lista.toString();
	}

	public static String listaFacturas() {
		Iterator<Factura> iterator = facturas.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Factura factura = (Factura) iterator.next();
			lista.append(factura.toString() + "\n");
		}
		return lista.toString();
	}

	public static String listaHabitaciones() {
		Iterator<Lugar> iterator = habitaciones.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.toString() + "\n");
		}
		return lista.toString();
	}

	public static String listaHabitacionesocupadas() {
		Iterator<Lugar> iterator = habitacionesocupadas.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.toString() + "\n");
		}
		return lista.toString();
	}

	public static void nodisponible(Lugar hb) {
		habitaciones.remove(hb);
		habitacionesocupadas.add(hb);
	}

	public static void disponible(Lugar hb) {
		habitaciones.add(hb);
		habitacionesocupadas.remove(hb);
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

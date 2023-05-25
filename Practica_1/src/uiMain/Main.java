	/*
	package uiMain;

	import gestorAplicacion.Destinos;
	import gestorAplicacion.Empleado;
	import gestorAplicacion.Evento;
	import gestorAplicacion.Factura;
	import gestorAplicacion.Lugar;
	import gestorAplicacion.Persona;
	import gestorAplicacion.Reserva;
	import gestorAplicacion.Servicio;
	import gestorAplicacion.ServicioExterno;
	import gestorAplicacion.Usuario;
	import gestorAplicacion.Evento;
	import gestorAplicacion.ServicioExterno;

	import java.io.Serializable;
	import java.text.ParseException;
	import java.text.SimpleDateFormat;
	import java.util.ArrayList;
	import java.util.Arrays;
	import java.util.Collections;
	import java.util.Comparator;
	import java.util.Date;
	import java.util.Iterator;
	import java.util.List;
	import java.util.Scanner;
	import baseDatos.Deserializador;

	//clase
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
		private static List<Lugar> habitaciondis = new ArrayList<Lugar>();

		static Scanner sc = new Scanner(System.in);
		private static ArrayList<Factura> hola = new ArrayList<Factura>();
		static Usuario usuario1 = new Usuario("carlos", 1234, 0, null, "", hola);
		static Usuario usuario2 = new Usuario("Maria", 345, 0, null, "", null);
		static Usuario usuario3 = new Usuario("Ximena", 763, 0, null, "", null);
		static Usuario usuario4 = new Usuario("Valentin", 2468, 0, null, "", null);
		static Empleado empleado1 = new Empleado("luis pedro", 0, 0, null, 0, 0);

		static public Usuario[] ListaUsuarios = { usuario1, usuario2, usuario3, usuario4 };
		
		private static List<Servicio> serviciosad = new ArrayList<Servicio>();
		
		static Servicio comida=new Servicio("Comida",2000);
		static Servicio masaje=new Servicio("Masaje",2000);

		public Main() {
			Deserializador.deserializar(this);
			habitaciones.add(h1);
			habitaciones.add(h2);
			habitaciones.add(h3);
			habitaciones.add(h4);
			habitaciones.add(h5);
			habitaciones.add(h6);
			serviciosad.add(masaje);
			serviciosad.add(comida);
			clientes.add(usuario1);

		}

		public static List<Lugar> getHabitaciones() {
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

		public static Usuario registrarUsuario(String nombre, int id, int telefono, String tipo, String cuentaBancaria) {
			Usuario cliente = new Usuario(nombre, id, telefono, tipo, cuentaBancaria, hola);
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

		public static Factura nuevaFactura(Usuario cliente, Empleado empleado, List<Servicio> items, Destinos destino,
				String concepto) {
			Factura factura = new Factura(cliente, empleado, items, destino, concepto);
			facturas.add(factura);
			return factura;
		}

		public static Evento nuevoEvento(Lugar lugar, Usuario cliente, ArrayList<ServicioExterno> servicios, String fecha, int duracion,
		int numeroAsistentes, ArrayList<Empleado> empleados)  {
			Evento evento = new Evento(lugar, cliente, servicios, fecha, duracion, numeroAsistentes, empleados);
			return evento;
		}
		public static Lugar nuevoLugarDeEventos(String tipo){
			Lugar lugar = new Lugar(tipo);
			return lugar;
		}

		

		public static Reserva nuevaReserva(String fechaEntrada, String fechaSalida, List<Lugar> habitaciones, float aporte,
				Usuario cliente) {
			Reserva reserva = new Reserva(fechaEntrada, fechaSalida, habitaciones, aporte, cliente);
			reservas.add(reserva);
			return reserva;
		}
		
		public static Servicio buscarServicio(String id) {
			Iterator<Servicio> iterator = serviciosad.iterator();
			while (iterator.hasNext()) {
				Servicio servicio = (Servicio) iterator.next();
				if (servicio.getNombre().equals(id)) {
					return servicio;

				}
			}
			return null;
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

		

		
		public static Lugar buscarHabitacion(int id) {
			Iterator<Lugar> iterator = habitaciondis.iterator();
			while (iterator.hasNext()) {
				Lugar habitacion = (Lugar) iterator.next();
				if (habitacion.getNumero() == id) {
					return habitacion;

				}
			}
			return null;
		}

		
		//Metodos que tengo que copiar en almacenamiento

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

		public static String listaFacturascliente(Usuario cliente) {
			Iterator<Factura> iterator = cliente.getListaFacturas().iterator();
			StringBuffer lista = new StringBuffer();
			while (iterator.hasNext()) {
				Factura factura = (Factura) iterator.next();
				lista.append(factura.toString() + "\n");
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

		public static String listaHabitaciones(List<Lugar> esto) {
			Iterator<Lugar> iterator = esto.iterator();
			StringBuffer lista = new StringBuffer();
			while (iterator.hasNext()) {
				Lugar habitacion = (Lugar) iterator.next();
				lista.append(habitacion.toString() + "\n");
			}
			return lista.toString();
		}

		public static void nodisponible(Lugar hb) {
			habitaciones.remove(hb);
		}

		public static String listarDisponibles(String fechaEntrada, String fechaSalida) {
			
			habitaciondis.clear();
			SimpleDateFormat fecha = new SimpleDateFormat("dd/MM/yyyy");
			Date fEntrada = new Date();
			try {
				fEntrada = fecha.parse(fechaEntrada);
			} catch (ParseException e) {
				e.printStackTrace();
			}
			Date fSalida = new Date();
			try {
				fSalida = fecha.parse(fechaSalida);
			} catch (ParseException e) {
				e.printStackTrace();
			}
			for (Reserva re : reservas) {
				for (Lugar h : re.getHabitaciones()) {
					if (fEntrada.after(re.getFechaEntrada()) && fSalida.after(re.getFechaSalida())
							|| fEntrada.before(re.getFechaEntrada()) && fSalida.before(re.getFechaSalida())) {
						habitaciondis.add(h);
					}
				}
			}
			Iterator<Lugar> iterator = habitaciones.iterator();
			while (iterator.hasNext()) {
				Lugar habitacion = (Lugar) iterator.next();
				habitaciondis.add(habitacion);
			}
			Collections.sort(habitaciondis, new Comparator<Lugar>() {
				public int compare(Lugar p1, Lugar p2) {
					return new Integer(p1.getNumero()).compareTo(new Integer(p2.getNumero()));
				}
			});
			String lista = listaHabitaciones(habitaciondis);
			return lista;

		}


	}
	*/
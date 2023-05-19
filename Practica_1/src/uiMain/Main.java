package uiMain;

import gestorAplicacion.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;
import baseDatos.Deserializador;

public class Main implements Serializable {

	private static final long serialVersionUID = 1L;

	private static ArrayList<Reserva> reservas = new ArrayList<Reserva>();
	private static ArrayList<Factura> facturas = new ArrayList<Factura>();
	private static ArrayList<Usuario> clientes = new ArrayList<Usuario>();
	
	
	public Main() {
		Deserializador.deserializar(this);
	}
	
	public static ArrayList<Reserva> getReservas() {
		return reservas;
	}

	public static void setReservas(ArrayList<Reserva> reservas) {
		Main.reservas = reservas;
	}

	public static ArrayList<Usuario> getClientes() {
		return clientes;
	}

	public static void setClientes(ArrayList<Usuario> clientes) {
		Main.clientes = clientes;
	}

	public static ArrayList<Factura> getFacturas() {
		return facturas;
	}

	public static void setFacturas(ArrayList<Factura> facturas) {
		Main.facturas = facturas;
	}
	
	public Usuario registro(String nombre, int id, int telefono, String tipo, int cuentaBancaria) {
		Usuario cliente= new Usuario(nombre,id,telefono,tipo,cuentaBancaria);
		clientes.add(cliente);
		return cliente;
	}
	
	public static Usuario buscar(int id) {
		Usuario user = null;
		for (Usuario usuario : clientes) {
			if (usuario.getIdentificacion() == id) {
				System.out.println("Este usuario está registrado como: " + usuario.getNombre());
				user = usuario;
				break;

			}
		}
		if (user == null) {
			int opcion;
			do {
				System.out.println("Este usuario no existe \n ¿Desea registrarlo?");
				System.out.println("1)Si \n2)No");
				opcion = sc.nextInt();

				switch (opcion) {
				case 1:
					user = registro();
					opcion = 2;
					System.out.println(user);
					break;
				case 2:
					System.out.println("Ok");
					break;
				default:
					System.out.println("Opcion no valida");
					break;
				}
			} while (opcion != 2);
		}
		return user;
	}
	
	public Factura nuevaFactura(Usuario cliente, Empleado empleado, Servicio[] items, Destinos destino) {
		Factura factura= new Factura(cliente,empleado,items,destino);
		facturas.add(factura);
		return factura;
	}
	
	public Factura buscarFactura(int id) {
		Factura user = null;
		for (Factura factura : facturas) {
			if (factura.getCliente().getIdentificacion() == id) {
				System.out.println("Este factura se registra a nombre de: " + factura.getCliente().getNombre());
				user = factura;
				break;

			}
		}
		if (user == null) {
				System.out.println("Este cliente no tiene una factura asociada, confirme su identificacion");
		}
		return user;
	}
	
	public Factura nuevaReserva(Usuario cliente, Empleado empleado, Servicio[] items, Destinos destino) {
		Factura factura= new Factura(cliente,empleado,items,destino);
		facturas.add(factura);
		return factura;
	}
	
	public Factura buscarReserva(int id) {
		Factura user = null;
		for (Factura factura : facturas) {
			if (factura.getCliente().getIdentificacion() == id) {
				System.out.println("Este factura se registra a nombre de: " + factura.getCliente().getNombre());
				user = factura;
				break;

			}
		}
		if (user == null) {
				System.out.println("Este cliente no tiene una factura asociada, confirme su identificacion");
		}
		return user;
	}
	
	
	static Scanner sc = new Scanner(System.in);
	static Usuario usuario1 = new Usuario("carlos", 1234, 0, null, 0);
	static Usuario usuario2 = new Usuario("Maria", 345, 0, null, 0);
	static Usuario usuario3 = new Usuario("Ximena", 763, 0, null, 0);
	static Usuario usuario4 = new Usuario("Valentin", 2468, 0, null, 0);
	static Empleado empleado1 = new Empleado("luis pedro", 0, 0, null, 0, 0);
	static Lugar hab1 = new Lugar(0, null, 0);
	static Servicio ser1 = new Servicio("piscina", 34);
	static Factura f1 = new Factura(usuario1, empleado1, null, null);

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

	

	public static void reservar() {
		clientes.add(usuario1);
		clientes.add(usuario2);
		clientes.add(usuario3);
		clientes.add(usuario4);
		System.out.println("Escribe tu identificacion:");
		int ide = sc.nextInt();
		Usuario user = buscar(ide);
		System.out.println("Por favor ingrese la fecha de entrada en formato dd/mm/aaaa");
		String fentrada = sc.next();
		System.out.println("Ingrese la fecha de Salida en formato dd/mm/aaaa");
		String fsalida = sc.next();
		Reserva reserva = new Reserva(Main.f1, fentrada, fsalida, 2000, user);

		System.out.println(reserva);
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

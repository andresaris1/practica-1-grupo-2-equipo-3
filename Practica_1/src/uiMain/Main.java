package uiMain;

import gestorAplicacion.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static ArrayList<Usuario> clientes = new ArrayList<Usuario>();
	static ArrayList<Usuario> reservas = new ArrayList<Usuario>();
	static ArrayList<Usuario> lugares = new ArrayList<Usuario>();
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

	/*
	 * Metodo de busqueda de usuario en la "base de datos" busca un usuario segun su
	 * documento entre un array que contiene todos los usuarios creados recide
	 * comoparemtro el documento de indentidad del usuario y regresa el objeto
	 */
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

	public static Usuario busca(int id) {
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

	public static void reservar() {
		clientes.add(usuario1);
		clientes.add(usuario2);
		clientes.add(usuario3);
		clientes.add(usuario4);
		System.out.println("Escribe tu identificacion:");
		int ide = sc.nextInt();
		Usuario user=busca(ide);
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

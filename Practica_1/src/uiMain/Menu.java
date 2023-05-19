//Clase destinada a la interfaz "grafica" que se mostrar al usuario

package uiMain;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import gestorAplicacion.*;
import baseDatos.Serializador;

public class Menu {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		Main main = new Main();
		int opcion;
		do {
			System.out.println("-- - - FUNCIONALIDADES - - - -");
			System.out.println("1. Reservar Alojamiento");
			System.out.println("2. Reservar Turística");
			System.out.println("3. Reservar Evento");
			System.out.println("4. Cobro");
			System.out.println("5. Mostrar información de habitaciones");
			System.out.println("6. Salir del sistema");
			System.out.println("Eliga una opción: ");
			opcion = sc.nextInt();

			switch (opcion) {
			case 1:
				reservar(main);
				break;

			case 2:
				// reserva turística
				System.out.println("Ingrese la identificación del usuario: ");

				int identificacion = sc.nextInt();

				Usuario usuario = Main.buscarUsuario(identificacion);

				if (usuario == null) {

					System.out.println("Usuario no encontrado en la base de datos");

					return; // Sale del caso 2 si el usuario no se encuentra

				}

				ArrayList<Destinos> destinosSeleccionados = new ArrayList<>();

				while (true) {

					System.out.println("Seleccione un destino:");

					int index = 1;
					for (Destinos destino : Destinos.values()) {

						System.out.println(index + ". " + destino);

						index++;

					}

					System.out.println("Ingrese el número del destino seleccionado (0 para salir): ");
					int numDestino = sc.nextInt();

					if (numDestino == 0) {
						break;
						// Salir del bucle si se ingresa 0
					}

					if (numDestino >= 1 && numDestino <= Destinos.values().length) {
						// revisar que el numero ingresado cuente como una opcion valida ofrecida para
						// el tour
						Destinos destinoSeleccionado = Destinos.values()[numDestino - 1];
						destinosSeleccionados.add(destinoSeleccionado);
						System.out.println("Ha seleccionado el destino: " + destinoSeleccionado);

						// Crear la factura y registrarla en la lista del cliente
						Factura factura = new Factura(usuario, Main.empleado1, new Servicio[0], destinoSeleccionado);
						usuario.getListaFacturas().add(factura);

					} else {
						System.out.println("Opción inválida, elija una opcion valida porfavor.");
						continue;
						// vuelve al inicio del bucle
					}
				}

				// muestro los destinos seleccionados 1 o mas si fue el caso
				// del usuario
				System.out.println("Destinos seleccionados:");

				for (Destinos destino : destinosSeleccionados) {
					System.out.println(destino);

				}

				//
				int valorTotalTours = 0;
				for (Destinos destino : destinosSeleccionados) {
					valorTotalTours += destino.getValor();

				}
				// valor total de los tours seleccionados
				System.out.println("Valor total de los tours seleccionados: $" + valorTotalTours);
				// Codigo de la funcionalidad reserva de tours
				break;

			case 3:
				// Codigo para la funcionalidad Reserva de eventos

				// Le pedimos su información al cliente
				System.out.println("Escribe tu identificacion: ");
				String id = sc.next();
				System.out.println("Escribe tu nombre:");
				String nombre = sc.next();

				// Se le consulta sobre el lugar que requiere
				// para su evento
				System.out.println("Escribe el lugar en el que desea su evento: ");
				System.out.println("1. Terraza");
				System.out.println("2. Piscina");
				System.out.println("3. Salon");

				// se instancia un diccionario que le dará significado
				// a su respuesta
				HashMap<Integer, String> lugares = new HashMap<Integer, String>();
				lugares.put(1, "Terraza");
				lugares.put(2, "Piscina");
				lugares.put(3, "Salon");
				int numLugar = sc.nextInt();
				String tipoLugar = lugares.get(numLugar);

				// Se le consulta sobre la cantidad de personas que
				// asistirán a su evento
				System.out.println("Escribe la cantidad de personas que asistirán al evento: ");
				int int numAsistentes = sc.nextInt();

				// Instanciamos el Diccionario que usaremos para guardar la información sobre
				// los
				// empleados que el cliente necesita
				HashMap<String, Integer> empleadosNecesarios = new HashMap<String, Integer>();
				empleadosNecesarios.put("Cocineros", -1);
				empleadosNecesarios.put("Meseros", -1);
				empleadosNecesarios.put("Bartenders", -1);

				// Pedimos al cliente que nos especifique cuántos empleados requiere
				// de cada uno de los tres tipos que le podemos ofrecer, validadando e
				// insistiendo en respetar el formato específico que sus respuestas deben tener
				for (String x : empleadosNecesarios.keySet()) {
					while (empleadosNecesarios.get(x) < 0) {
						System.out.println("¿Cuántos " + x + " requiere?");
						System.out.println("Ingrese un natural mayor o igual que cero");
						empleadosNecesarios.put(x, sc.nextInt());
					}
				}

				// le preguntamos al cliente si desea que contratemos algún servicio extra para
				// él
				System.out.println("¿Desea contratar algún servicio extra? (si/no)");
				switch (sc.next()) {
				case "si":
					System.out.println("¿Qué servicio desea contratar?");
					System.out.println("1. Entretenimiento");
					System.out.println("2. Sonido");
					System.out.println("3. Pantalla");
					int servicio = sc.nextInt();

					break;
				case "no":
					break;
				}

				// Generar la factura para el cliente tomando en cuenta todo lo solicitado.

				break;
			case 4:
				// codigo para la funcionalidad de cobro final
				System.out.println("Buen día.\nPor favor ingrese el número de documento de quien desea pagar:\n");
				int documento = sc.nextInt();
				Usuario user = Main.buscarUsuario(documento);

				if (user == null) {
					System.out.println("Usuario no encontrado en la base de datos");
					return;
					// Sale del caso 4 si el usuario no se encuentra

				}

				System.out.println("La información ingresada corresponde a:");
				System.out.println(user.informacion());

				ArrayList<Factura> listaDeuda = Factura.facturasEnDeuda(user);
				int deudaTotal = Factura.sumarDeuda(user);

				System.out.println("Se tiene una deuda de " + deudaTotal + " correspondiente a las facturas "
						+ Factura.imprimirCodigos(listaDeuda));

				System.out.println("¿Desea realizar el pago de la deuda? (S/N):");
				String opcionPago = sc.next();

				if (opcionPago.equalsIgnoreCase("S")) {
					System.out.println("Ingrese el valor a pagar: ");
					int valorIngresado = sc.nextInt();

					if (valorIngresado < deudaTotal) {
						System.out.println("El valor ingresado es menor a la deuda total.");

					}

					else {
						int vuelto = valorIngresado - deudaTotal;

						for (Factura factura : listaDeuda) {
							factura.setEstado(1);

						}

						System.out.println("Pago realizado con éxito.");
						System.out.println("Vuelto: $" + vuelto);

					}

				} else {
					System.out.println("Opción inválida. Se asume que desea realizar el pago.");
					System.out.println("Ingrese el valor a pagar: ");
					int valorIngresado = sc.nextInt();

					if (valorIngresado < deudaTotal) {
						System.out.println("El valor ingresado es menor a la deuda total.");

					} else {
						int vuelto = valorIngresado - deudaTotal;

						for (Factura factura : listaDeuda) {
							factura.setEstado(1);

						}

						System.out.println("Pago realizado con éxito.");
						System.out.println("Vuelto: $" + vuelto);

					}

				}

				break;
			case 5:
				// Codigo para la funcionalidad de mostrar informacion de habitaciones
				break;
			case 6:
				System.out.println("Gracias por preferirnos");
				Serializador.serializar(main);
				System.exit(0);
				break;
			case 7:
				System.out.println("-- - - Reservas Existentes - - - -");
				System.out.println(Main.listaReservas());
				System.out.println("-- - - Clientes Existentes - - - -");
				System.out.println(Main.listaClientes());
				System.out.println("-- - - Facturas Existentes - - - -");
				System.out.println(Main.listaFacturas());
				break;

			default:
				System.out.println("Opcion Invalida");
				break;

			}

		} while (opcion != 6);

		sc.close();
	}

	static void reservar(Main main) {
		System.out.println("Escribe tu identificacion:");
		int ide = sc.nextInt();
		Usuario user = Main.buscar(ide);
		if (user == null) {
			user = registro(main);
			if (user == null) {
				System.out.println("No se pudo realizar la reserva pues no hay un cliente a registrar\n");
				return;
			}
		}
		System.out.println("Por favor ingrese la fecha de entrada en formato dd/mm/aaaa");
		String fentrada = sc.next();
		System.out.println("Ingrese la fecha de Salida en formato dd/mm/aaaa");
		String fsalida = sc.next();
		Factura f1 = main.nuevaFactura(user, null, null, null);
		Reserva reserva = main.nuevaReserva(f1, fentrada, fsalida, 2000, user);
		System.out.println("\n" + reserva + "\n");
	}

	static Usuario registro(Main main) {
		int opcion;
		Usuario cli=null;
		do {
			System.out.println("Este numero de identificación no está registrado\n¿Desea registrarlo?");
			System.out.println("1. Si \n2. No ");
			opcion = sc.nextInt();
			switch (opcion) {
			case 1:
				System.out.println("Digite el numero de documento:\n");
				int id = sc.nextInt();
				System.out.println("Ingrese el nombre:\n");
				String nombre = sc.next();
				System.out.print("Ingrese un numero de telefono:\n");
				int tel = sc.nextInt();
				System.out.print("Ingrese una cuenta bancaria:\n");
				int cb = sc.nextInt();
				Usuario cliente = main.registrarUsuario(nombre, id, tel, null, cb);
				cli=cliente;
				System.out.println("Usuario creado con exito");
				System.out.println(cli.informacion());
				opcion=2;
				break;
			case 2:
				cli= null;
				break;
			default:
				System.out.println("Esta opcion no es valida");
				break;
			}
		} while (opcion != 2);
	return cli;

	}
}

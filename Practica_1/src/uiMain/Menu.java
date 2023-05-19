//Clase destinada a la interfaz "grafica" que se mostrar al usuario

package uiMain;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

import uiMain.Main;
import gestorAplicacion.*;

public class Menu {
	Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int opcion;
		do {
			System.out.println("-- - - FUNCIONALIDADES - - - -");
			System.out.println("1.Reservar Alojamiento");
			System.out.println("2.Reservar Turística");
			System.out.println("3.Reservar Evento");
			System.out.println("4.Cobro");
			System.out.println("5.Mostrar información de habitaciones");

			System.out.println("Eliga una opción: ");
			opcion = sc.nextInt();

			switch (opcion) {
			case 1:
				Main.reservar();
				break;

			/*
			 * case 2: // Codigo de la funcionalidad reserva de tours
			 * System.out.println("Ingrese la identificacion del usuario: "); String id =
			 * sc.next(); break;
			 */

			case 2:
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

				System.out.println("Destinos seleccionados:");
				for (Destinos destino : destinosSeleccionados) {
					System.out.println(destino);
				}
				// Codigo de la funcionalidad reserva de tours
				break;

			case 3:
				// Codigo para la funcionalidad Reserva de eventos

				// Le pedimos su información al cliente
				System.out.println("Escribe tu identificacion: ");
				String id = sc.next();
				System.out.println("Escribe tu nombre:");
				String nombre = sc.next();
				System.out.println("Escribe el lugar en el que desea su evento: ");
				System.out.println("1. Terraza");
				System.out.println("2. Piscina");
				System.out.println("3. Salon de eventos");
				System.out.println("4. Gran salón de eventos");
				int tipoLugar = sc.nextInt();

				// Instanciamos el Diccionario que usaremos para guardar la información sobre
				// los
				// empleados que el cliente necesita
				HashMap<String, Integer> empleadosNecesarios = new HashMap<String, Integer>();
				empleadosNecesarios.put("Cocineros", -1);
				empleadosNecesarios.put("Meseros", -1);
				empleadosNecesarios.put("Bartenders", -1);

				// Pedimos al cliente que nos especifique cuántos empleados requiere
				// de cada uno de los tres tipos que le podemos ofrecer, validadando e
				// insistiendo
				// el formato específico que sus respuestas deben tener
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
				System.out.println("Buen dia.\nPor favor ingrese el numero de documento de quien desea pagar:\n");
				int documento = sc.nextInt();
				Usuario user = Main.buscarUsuario(documento);
				if (user == null) {
					System.out.print("Usuario no encontrado en la base de datos");
				}

				System.out.print("La informacion ingresada corresponde a: ");
				System.out.print(user.informacion());

				ArrayList<Factura> listaDeuda = Factura.facturasEnDeuda(user);
				int deudaTotal = Factura.sumarDeuda(user);

				System.out.println("Se tiene una deuda de " + deudaTotal + "correspondiente a las facturas"
						+ Factura.imprimirCodigos(listaDeuda));

				break;
			case 5:
				// Codigo para la funcionalidad de mostrar informacion de habitaciones
				break;

			default:
				System.out.println("Opcion Invalida");
				break;

			}
			sc.close();

		} while (opcion != 5);
	}
}
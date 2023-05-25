//Clase destinada a la interfaz "grafica" que se mostrar al usuario
//Librerias a importar
package uiMain;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.random.RandomGenerator;
import java.util.Random;

import baseDatos.Serializador;
import gestorAplicacion.Destinos;
import gestorAplicacion.Empleado;
import gestorAplicacion.Factura;
import gestorAplicacion.Lugar;
import gestorAplicacion.Reserva;
import gestorAplicacion.Servicio;
import gestorAplicacion.Usuario;
import gestorAplicacion.ServicioExterno;
import gestorAplicacion.Evento;

public class Menu {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		Random rand = new Random();
		Almacenamiento almacen = new Almacenamiento();
		int opcion;
		do {
			System.out.println("-- - - FUNCIONALIDADES - - - -");
			System.out.println("1. Reserva Alojamiento");
			System.out.println("2. Reserva Turística");
			System.out.println("3. Reserva Evento");
			System.out.println("4. Cobro");
			System.out.println("5. Mostrar información de habitaciones");
			System.out.println("6. Servicios Adicionales");
			System.out.println("7. Salir del sistema");
			System.out.println("Eliga una opción: ");

			opcion = sc.nextInt();

			switch (opcion) {
				case 1:
					reservar(almacen);
					break;

				case 2:
					// FUNCIONALIDAD RESERVA TURÍSTICA
					reservarTur(almacen);
					break;

				case 3:
					// FUNCIONALIDAD RESERVA DE EVENTOS
					reservarEvento(almacen);
					break;
				case 4:

					// FUNCIONALIDAD DE COBROS
					// Queda aregar una opcion mas de consulta que deriva en cobro
					System.out.println("Por favor ingrese el número de documento de quien desea pagar:\n");
					int documento = sc.nextInt();
					Usuario user = Almacenamiento.buscarUsuario(documento);

					if (user == null) {
						System.out.println("Usuario no encontrado en la base de datos");
						return;
						// Regresar al menu principal
					}

					System.out.println("La información ingresada corresponde a:");
					System.out.println(user.informacion());

					ArrayList<Factura> listaDeuda = Factura.facturasEnDeuda(user);
					int deudaTotal = Factura.sumarDeuda(user);

					System.out.println("Se tiene una deuda de " + deudaTotal + " correspondiente a las facturas "
							+ Factura.imprimirCodigos(listaDeuda));

					Menu.cobro(listaDeuda, deudaTotal);

					break;
				case 5:
					// FUNCIONALIDAD INFORMACION DE HABITACIONES
					// Se le preguntara al usuario si desea saber luego sobre los eventos a realizar
					// en el hotel o las habitaciones
					System.out.println("Que desea ver?");
					System.out.println("1:Informacion de habitaciones");
					System.out.println("2:informacion de eventos");

					int res2 = sc.nextInt();
					
					List<Reserva> reservas = new ArrayList<Reserva>();
					reservas = Almacenamiento.getListaReservas();

					if (res2 == 1) {
						System.out.println("Por ahora tenemos " + Almacenamiento.getListaHabitaciones().size()
								+ " habitaciones disponibles");

						// Informacion categorizada por el tipo de habitacion
						System.out.println("Sobre que tipo de habitacion desea tener informacion?");

						System.out.println("1: Habitacion Familiar");
						System.out.println("2: Habitacion Doble");
						System.out.println("3: Habitacion individual");
						System.out.println("4: Ver informacion completa");

						res2 = sc.nextInt();

						if (res2 == 1) {
							// informacion de las habitaciones familiares
							// Creamos listas de las habitaciones disponibles y ocupadas para dar respectiva
							// informacion de ambas

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							List<Lugar> hab_ocu = new ArrayList<Lugar>();

							hab_dis = Almacenamiento.getListaHabitaciones();
							hab_ocu = reservas.get(0).getHabitaciones();

							// Contador de habitaciones
							int num = 0;
							int num2 = 0;

							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación familiar") {

									num++;

								}

								if (hab_ocu.get(i).getTipo() == "Habitación familiar") {

									num2++;

								}
							}

							if (num != 0) {
								System.out.println("Tenemos " + (num - num2) + " habitaciones familiares disponibles");
								System.out.println("La habitacion familiar tiene una capacidad para 4 personas");
								// Costo habitacion familiar

								int valor = Lugar.valorSegunTipo("Habitacion familiar");
								System.out.println("La habitacion familiar tiene un costo de " + valor);

							} else {

								System.out.println("No tenemos habitaciones familiares disponibles");
							}

						} else if (res2 == 2) {
							// informacion de las habitaciones dobles
							// Creamos listas de las habitaciones disponibles y ocupadas para dar respectiva
							// informacion de ambas

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							List<Lugar> hab_ocu = new ArrayList<Lugar>();

							hab_dis = Almacenamiento.getListaHabitaciones();
							hab_ocu = reservas.get(0).getHabitaciones();

							// Contador de habitaciones
							int num = 0;
							int num2 = 0;

							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación doble") {

									num++;

								}
								if (hab_ocu.get(i).getTipo() == "Habitación doble") {

									num2++;

								}

							}
							if (num != 0) {
								System.out.println("Tenemos " + (num - num2) + " habitaciones dobles disponibles");
								System.out.println("La habitacion doble tiene una capacidad para 2 personas");
								// costo habitacion doble

								int valor = Lugar.valorSegunTipo("Habitacion doble");
								System.out.println("La habitacion doble tiene un costo de " + valor);
							} else {
								System.out.println("No tenemos habitaciones dobles disponibles");
							}

						} else if (res2 == 4) {
							// Tabla de informacion general

							// Creamos listas de las habitaciones disponibles y ocupadas para dar respectiva
							// informacion de ambas
							List<Lugar> hab_dis = new ArrayList<Lugar>();
							List<Lugar> hab_ocu = new ArrayList<Lugar>();

							hab_dis = Almacenamiento.getListaHabitaciones();
							hab_ocu = reservas.get(0).getHabitaciones();

							// Contador de habitaciones
							int num = 0;
							int num2 = 0;
							Usuario cliente = reservas.get(0).getCliente();

							System.out.println("-----------------------------------------------------");

							for (int i = 0; i < hab_dis.size(); i++) {
								System.out.println("---------------------------------------------");

								// info de habitacion
								System.out.println("Habitacion " + hab_dis.get(i).getNumero());
								System.out.println("Tipo: " + hab_dis.get(i).getTipo());
								System.out.println("Capacidad: " + hab_dis.get(i).getCapacidad());
								System.out.println("Precio: " + Lugar.valorSegunTipo(hab_dis.get(i).getTipo()));

								// informacion de cliente asociado
								if (hab_ocu.contains(hab_dis.get(i))) {

									System.out.println("Cliente asociado a esta: ");
									System.out.println(cliente);

								}

								System.out.println("---------------------------------------------");

							}

							System.out.println("-----------------------------------------------------");

						} else {
							// informacion de las habitaciones individuales
							// Creamos listas de las habitaciones disponibles y ocupadas para dar respectiva
							// informacion de ambas

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							List<Lugar> hab_ocu = new ArrayList<Lugar>();

							hab_dis = Almacenamiento.getListaHabitaciones();
							hab_ocu = reservas.get(0).getHabitaciones();

							// Contador de habitaciones
							int num = 0;
							int num2 = 0;

							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación individual") {

									num++;
								}

								if (hab_ocu.get(i).getTipo() == "Habitación individual") {

									num2++;
								}
							}

							if (num != 0) {

								System.out
										.println("Tenemos " + (num - num2) + " habitaciones individuales disponibles");
								System.out.println("La habitacion individual tiene una capacidad para 4 personas");
								// costo habitacion individual

								int valor = Lugar.valorSegunTipo("Habitacion individual");
								System.out.println("La habitacion doble tiene un costo de " + valor);

							} else {

								System.out.println("No tenemos habitaciones individuales disponibles");

							}
						}

					} else {
						// Informacion categorizada por el tipo de evento
					}
					break;
				case 6:
					Servicioad(almacen);
					break;
				case 7:
					System.out.println("Gracias por preferirnos");
					Serializador.serializar(almacen);
					System.exit(0);
					break;
				default:
					System.out.println("Opcion Invalida");
					break;

			}

		} while (opcion != 7);

		sc.close();
	}

	static void cobro(ArrayList<Factura> lista, int deudaTotal) {
		System.out.println("¿Desea realizar el pago total de la deuda?");
		System.out.println("1. Si \n2. No ");
		int opcionPago = sc.nextInt();

		if (opcionPago == 2) {
			// regresar al menuprincipal
			return;
		}
		if (opcionPago == 1) {
			System.out.println("Ingrese el valor entregado: ");
			int valorIngresado = sc.nextInt();
			if (valorIngresado < deudaTotal) {
				System.out.println("El valor ingresado es menor al de la deuda");
				// Regresar al menu
				return;
			} else {
				Factura.realizarCobro(lista, valorIngresado);
				System.out.println("Pago realizado con éxito.");

			}

		} else {
			System.out.println("Opcion Invalida");
			// Regresar al menuprincipal
		}

	}

	static void reservar(Almacenamiento almacenamiento) {
		List<Lugar> habitaciones = new ArrayList<Lugar>();
		System.out.println("Escribe tu identificacion:");
		int personas;
		int valor = 0;
		int ide = sc.nextInt();
		Usuario user = Almacenamiento.buscarUsuario(ide);
		if (user == null) {
			user = registro(almacenamiento);
			if (user == null) {
				System.out.println("No se pudo realizar la reserva pues no hay un cliente a registrar\n");
				return;
			}
		}
		System.out.println("Hola " + user.getNombre() + ", bienvenido");
		System.out.println("Por favor ingrese la fecha de entrada en formato dd/mm/aaaa");
		String fentrada = sc.next();
		System.out.println("Ingrese la fecha de Salida en formato dd/mm/aaaa");
		String fsalida = sc.next();
		System.out.println("¿Para cuantas personas es la reserva?");
		personas = sc.nextInt();
		int suma = 0;
		do {
			System.out.println("-- - - Habitaciones disponibles - - - -");
			System.out.println(Almacenamiento.getListaHabitaciones());
			System.out.println("¿Que habitacion desea reservar?");
			int hb = sc.nextInt();
			Lugar habitacion = Almacenamiento.buscarHabitacion(hb);
			if (habitacion != null) {
				habitaciones.add(habitacion);
				Almacenamiento.nodisponible(habitacion);
				suma += habitacion.getCapacidad();
				valor += Lugar.valorSegunTipo(habitacion.getTipo());
				System.out.println("Habitacion reservada con exito");
			} else {
				System.out.println("Esta habitacion no está disponible");
			}
		} while (suma < personas);
		List<Servicio> servicios = new ArrayList<Servicio>();
		servicios.add(new Servicio("Reserva", valor));
		Reserva reserva = Almacenamiento.crearReserva(fentrada, fsalida, habitaciones, 0, user);
		Factura f1 = Almacenamiento.crearFactura(user, null, servicios, null, "Reserva");
		System.out.println(f1.imprimirFactura());
		System.out.println("Su reserva tiene un valor de: " + valor);
		System.out.println("¿Cuanto desea abonar?");
		int abonado = sc.nextInt();
		float t = valor - abonado;
		reserva.setAporte(t);
		System.out.println("\n" + reserva + "\n");

	}

	static void reservarEvento(Almacenamiento almacenamiento) {

		//pedimos la información del empleado  encargado de la reserva
		System.out.println("Ingrese la identificacion del empleado encargado de la reserva: ");
		int idEmpleado = sc.nextInt();
		Empleado empleadoEncargado = Almacenamiento.buscarEmpleado(idEmpleado);

		// Le pedimos su información al cliente
		System.out.println("Identificacion del usuario a realizar la reserva: ");

		// Se valida si el usuario ya está en la base de datos.
		// En caso de que no, ingresarlo a la base de datos.
		int id = sc.nextInt();
		Usuario usuario = Almacenamiento.buscarUsuario(id);
		if (usuario == null) {
			usuario = registro(almacenamiento);
			if (usuario == null) {
				System.out.println("No se pudo realizar la reserva pues no hay un cliente a registrar\n");
				return;
			}
		}

		System.out.println("Escriba la fecha en la que desea su evento: (dd/mm/aaaa))");
		String fecha = sc.next();

		System.out.println("Ecriba la duración en minutos de su evento: ");
		int duracion = sc.nextInt();

		// Se le consulta sobre el lugar que requiere
		// para su evento
		System.out.println("Escribe el lugar en el que desea su evento: ");
		System.out.println("1. Terraza");
		System.out.println("2. Piscina");
		System.out.println("3. Salon");

		// se instancia un diccionario que le dará significado
		// a su respuesta
		HashMap<Integer, String> lugares = new HashMap<Integer, String>();
		lugares.put(1, "terraza");
		lugares.put(2, "piscina");
		lugares.put(3, "salon");
		int numLugar = sc.nextInt();
		Lugar tipoLugar = Almacenamiento.crearLugar(lugares.get(numLugar));

		// Se le consulta sobre la cantidad de personas que
		// asistirán a su evento
		System.out.println("Escribe la cantidad de personas que asistirán al evento: ");
		int numAsistentes = sc.nextInt();

		System.out.println("¿Desea contratar algún servicio externo?");
		System.out.println("1. Si");
		System.out.println("2. No");

		int respuesta = sc.nextInt();

		ArrayList<ServicioExterno> serviciosExternos;

		if (respuesta == 1) {
			serviciosExternos = crearServiciosExternos(almacenamiento);
		} else {
			System.out.println("No se contrataron servicios externos");
			serviciosExternos = null;
		}

		int codigoEvento = (int) Math.floor(Math.random() * (1000000 - 10 + 1) + 10);
		// Finalmente, creación del evento
		Evento evento = Almacenamiento.crearEvento(tipoLugar, usuario, serviciosExternos, fecha, duracion,
				numAsistentes, empleadosNecesarios(almacenamiento), codigoEvento);


		// Facturación del evento:
		Servicio servicioEvento = evento;

		//Factura crearFactura(Usuario cliente, Empleado empleado, List<Servicio> items, 
		//Destinos destino, String concepto)

		List<Servicio> items = new ArrayList<Servicio>();
		items.add(servicioEvento);
		Factura factura = Almacenamiento.crearFactura(usuario, empleadoEncargado, items, null, "Evento");

		factura.imprimirFactura();
	}

	/*
	 * Este método fue creado para preguntarle al cliente por los empleados para el
	 * evento necesita
	 * dentro de la funcionalidad reserva de Eventos
	 */
	static ArrayList<Empleado> empleadosNecesarios(Almacenamiento almacenamiento) {

		ArrayList<Empleado> empleados = new ArrayList<Empleado>();
		// Instanciamos el Diccionario que usaremos para guardar la información sobre
		// los
		// empleados que el cliente necesita
		HashMap<String, Integer> empleadosNecesarios = new HashMap<String, Integer>();
		empleadosNecesarios.put("Cocineros", -1);
		empleadosNecesarios.put("Meseros", -1);
		empleadosNecesarios.put("Bartenders", -1);

		/*
		 * Pedimos al cliente que nos especifique cuántos empleados requiere
		 * de cada uno de los tres tipos que le podemos ofrecer, validadando e
		 * insistiendo en respetar el formato específico que sus respuestas deben tener
		 */
		for (String x : empleadosNecesarios.keySet()) {
			while (empleadosNecesarios.get(x) < 0) {
				System.out.println("¿Cuántos " + x + " requiere?");
				System.out.println("Ingrese un numero natural mayor o igual que cero");
				empleadosNecesarios.put(x, sc.nextInt());
			}
		}
		int variable = 0;
		for (String x : empleadosNecesarios.keySet()) {
			variable += 1;
			empleados.add(new Empleado("Rigoberto " + String.valueOf(variable), variable, x.toLowerCase()));
		}
		return empleados;
	}

	/*
	 * Este método fue creado para preguntarle al cliente por los servicios externos
	 * que necesita
	 * dentro de la funcionalidad reserva de Eventos
	 */
	static ArrayList<ServicioExterno> crearServiciosExternos(Almacenamiento almacenamiento) {

		// Instanciamos el Diccionario que usaremos para guardar los servicios

		ArrayList<ServicioExterno> serviciosExternos = new ArrayList<>();

		// le preguntamos al cliente si desea que contratemos algún servicio extra para
		// él

		String res = "si";
		while (res.equals("si")) {
			System.out.println("¿Qué servicio desea contratar?");
			System.out.println("1. entretenimiento");
			System.out.println("2. sonido");
			System.out.println("3. decoracion");
			String servicio;
			switch (sc.nextInt()) {
				case 1:
					servicio = "entretenimiento";
					break;
				case 2:
					servicio = "sonido";
					break;
				case 3:
					servicio = "decoracion";
					break;
				default:
					servicio = null;
			}

			ServicioExterno servicioExterno = new ServicioExterno(servicio, null);
			serviciosExternos.add(servicioExterno);

			System.out.println("¿Desea contratar algún otro servicio extra? (si/no)");
			res = sc.next();
		}
		return serviciosExternos;
	}

	static Usuario registro(Almacenamiento almacenamiento) {
		int opcion;
		Usuario cli = null;
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
					String cb = sc.next();
					Usuario cliente = Almacenamiento.crearUsuario(nombre, id, tel, null, cb, new ArrayList<Factura>());

					System.out.println("Usuario creado con exito");
					System.out.println(cli.informacion());
					opcion = 2;
					break;
				case 2:
					cli = null;
					break;
				default:
					System.out.println("Esta opcion no es valida");
					break;
			}
		} while (opcion != 2);
		return cli;

	}

	static void reservarTur(Almacenamiento almacenamiento) {

		System.out.print("Ingrese la identificación del empleado: ");
		int idEmpleado = sc.nextInt();
		Empleado empleado = Almacenamiento.buscarEmpleado(idEmpleado);

		if (empleado == null) {
			System.out.println("El empleado no existe.");
			break;

		}

		System.out.println("Ingrese la identificación del usuario: ");
		int identificacion = sc.nextInt();

		Usuario usuario = Almacenamiento.buscarUsuario(identificacion);

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
				break; // Salir del bucle si se ingresa 0

			}

			if (numDestino >= 1 && numDestino <= Destinos.values().length) {

				// Revisar que el número ingresado cuente como una opción válida ofrecida para
				// el tour
				Destinos destinoSeleccionado = Destinos.values()[numDestino - 1];
				destinosSeleccionados.add(destinoSeleccionado);
				System.out.println("Ha seleccionado el destino: " + destinoSeleccionado);

			} else {
				System.out.println("Opción inválida, elija una opción válida por favor.");
				continue; // Vuelve al inicio del bucle

			}
		}

		// Crear la factura y registrarla en la lista del cliente
		List<Servicio> servicios = new ArrayList<>();
		int valorTotal = 0;

		for (Destinos destino : destinosSeleccionados) {
			servicios.add(new Servicio(destino.toString(), destino.getValor()));
			System.out.println(destino.toString());
			valorTotal += destino.getValor();

		}

		//Factura(Usuario cliente, Empleado empleado, List<Servicio> items, List<Destinos> destino, String concepto)
		String concepto = "Reserva de destinos turísticos";
		Factura factura = almacenamiento.crearFactura(usuario, empleado, servicios, destinosSeleccionados, concepto);


		System.out.println("Valor total de los destinos: " + valorTotal);
		System.out.println("Factura agregada exitosamente.");

	}

	static void Servicioad(Almacenamiento almacenamiento) {
		int opcion;
		int con = 0;
		List<Servicio> servicios = new ArrayList<Servicio>();
		System.out.println("Escribe tu identificacion:");
		int ide = sc.nextInt();
		Usuario user = Almacenamiento.buscarUsuario(ide);
		if (user == null) {
			System.out.println("Usuario no registrado\n");
			return;
		} else {
			System.out.println("Hola" + user.getNombre());
		}
		do {
			System.out.println("¿Que servicio adicional desea adquirir?");
			System.out.println("1. Comida \n2. Masaje ");
			opcion = sc.nextInt();
			switch (opcion) {
				case 1:
					servicios.add(Almacenamiento.buscarServicio("Comida"));
					System.out.println("¿Desea añadir otro servicio?");
					System.out.println("1. Si \n2. No ");
					con = sc.nextInt();
					if (con == 2) {
						opcion = 2;
					}
					break;
				case 2:
					servicios.add(Almacenamiento.buscarServicio("Masaje"));
					System.out.println("¿Desea añadir otro servicio?");
					System.out.println("1. Si \n2. No ");
					con = sc.nextInt();
					if (con == 2) {
						opcion = 2;
					}
					break;
				default:
					System.out.println("Esta opcion no es valida");
					break;
			}
		} while (con != 2);

		Factura f1 = Almacenamiento.crearFactura(user, null, servicios, null, "Adicional");
		System.out.println(f1.imprimirFactura());

	}

}

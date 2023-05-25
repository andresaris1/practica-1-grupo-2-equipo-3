//Clase destinada a la interfaz "grafica" que se mostrar al usuario
//Librerias a importar
package uiMain;

//importaciones del proyecto
import gestorAplicacion.modelos.*;
import gestorAplicacion.reservacion.*;

//importaciones de java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
//import java.util.random.RandomGenerator;
import java.util.Random;

import baseDatos.Serializador;


public class Menu {
	static Scanner sc = new Scanner(System.in);
	

	public static void main(String[] args) {
		objetoss.hola();
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

					// FUNCIONALIDAD RESERVA ALOJAMIENTO
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
					informacionHabitaciones(almacen);
					break;

				case 6:

					// FUNCIONALIDAD SERVICIOS ADICIONALES
					Servicioad(almacen);
					break;

				case 7:

					// FUNCIONALIDAD SALIR DEL SISTEMA (opción secreta)
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



	//Funcionalidad de Reserva de Alojamiento
	/*
	 * Metodo que permite realizar una reserva de alojamiento. 
	 */
	static void reservar(Almacenamiento almacenamiento) {
		List<Lugar> habitaciones = new ArrayList<Lugar>();
		System.out.println("Escriba su ID de empleado:");
		int idex = sc.nextInt();
		Empleado empleado  = almacenamiento.buscarEmpleado(idex);
		System.out.println("Escriba la identificacion de quien va a reservar:");
		int personas;
		int valor = 0;
		int ide = sc.nextInt();
		Usuario user = almacenamiento.buscarUsuario(ide);
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
		if(comprobarfecha(fentrada,fsalida)) {
			return;
		}
		System.out.println("¿Para cuantas personas es la reserva?");
		personas = sc.nextInt();
		int suma = 0;
		do {
			System.out.println("-- - - Habitaciones disponibles - - - -");
			System.out.println(almacenamiento.listarDisponibles(fentrada,fsalida));
			System.out.println("¿Que habitacion desea reservar?");
			int hb = sc.nextInt();
			Lugar habitacion = almacenamiento.buscarHabitacion(hb);
			if (habitacion != null) {
				habitaciones.add(habitacion);
				almacenamiento.nodisponible(habitacion);
				suma += habitacion.getCapacidad();
				valor += habitacion.valorSegunTipo(habitacion.getTipo());
				System.out.println("Habitacion reservada con exito");
			} else {
				System.out.println("Esta habitacion no está disponible");
			}
		} while (suma < personas);
		List<Servicio> servicios=new ArrayList<Servicio>();
		servicios.add(new Servicio("Reserva", valor));
		Reserva reserva = almacenamiento.crearReserva(fentrada, fsalida, habitaciones, 0, user);
		Factura f1= almacenamiento.crearFactura(user,empleado,servicios,null, "Reserva");
		System.out.println(f1.imprimirFactura());
		System.out.println("Su reserva tiene un valor de: " + valor);
		System.out.println("¿Cuanto desea abonar?");
		int abonado = sc.nextInt();
		int t=valor-abonado;
		reserva.setAporte(t);
		f1.setValorTotal(t);
		System.out.println(f1.imprimirFactura());
		System.out.println("\n" + reserva + "\n");

	}

	static boolean comprobarfecha(String fentrada, String fsalida) {
		SimpleDateFormat fecha = new SimpleDateFormat("dd/MM/yyyy");
		Date fEntrada = new Date();
		try {
			fEntrada = fecha.parse(fentrada);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		Date fSalida = new Date();
		try {
			fSalida = fecha.parse(fsalida);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		Date date=new Date();
		if ((fEntrada.before(date)) || (fEntrada.after(fSalida))) {
			System.out.println("Fechas de entrada invalida");
			return true;
		}else if ((fSalida.before(date)) || (fSalida.before(fEntrada))){
			System.out.println("Fechas de salida invalida");
			return true;
		}else {
			return false;
		}
	}








	//SECCIÓN FUNCIONALIDAD RESERVA DE EVENTOS
	//-----------------------------------------------------------------
	static void reservarEvento(Almacenamiento almacenamiento) {

		/*Esta funcionalidad consiste en brindarle al cliente la posibilidad de rentar, por un día,
		* uno de los espacios designados para este fin, para la realización de eventos sociales.
		* Descrita paso a paso, esta funcionalidad consiste en lo siguiente:
		* 1. La recepcionista ingresa su identificación, de modo tal que quede registrado
		*	  que la reserva fuera realizada por ella.
		* 2. Se le pide al cliente que ingrese su identificación, para así buscarlo en la base
		*    de datos. En caso de que no se encuentre, se le pide que se registre.
		* 3. Tras haberse encontrado en la base de datos o, en su defecto, haberse registrado, se le
		*    pide al cliente que ingrese la fecha en la que planea realizar el evento. (no validé 
		*    que la fecha no estuviese ocupada)
		* 4. Se le pregunta al cliente por la duración de su Evento
		* 5. Se le pregunta al cliente por el tipo de espacio que desea alquilar para el evento
		*    en cuestión: Terraza, Salón o Piscina.
		* 6. Se le pregunta al usuario cuantas personas asistirán al evento.
		* 7. Se le pregunta al usuario si desea contratar algún/os servicio/s externo/s 
		*    (decoración, entretenimiento, sonido)
		* 8. Se genera un código aleatorio unico e inmutable para identificar al Evento.
		* 9. Se realiza la Facturación y se imprime la factura
		*/
		//pedimos la información del empleado  encargado de la reserva
		System.out.println("Ingrese la identificacion del empleado encargado de la reserva: ");
		int idEmpleado = sc.nextInt();
		Empleado empleadoEncargado = Almacenamiento.buscarEmpleado(idEmpleado);
		if (empleadoEncargado == null) {
			System.out.println("El empleado no existe");
		}

		// Le pedimos su información al cliente
		System.out.println("Identificacion del usuario a realizar la reserva: ");
		int id = sc.nextInt();
		// Se valida si el usuario ya está en la base de datos.
		// En caso de que no, ingresarlo a la base de datos.
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

		//se genera un codigo aleatorio para el evento
		int codigoEvento = (int) Math.floor(Math.random() * (1000000 - 10 + 1) + 10);

		// Finalmente, creación del evento
		Evento evento = Almacenamiento.crearEvento(tipoLugar, usuario, serviciosExternos, fecha, duracion,
				numAsistentes, empleadosNecesarios(almacenamiento), codigoEvento);


		// Facturación del evento:
		Servicio servicioEvento = evento;

		
		List<Servicio> items = new ArrayList<Servicio>();
		items.add(servicioEvento);

		//Se crea la factura
		Factura factura = Almacenamiento.crearFactura(usuario, empleadoEncargado, items, null, "Evento");

		//Se imprime la factura
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

	// ----------------- Aquí acaba lo relacionado con la funcionalidad de reserva de eventos -----------------





	/*
	 * Método usado para registrar un nuevo usuario dentro de la base de datos
	 */
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
					cli=cliente;
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







	/*
	 * Funcionalidad de Reserva de Tour
	 */
	static void reservarTur(Almacenamiento almacenamiento) {

		System.out.print("Ingrese la identificación del empleado: ");
		int idEmpleado = sc.nextInt();
		Empleado empleado = Almacenamiento.buscarEmpleado(idEmpleado);

		if (empleado == null) {
			System.out.println("El empleado no existe.");
			return;

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
		Factura factura = Almacenamiento.crearFactura(usuario, empleado, servicios, destinosSeleccionados, concepto);


		System.out.println("Valor total de los destinos: " + valorTotal);
		System.out.println("Factura agregada exitosamente.");
		factura.imprimirFactura();

	}






	/*
	 * Funcionalidad de Servicio adicional.
	 * Complementario a la Reserva de Alojamiento.
	 * Permite al usuario adquirir servicios adicionales como por ejemplo 
	 * masajes, comidas, transporte.
	 */
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
			System.out.println("1. Comida \n2. Masaje \n3. Transporte ");
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
				case 3:
					servicios.add(Almacenamiento.buscarServicio("Transporte"));
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



	// Funcionalidad de Información de Habitaciones

	/*
	 * Esta funcionalidad se encarga de mostrar de manera detallada y organizada toda la
	 * información en cuanto a los lugares del hotel y sus servicios prestados.
	 * 
	 */
	static void informacionHabitaciones(Almacenamiento almacenamiento){
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
	}

}

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
		Main main = new Main();
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
					reservar(main);
					break;

				case 2:
					 // FUNCIONALIDAD RESERVA TURÍSTICA
					System.out.println("Ingrese la identificación del usuario: ");
					int identificacion = sc.nextInt();

					Usuario usuario = Almacenamiento.buscarUsuario(identificacion);

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
							break; // Salir del bucle si se ingresa 0
        
						}

						if (numDestino >= 1 && numDestino <= Destinos.values().length) {

							// Revisar que el número ingresado cuente como una opción válida ofrecida para el tour
							Destinos destinoSeleccionado = Destinos.values()[numDestino - 1];
							destinosSeleccionados.add(destinoSeleccionado);
							System.out.println("Ha seleccionado el destino: " + destinoSeleccionado);

						}
						else {
							System.out.println("Opción inválida, elija una opción válida por favor.");
							continue; // Vuelve al inicio del bucle

						}
					}

					// Crear la factura y registrarla en la lista del cliente
					List<Servicio> servicios = new ArrayList<Servicio>();
					for (Destinos destino : destinosSeleccionados) {
						Servicio servicioTurismo = new Servicio("Turismo", destino.getPrecio());
						servicios.add(servicioTurismo);

					}
					
					Factura factura = Main.nuevaFactura(usuario, servicios);
					usuario.getListaFacturas().add(factura);

					break;
				case 3:
					//FUNCIONALIDAD RESERVA DE EVENTOS
					reservarEvento(main);
					break;
				case 4:

					// FUNCIONALIDAD DE COBROS 
					//Queda aregar una opcion mas de consulta que deriva en cobro
					System.out.println("Por favor ingrese el número de documento de quien desea pagar:\n");
					int documento = sc.nextInt();
					Usuario user = Main.buscarUsuario(documento);

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

					if (res2 == 1) {
						System.out.println("Por ahora tenemos " + Almacenamiento.getListaHabitaciones().size() + " habitaciones disponibles");

						// Informacion categorizada por el tipo de habitacion
						System.out.println("Sobre que tipo de habitacion desea tener informacion?");

						System.out.println("1: Habitacion Familiar");
						System.out.println("2: Habitacion Doble");
						System.out.println("3: Habitacion individual");
						System.out.println("4: Ver informacion completa");

						res2 = sc.nextInt();

						if (res2 == 1) {
							// informacion de las habitaciones familiares

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							hab_dis = Almacenamiento.getListaHabitaciones();
							int num = 0;

							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación familiar") {
									num++;
								}
							}

							if (num != 0) {
								System.out.println("Tenemos " + num + " habitaciones familiares disponibles");
								System.out.println("La habitacion familiar tiene una capacidad para 4 personas");
								// Costo habitacion familiar

								int valor = Lugar.valorSegunTipo("Habitacion familiar");
								System.out.println("La habitacion familiar tiene un costo de " + valor);

							} else {

								System.out.println("No tenemos habitaciones familiares disponibles");
							}

						} else if (res2 == 2) {
							// informacion de las habitaciones dobles

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							hab_dis = Almacenamiento.getListaHabitaciones();
							int num = 0;

							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación doble") {
									num++;
								}

							}
							if (num != 0) {
								System.out.println("Tenemos " + num + " habitaciones dobles disponibles");
								System.out.println("La habitacion doble tiene una capacidad para 2 personas");
								// costo habitacion doble

								int valor = Lugar.valorSegunTipo("Habitacion doble");
								System.out.println("La habitacion doble tiene un costo de " + valor);
							} else {
								System.out.println("No tenemos habitaciones dobles disponibles");
							}

						} else if (res2 == 4){
							//Tabla de informacion general
							List<Lugar> hab_dis = new ArrayList<Lugar>();
							hab_dis = Almacenamiento.getListaHabitaciones();
							int num = 0;
							
							System.out.println("-----------------------------------------------------");
							
							for (int i = 0; i < hab_dis.size(); i++) {
								System.out.println("---------------------------------------------");
								
								System.out.println("Habitacion "+ hab_dis.get(i).getNumero());
								System.out.println("Tipo: " + hab_dis.get(i).getTipo());
								System.out.println("Capacidad: " + hab_dis.get(i).getCapacidad());
								System.out.println("Precio: " + Lugar.valorSegunTipo(hab_dis.get(i).getTipo()));
								
								System.out.println("---------------------------------------------");

							}
							
							System.out.println("-----------------------------------------------------");
							
						}else {
							// informacion de las habitaciones individuales

							List<Lugar> hab_dis = new ArrayList<Lugar>();
							hab_dis = Almacenamiento.getListaHabitaciones();
							int num = 0;
							for (int i = 0; i < hab_dis.size(); i++) {

								if (hab_dis.get(i).getTipo() == "Habitación individual") {

									num++;
								}
							}

							if (num != 0) {

								System.out.println("Tenemos " + num + " habitaciones individuales disponibles");
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
					Servicioad(main);
					break;
				case 7:
					System.out.println("Gracias por preferirnos");
					Serializador.serializar(main);
					System.exit(0);
					break;
				case 8:
					System.out.println("-- - - Reservas Existentes - - - -");
					System.out.println(Main.listaReservas());
					System.out.println("-- - - Clientes Existentes - - - -");
					System.out.println(Main.listaClientes());
					System.out.println("-- - - Facturas de Cliente - - - -");
					Usuario usere=Main.usuario1;
					System.out.println(Main.listaFacturascliente(usere));
					System.out.println("-- - - Facturas Existentes - - - -");
					System.out.println(Main.listaFacturas());
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

	static void reservar(Main main) {
		List<Lugar> habitaciones = new ArrayList<Lugar>();
		System.out.println("Escribe tu identificacion:");
		int personas;
		int valor = 0;
		int ide = sc.nextInt();
		Usuario user = Main.buscar(ide);
		if (user == null) {
			user = registro(main);
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
			System.out.println(Main.listarDisponibles(fentrada,fsalida));
			System.out.println("¿Que habitacion desea reservar?");
			int hb = sc.nextInt();
			Lugar habitacion = main.buscarHabitacion(hb);
			if (habitacion != null) {
				habitaciones.add(habitacion);
				main.nodisponible(habitacion);
				suma += habitacion.getCapacidad();
				valor += habitacion.valorSegunTipo(habitacion.getTipo());
				System.out.println("Habitacion reservada con exito");
			} else {
				System.out.println("Esta habitacion no está disponible");
			}
		} while (suma < personas);
		List<Servicio> servicios=new ArrayList<Servicio>();
		servicios.add(new Servicio("Reserva", valor));
		Reserva reserva = main.nuevaReserva(fentrada, fsalida, habitaciones, 0, user);
		Factura f1=main.nuevaFactura(user,null,servicios,null, "Reserva");
		System.out.println(f1.imprimirFactura());
		System.out.println("Su reserva tiene un valor de: " + valor);
		System.out.println("¿Cuanto desea abonar?");
		int abonado = sc.nextInt();
		float t=valor-abonado;
		reserva.setAporte(t);
		System.out.println("\n" + reserva + "\n");
		
	}

	static void reservarEvento(Main main){
		// Le pedimos su información al cliente
		System.out.println("Escribe tu identificacion: ");
		//Se valida si el usuario ya está en la base de datos.
		//En caso de que no, ingresarlo a la base de datos.
		int id = sc.nextInt();
		Usuario usuario = Main.buscar(id);
		if (usuario == null) {
			usuario = registro(main);
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
		Lugar tipoLugar = Main.nuevoLugarDeEventos(lugares.get(numLugar));

		// Se le consulta sobre la cantidad de personas que
		// asistirán a su evento
		System.out.println("Escribe la cantidad de personas que asistirán al evento: ");
		int numAsistentes = sc.nextInt();

		

		System.out.println("¿Desea contratar algún servicio externo?");
		System.out.println("1. Si");
		System.out.println("2. No");

		int respuesta = sc.nextInt();

		ArrayList<ServicioExterno> serviciosExternos;

		if(respuesta==1){
			serviciosExternos = crearServiciosExternos(main);
		}else{
			System.out.println("No se contrataron servicios externos");
			serviciosExternos =null;
		}
		
		//Finalmente, creación del evento
		Evento evento = Main.nuevoEvento(tipoLugar, usuario, serviciosExternos, fecha, duracion, numAsistentes,empleadosNecesarios(main) );

		//Facturación del evento:
		Servicio servicioEvento = evento;
	
	}
	
	/*
	 * Este método fue creado para preguntarle al cliente por los empleados para el 
	 * evento  necesita
	 * dentro de la funcionalidad reserva de Eventos
	 */
	static ArrayList<Empleado> empleadosNecesarios(Main main){

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
			empleados.add(new Empleado("Rigoberto "+String.valueOf(variable) ,variable, x.toLowerCase()  ));
		}
		return empleados;
	}

	/*
	 * Este método fue creado para preguntarle al cliente por los servicios externos
	 * que necesita
	 * dentro de la funcionalidad reserva de Eventos
	 */
	static ArrayList<ServicioExterno> crearServiciosExternos(Main main) {

		// Instanciamos el Diccionario que usaremos para guardar los servicios

		ArrayList<ServicioExterno> serviciosExternos = new ArrayList<>();


		// le preguntamos al cliente si desea que contratemos algún servicio extra para
		// él
		
		String res = "si";
		while(res.equals("si")) {
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
					servicio=null;
			}

			ServicioExterno servicioExterno = new ServicioExterno(servicio,null);
			serviciosExternos.add(servicioExterno);
			
			System.out.println("¿Desea contratar algún otro servicio extra? (si/no)");
			res = sc.next();
		}
		return serviciosExternos;
	}
	
	
	static Usuario registro(Main main) {
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
					Usuario cliente = main.registrarUsuario(nombre, id, tel, null, cb);
					cli = cliente;
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
	
	static void Servicioad(Main main) {
		int opcion;
		int con=0;
		List<Servicio> servicios=new ArrayList<Servicio>();
		System.out.println("Escribe tu identificacion:");
		int ide = sc.nextInt();
		Usuario user = Main.buscar(ide);
		if (user == null) {
			System.out.println("Usuario no registrado\n");
			return;
		}else {
			System.out.println("Hola"+user.getNombre());
		}
		do {
			System.out.println("¿Que servicio adicional desea adquirir?");
			System.out.println("1. Comida \n2. Masaje ");
			opcion = sc.nextInt();
			switch (opcion) {
				case 1:
					servicios.add(main.buscarServicio("Comida"));
					System.out.println("¿Desea añadir otro servicio?");
					System.out.println("1. Si \n2. No ");
					con = sc.nextInt();
					if(con==2){
						opcion=2;
					}
					break;
				case 2:
					servicios.add(main.buscarServicio("Masaje"));
					System.out.println("¿Desea añadir otro servicio?");
					System.out.println("1. Si \n2. No ");
					con = sc.nextInt();
					if(con==2){
						opcion=2;
					}
					break;
				default:
					System.out.println("Esta opcion no es valida");
					break;
			}
		} while (con != 2);
		
		Factura f1=main.nuevaFactura(user,null,servicios,null, "Adicional");
		System.out.println(f1.imprimirFactura());

	}

}

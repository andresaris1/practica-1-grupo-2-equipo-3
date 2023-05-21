
	
	public static Reserva nuevaReserva(Factura factura, String fechaEntrada, String fechaSalida, List<Lugar> habitaciones, float aporte, Usuario cliente) {
		Reserva reserva= new Reserva(factura, fechaEntrada, fechaSalida, habitaciones, aporte, cliente);
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
		Lugar habitacion= new Lugar(numero, tipo,  capacidad);
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
	
	public static String listaHabitaciones() {
		Iterator<Lugar> iterator = habitaciones.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.toString()+"\n");
		}
		return lista.toString();
	}
	
	public static String listaHabitacionesocupadas() {
		Iterator<Lugar> iterator = habitacionesocupadas.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.toString()+"\n");
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

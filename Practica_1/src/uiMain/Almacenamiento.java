package uiMain;

import gestorAplicacion.*;

import java.io.Serializable;
import java.sql.Date;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import baseDatos.Deserializador;

public class Almacenamiento implements Serializable {

    // LISTA PARA GUARDAR LOS OBJETOS DE CADA TIPO (SERIALIZACION)

    // lista usurios
    private static List<Usuario> listaUsuarios = new ArrayList<Usuario>();
    // lista empleados
    private static List<Empleado> listaEmpleados = new ArrayList<Empleado>();

    // Lista Habitaciones
    private static List<Lugar> listaHabitaciones = new ArrayList<Lugar>();
    // Lista Lugares para eventos
    private static List<Lugar> listaLugares = new ArrayList<Lugar>();

    // lista reservas
    private static List<Reserva> listaReservas = new ArrayList<Reserva>();
    // lista eventos
    private static List<Evento> listaEventos = new ArrayList<Evento>();
    // lista Servicios
    private static List<Servicio> listaServicios = new ArrayList<Servicio>();

    // lista Facturas
    private static List<Factura> listaFacturas = new ArrayList<Factura>();
    // lista Servicios Externos
    private static List<ServicioExterno> listaServiciosExternos = new ArrayList<ServicioExterno>();

    // lista copiada de main
    private static List<Lugar> habitaciondis = new ArrayList<Lugar>();

    // METODOS DE BUSQUEDA
    public static Usuario buscarUsuario(int id) {
        Iterator<Usuario> iterator = Almacenamiento.getListaUsuarios().iterator();
        while (iterator.hasNext()) {
            Usuario cliente = (Usuario) iterator.next();
            if (cliente.getIdentificacion() == id) {
                return cliente;

            }
        }
        return null;
    }

    public static Empleado buscarEmpleado(int id) {
        Iterator<Empleado> iterator = Almacenamiento.getListaEmpleados().iterator();
        while (iterator.hasNext()) {
            Empleado empleado = (Empleado) iterator.next();
            if (empleado.getIdentificacion() == id) {
                return empleado;

            }
        }
        return null;
    }

    public static Lugar buscarHabitacion(int id) {
        Iterator<Lugar> iterator = Almacenamiento.getListaHabitaciones().iterator();
        while (iterator.hasNext()) {
            Lugar habitacion = (Lugar) iterator.next();
            if (habitacion.getNumero() == id) {
                return habitacion;

            }
        }
        return null;
    }

    public static Lugar buscarLugar(String tipo) {
        Iterator<Lugar> iterator = Almacenamiento.getListaLugares().iterator();
        while (iterator.hasNext()) {
            Lugar lugar = (Lugar) iterator.next();
            if (lugar.getTipo() == tipo) {
                return lugar;

            }
        }
        return null;
    }

    public static Servicio buscarServicio(String nombre) {
        Iterator<Servicio> iterator = Almacenamiento.getListaServicios().iterator();
        while (iterator.hasNext()) {
            Servicio servicio = (Servicio) iterator.next();
            if (servicio.getNombre() == nombre) {
                return servicio;

            }
        }
        return null;
    }

    public static Reserva buscarReserva(int id) {
        Iterator<Reserva> iterator = Almacenamiento.getListaReservas().iterator();
        while (iterator.hasNext()) {
            Reserva reserva = (Reserva) iterator.next();
            if (reserva.getCliente().getIdentificacion() == id) {
                return reserva;

            }
        }
        return null;
    }

    public static Evento buscarEvento(int id) {
        Iterator<Evento> iterator = Almacenamiento.getListaEventos().iterator();
        while (iterator.hasNext()) {
            Evento evento = (Evento) iterator.next();
            if (evento.getCodigo() == id) {
                return evento;

            }
        }
        return null;
    }

    // METODOS PARA CREAR OBJETOS

    public static Usuario crearUsuario(String nombre, int identificacion, int telefono, String tipo,
            String cuentaBancaria,
            ArrayList<String> arrayList) {
        Usuario usuario = new Usuario(nombre, identificacion, telefono, tipo, cuentaBancaria, new ArrayList<Factura>());
        Almacenamiento.listaUsuarios.add(usuario);
        return usuario;
    }

    public static Empleado crearEmpleado(String nombre, int identificacion, int telefono, String cargo) {
        Empleado empleado = new Empleado(nombre, identificacion, cargo);
        Almacenamiento.listaEmpleados.add(empleado);
        return empleado;
    }

    public static Lugar crearHabitacion(int numero, String tipo, int capacidad) {
        Lugar habitacion = new Lugar(numero, tipo, capacidad);
        Almacenamiento.listaHabitaciones.add(habitacion);
        return habitacion;
    }

    public static Lugar crearLugar(String tipo) {
        Lugar lugar = new Lugar(tipo);
        Almacenamiento.listaLugares.add(lugar);
        return lugar;

    }

    public static Servicio crearServico(String nombre, int valor) {
        Servicio servicio = new Servicio(nombre, valor);
        Almacenamiento.listaServicios.add(servicio);
        return servicio;
    }

    public static Reserva crearReserva(String fechaEntrada, String fechaSalida, List<Lugar> habitaciones, float aporte,
            Usuario cliente) {
        Reserva reserva = new Reserva(fechaEntrada, fechaSalida, habitaciones, aporte, cliente);
        Almacenamiento.listaReservas.add(reserva);
        return reserva;
    }

    public static Evento crearEvento(Lugar lugar, Usuario cliente, ArrayList<ServicioExterno> servicios, String fecha,
            int duracion, int numeroAsistentes, ArrayList<Empleado> empleados, int codigo) {
        Evento evento = new Evento(lugar, cliente, servicios, fecha, duracion, numeroAsistentes, empleados, codigo);
        Almacenamiento.listaEventos.add(evento);
        return evento;
    }

    public static Factura crearFactura(Usuario cliente, Empleado empleado, List<Servicio> items, Destinos destino,
			String concepto) {
		Factura factura = new Factura(cliente, empleado, items, destino, concepto);
		listaFacturas.add(factura);
		return factura;
	}

    // METODOS COPIADOS DE LA CLASE MAIN
    // Metodos que tengo que copiar en almacenamiento

    public static String listaUsuarios() {
        Iterator<Usuario> iterator = listaUsuarios.iterator();
        StringBuffer lista = new StringBuffer();
        while (iterator.hasNext()) {
            Usuario usuario = (Usuario) iterator.next();
            lista.append(usuario.informacion() + "\n");
        }
        return lista.toString();
    }

    public static String listaReservas() {
        Iterator<Reserva> iterator = listaReservas.iterator();
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
        Iterator<Factura> iterator = listaFacturas.iterator();
        StringBuffer lista = new StringBuffer();
        while (iterator.hasNext()) {
            Factura factura = (Factura) iterator.next();
            lista.append(factura.toString() + "\n");
        }
        return lista.toString();
    }

    public static String listaHabitaciones() {
        Iterator<Lugar> iterator = listaHabitaciones.iterator();
        StringBuffer lista = new StringBuffer();
        while (iterator.hasNext()) {
            Lugar habitacion = (Lugar) iterator.next();
            lista.append(habitacion.toString() + "\n");
        }
        return lista.toString();
    }

    // Sobrecarga de metodos
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
        listaHabitaciones.remove(hb);
    }
/*
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
        for (Reserva re : listaReservas) {
            for (Lugar h : re.getHabitaciones()) {
                if (fEntrada.after(re.getFechaEntrada()) && fSalida.after(re.getFechaSalida())
                        || fEntrada.before(re.getFechaEntrada()) && fSalida.before(re.getFechaSalida())) {
                    habitaciondis.add(h);
                }
            }
        }
        Iterator<Lugar> iterator = listaHabitaciones.iterator();
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
*/
    // CONSTRUCTOR
    public Almacenamiento() {
        Deserializador.deserializar(this);
    }

    // GETERS AND SETTERS
    public static List<Usuario> getListaUsuarios() {
        return listaUsuarios;
    }

    public static void setListaUsuarios(List<Usuario> listaUsuarios) {
        Almacenamiento.listaUsuarios = listaUsuarios;
    }

    public static List<Empleado> getListaEmpleados() {
        return listaEmpleados;
    }

    public static void setListaEmpleados(List<Empleado> listaEmpleados) {
        Almacenamiento.listaEmpleados = listaEmpleados;
    }

    public static List<Lugar> getListaHabitaciones() {
        return listaHabitaciones;
    }

    public static void setListaHabitaciones(List<Lugar> listaHabitaciones) {
        Almacenamiento.listaHabitaciones = listaHabitaciones;
    }

    public static List<Lugar> getListaLugares() {
        return listaLugares;
    }

    public static void setListaLugares(List<Lugar> listaLugares) {
        Almacenamiento.listaLugares = listaLugares;
    }

    public static List<Reserva> getListaReservas() {
        return listaReservas;
    }

    public static void setListaReservas(List<Reserva> listaReservas) {
        Almacenamiento.listaReservas = listaReservas;
    }

    public static List<Evento> getListaEventos() {
        return listaEventos;
    }

    public static void setListaEventos(List<Evento> listaEventos) {
        Almacenamiento.listaEventos = listaEventos;
    }

    public static List<Servicio> getListaServicios() {
        return listaServicios;
    }

    public static void setListaServicios(List<Servicio> listaServicios) {
        Almacenamiento.listaServicios = listaServicios;
    }

    public static List<ServicioExterno> getListaServiciosExternos() {
        return listaServiciosExternos;
    }

    public static void setListaServiciosExternos(List<ServicioExterno> listaServiciosExternos) {
        Almacenamiento.listaServiciosExternos = listaServiciosExternos;
    }

    public static List<Factura> getListaFacturas() {
        return listaFacturas;
    }

    public static void setListaFacturas(List<Factura> listaFacturas) {
        Almacenamiento.listaFacturas = listaFacturas;
    }

}

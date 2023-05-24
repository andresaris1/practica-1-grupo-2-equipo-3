package uiMain;

import gestorAplicacion.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Almacenamiento implements Serializable {

    // Listas para cada tipo de objetos, para guargar mediante la serializacion

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
    // lista Servicios Externos
    private static List<ServicioExterno> listaServiciosExternos = new ArrayList<ServicioExterno>();

    
    //GETERS AND SETTERS
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
    
}

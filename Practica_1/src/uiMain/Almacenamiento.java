package uiMain;

import gestorAplicacion.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import baseDatos.*;

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
    private static List<Usuario> listaReservas = new ArrayList<Usuario>();
    // lista eventos
    private static List<Usuario> listaEventos = new ArrayList<Usuario>();
    // lista Servicios
    private static List<Usuario> listaServicios = new ArrayList<Usuario>();;


    
}

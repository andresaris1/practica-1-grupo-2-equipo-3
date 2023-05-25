package gestorAplicacion.reservacion;
/*Clase reverva se usapara almacenar la informacion incluida en la reserva de cada cliente */

import java.io.Serializable;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import gestorAplicacion.modelos.*;

public class Reserva implements Serializable {
	private static final long serialVersionUID = 1L;

	private Date fechaEntrada;
	private Date fechaSalida;
	private String fe;
	private String fs;
	private float aporte;
	private Usuario cliente;
	private List<Lugar> habitaciones = new ArrayList<Lugar>();

	// CONSTRUCTOR
	public Reserva(String fechaEntrada, String fechaSalida, List<Lugar> habitaciones, float aporte, Usuario cliente) {
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
		this.fechaEntrada = fEntrada;
		this.fechaSalida = fSalida;
		this.aporte = aporte;
		this.cliente = cliente;
		this.habitaciones = habitaciones;
		this.setFe(fechaEntrada);
		this.setFs(fechaSalida);
	}

	// METODOS
	public String listaHabitaciones() {
		Iterator<Lugar> iterator = habitaciones.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.getNumero() + " " + habitacion.getTipo() + "\n");
		}
		return lista.toString();
	}

	public String toString() {
		String habitaciones = listaHabitaciones();
		return "la reserva se hizo a nombre de: " + cliente.nombre + " Entre los dias: " + getFe() + " y "
				+ getFs() + " para las habitaciones:\n" + habitaciones;
	}

	// GETTERS Y SETTERS
	public Date getFechaSalida() {
		return fechaSalida;
	}

	public void setFechaSalida(Date fechaSalida) {
		this.fechaSalida = fechaSalida;
	}

	public Usuario getCliente() {
		return cliente;
	}

	public Date getFechaEntrada() {
		return fechaEntrada;
	}

	public void setFechaEntrada(Date fechaEntrada) {
		this.fechaEntrada = fechaEntrada;
	}

	public float getAporte() {
		return aporte;
	}

	public void setAporte(float aporte) {
		this.aporte = aporte;
	}

	public List<Lugar> getHabitaciones() {
		return habitaciones;
	}

	public void setHabitaciones(List<Lugar> habitaciones) {
		this.habitaciones = habitaciones;
	}

	public String getFe() {
		return fe;
	}

	public void setFe(String fe) {
		this.fe = fe;
	}

	public String getFs() {
		return fs;
	}

	public void setFs(String fs) {
		this.fs = fs;
	}

}
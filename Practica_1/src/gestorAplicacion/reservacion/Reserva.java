package gestorAplicacion.reservacion;
/*Clase reverva se usapara almacenar la informacion incluida en la reserva de cada cliente */

//Importaciones de java
import java.io.Serializable;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;


//importaciones del proyecto
import gestorAplicacion.modelos.*;


/*
 * Clase Reserva encargada de crear las reservas de alojamiento, las cuales son un tipo 
 * de servicio que se le ofrece a los clientes, estas reservas pueden ser de diferentes 
 * tipos en función del tipo de habitación elegida para el alojamiento (Sencilla, doble, familiar).
 * La reserva de alojamiento admite distintos servicios adicionables por el cliente:
 * por ejemplo: masajes.
 * 
 */
public class Reserva implements Serializable {
	private static final long serialVersionUID = 1L;



	// ATRIBUTOS
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

	/*
	 * Metodo devuelve la lista de habitaciones en un formato mas legible para
	 * mostrarlo en la interfaz
	 */
	public String listaHabitaciones() {
		Iterator<Lugar> iterator = habitaciones.iterator();
		StringBuffer lista = new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.getNumero() + " " + habitacion.getTipo() + "\n");
		}
		return lista.toString();
	}


	/*
	 * toString encargado de mostrar la lista de habitaciones de manera más legible
	 * para ser mostrada en la interfaz
	 */
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

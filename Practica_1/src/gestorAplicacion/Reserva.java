package gestorAplicacion;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;


public class Reserva {
	private Factura factura;
	private Date fechaEntrada;
	private Date fechaSalida;
	private float aporte;
	private Usuario cliente;
	private List<Lugar> habitaciones = new ArrayList<Lugar>();
	
	
	//CONSTRUCTOR
	public Reserva(Factura factura, String fechaEntrada, String fechaSalida, List<Lugar> habitaciones,float aporte, Usuario cliente) {
		SimpleDateFormat fecha = new SimpleDateFormat("dd/MM/yyyy");
		Date fEntrada=new Date();
		try {
			fEntrada = fecha.parse(fechaEntrada);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		Date fSalida=new Date();
		try {
			fSalida = fecha.parse(fechaSalida);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		this.factura=factura;
		this.fechaEntrada=fEntrada;
		this.fechaSalida=fSalida;
		this.aporte=aporte;
		this.cliente=cliente;
		this.habitaciones=habitaciones;
	}
	
	//METODOS
	public String listaHabitaciones() {
		Iterator<Lugar> iterator = habitaciones.iterator();
		StringBuffer lista=new StringBuffer();
		while (iterator.hasNext()) {
			Lugar habitacion = (Lugar) iterator.next();
			lista.append(habitacion.numero+" "+habitacion.tipo+"\n");
		}
		return lista.toString();
	}
	
	//GETTERS Y SETTERS
	public Factura getFactura() {
		return factura;
	}
	public void setFactura(Factura factura) {
		this.factura = factura;
	}
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
	
	public String toString() {
		String habitaciones=listaHabitaciones();
		return "la reserva se hizo a nombre de: "+ cliente.nombre + " Entre los dias: " + getFechaEntrada() + " y " + getFechaSalida()+ " para las habitaciones:\n"+ habitaciones;
	}

	public List<Lugar> getHabitaciones() {
		return habitaciones;
	}

	public void setHabitaciones(List<Lugar> habitaciones) {
		this.habitaciones = habitaciones;
	}
	
	
	
}

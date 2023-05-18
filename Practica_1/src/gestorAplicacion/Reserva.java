package gestorAplicacion;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.Date;

public class Reserva {
	private Factura factura;
	private Date fechaEntrada;
	private Date fechaSalida;
	private float aporte;
	private Usuario cliente;
	
	
	
	//CONSTRUCTOR
	public Reserva(Factura factura, String fechaEntrada, String fechaSalida, float aporte, Usuario cliente) {
		SimpleDateFormat fecha = new SimpleDateFormat("dd/MM/yyyy");
		Date fEntrada=new Date();
		try {
			fEntrada = fecha.parse(fechaEntrada);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Date fSalida=new Date();
		try {
			fSalida = fecha.parse(fechaSalida);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.factura=factura;
		this.fechaEntrada=fEntrada;
		this.fechaSalida=fSalida;
		this.aporte=aporte;
		this.cliente=cliente;
	}
	
	//METODOS
	
	
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
	public void setCliente(Usuario cliente) {
		this.cliente = cliente;
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
		return "Entre los dias: " + getFechaEntrada() + " y " + getFechaSalida();
	}
	
}

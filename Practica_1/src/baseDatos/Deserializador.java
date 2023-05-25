package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.List;
import java.util.Set;

import uiMain.*;
import gestorAplicacion.*;

public class Deserializador {
	private static File ruta = new File("src\\baseDatos\\temp");
	@SuppressWarnings("unchecked")

	public static void deserializar(Almacenamiento almacenamiento) {
		File[] docs = ruta.listFiles();
		FileInputStream fis;
		ObjectInputStream ois;

		for (File file : docs) {
			if (file.getAbsolutePath().contains("usuarios")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaUsuarios((List<Usuario>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("empleados")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaEmpleados((List<Empleado>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("habitaciones")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaHabitaciones((List<Lugar>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("lugares")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaLugares((List<Lugar>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("servicios")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaServicios((List<Servicio>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("reservas")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaReservas((List<Reserva>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("eventos")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaEventos((List<Evento>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("facturas")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaFacturas((List<Factura>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("serviciosExternos")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					Almacenamiento.setListaServiciosExternos((List<ServicioExterno>) ois.readObject());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		}
	}
}
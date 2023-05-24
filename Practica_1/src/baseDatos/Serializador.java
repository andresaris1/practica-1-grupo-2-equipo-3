package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import uiMain.*;

public class Serializador {
	private static File ruta = new File("src\\baseDatos\\temp");

	public static void serializar(Main main) {
		FileOutputStream fos;
		ObjectOutputStream oos;
		File[] docs = ruta.listFiles();
		PrintWriter pw;

		// Limpia los archivos para evitar copias de informacion
		for (File file : docs) {
			try {
				pw = new PrintWriter(file);

			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		//bucle para serializar cada lista de objetos

		for (File file : docs) {
			if (file.getAbsolutePath().contains("usuarios")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaUsuarios());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("empleados")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaEmpleados());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("habitaciones")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaHabitaciones());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("lugares")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaLugares());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("servicios")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaServicios());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("serviciosExternos")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaServiciosExternos());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}else if (file.getAbsolutePath().contains("reservas")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaReservas());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("eventos")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(Almacenamiento.getListaEventos());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}

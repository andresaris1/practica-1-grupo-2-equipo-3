package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import uiMain.*;
import gestorAplicacion.*;

public class Deserializador {
	private static File ruta = new File("src\\baseDatos\\temp");

	public static void deserializar(Main main) {
		File[] docs = ruta.listFiles();
		FileInputStream fis;
		ObjectInputStream ois;

		for (File file : docs) {
			if (file.getAbsolutePath().contains("clientes")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream(fis);

					main.setClientes((ArrayList<Usuario>) ois.readObject());
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

					main.setFacturas((ArrayList<Factura>) ois.readObject());
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

					main.setReservas((ArrayList<Reserva>) ois.readObject());
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
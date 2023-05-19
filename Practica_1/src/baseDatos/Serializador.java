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

		for (File file : docs) {
			try {
				pw = new PrintWriter(file);

			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		for (File file : docs) {
			if (file.getAbsolutePath().contains("clientes")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(main.getClientes());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("facturas")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(main.getFacturas());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("reservas")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(main.getReservas());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}

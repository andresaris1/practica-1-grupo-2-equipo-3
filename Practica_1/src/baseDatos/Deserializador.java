package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.List;
import gestorAplicacion.*;

public class Deserializador {
	private static File ruta=new File("src\\baseDatos\\temp");
	
	public static void deserializar(Reserva reserva) {
		File[] docs = ruta.listFiles();
		FileInputStream fis;
		ObjectInputStream ois;
	
	for (File file:docs) {
		if (file.getAbsolutePath().contains("cliente")) {
			try {
				fis = new FileInputStream(file);
				ois = new ObjectInputStream(fis);
				
				reserva.setCliente((List<Cliente>) ois.readObject();
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			} catch (ClassNotFoundException e) {
				e.printStackTrace();
			}
		} else if (file.getAbsolutePath().contains("factura")) {
			try {
				fis = new FileInputStream(file);
				ois = new ObjectInputStream(fis);
				
				reserva.setFactura((List<Factura>) ois.readObject();
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
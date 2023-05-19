package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import gestorAplicacion.*;

public class Serializador {
	private static File ruta=new File("src\\baseDatos\\temp");
	
	public static void serializar(Reserva reserva) {
		FileOutputStream fos;
		ObjectOutputStream oos;
		File[] docs = ruta.listFiles();
		PrintWriter pw;
		
	for (File file:docs) {
		try {
			pw = new PrintWriter(file);
			
		}catch(FileNotFoundException e){
			e.printStackTrace();
		}
	}
	
	for (File file:docs) {
		if (file.getAbsolutePath().contains("cliente")) {
			try {
				fos = new FileOutputStream(file);
				oos = new ObjectOutputStream(fos);
				oos.writeObject(reserva.getCliente());
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else if (file.getAbsolutePath().contains("factura")) {
			try {
				fos = new FileOutputStream(file);
				oos = new ObjectOutputStream(fos);
				oos.writeObject(reserva.getFactura());
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	}
}
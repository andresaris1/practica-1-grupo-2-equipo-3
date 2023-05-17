package uiMain;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

import gestorAplicacion.Usuario;
import uiMain.Main;
import gestorAplicacion.*;

public class Menu {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("-- - - FUNCIONALIDADES - - - -");
        System.out.println("1.Reservar Alojamiento");
        System.out.println("2.Reservar Turística");
        System.out.println("3.Reservar Evento");
        System.out.println("4.Cobro");
        System.out.println("5.Mostrar información de habitaciones");

        System.out.println("Eliga una opción: ");
        int opcion = sc.nextInt();

        switch (opcion) {
            case 1:
                // Codigo de la funcionalidad reserva
                break;
            case 2:
                System.out.println("Ingrese la identificacion del usuario: ");
                String id = sc.next();

                break;
            case 3:
                // Codigo de la funcionalidad reserva de tours
                break;
            case 4:
                // Codigo para la funcionalidad Reserva de eventos
                System.out.println("Escribe tu identificacion: ");
                id = sc.next();
                System.out.println("Escribe el lugar en el que desea su evento: ");
                System.out.println("1. Terraza");
                System.out.println("2. Piscina");
                System.out.println("3. Salon de eventos");
                System.out.println("4. Gran salón de eventos");
                int tipoLugar = sc.nextInt();

                
                HashMap<String, Integer> empleadosNecesarios = new HashMap<String, Integer>();
                
                System.out.println("¿Cuántos cocineros requiere?");
                empleadosNecesarios.put("Chefs", sc.nextInt());

                System.out.println("¿Cuántos meseros requiere?");
                empleadosNecesarios.put("Meseros", sc.nextInt());
                
                System.out.println("¿Cuántos bartenders requiere?");
                empleadosNecesarios.put("Bartender", sc.nextInt());

                
                break;
            case 5:
                // codigo para la funcionalidad de cobro
                break;
            case 6:
                // Codigo para la funcionalidad de mostrar informacion de habitaciones
                break;

            default:
                System.out.println("Opcion Invalida");
                break;
        }

        sc.close();

    }
}
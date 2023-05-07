package uiMain;

import java.util.Scanner;

public class Menu {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("- - - FUNCIONALIDADES - - - -");
        System.out.println("1.Reserva");
        System.out.println("2.Pagos");
        System.out.println("3.Tours");
        System.out.println("4.Adicion servicios");
        System.out.println("5.Check In");
        System.out.println("6.Check out");

        System.out.println("Eliga una opción: ");
        int opcion = sc.nextInt();

        switch (opcion) {
            case 1:
                // Codigo de la funcionalidad reserva
                break;
            case 2:
                // codigo de cobros
                break;
            case 3:
                // Codigo de la funcionalidad reserva de tours
                break;
            case 4:
                // Codigo para la funcionalidad de agregar servicios
                break;
            case 5:
                // codigo para check in
                break;
            case 6:
                // Codigo para check out
                break;

            default:
                System.out.println("Opcion Invalida");
                break;

        }
        sc.close();
    }
}
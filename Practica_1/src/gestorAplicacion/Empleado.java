package gestorAplicacion;

public class Empleado extends Persona{
    String cargo;
    int comision;
    int nomina; //Valor prestablecido

    //METODOS 

    //CONSTRUCTOR
    
    

    //GETTERS AND SETTERS
    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public int getComision() {
        return comision;
    }

    public void setComision(int comision) {
        this.comision = comision;
    }

    public int getNomina() {
        return nomina;
    }

    public void setNomina(int nomina) {
        this.nomina = nomina;
    }

    

    

    
}

package gestorAplicacion;

public enum Destinos {
    TORRE_EIFFEL(60),
    MUSEO_LOUVRE(80),
    ARCO_TRIUNFO(50),
    NOTRE_DAME(70),
    PALACIO_VERSALLES(90);
    COMBO_SIMPLE_TRAE_DESTINOS_1Y3(100),
    COMBO_NORMAL_TRAE_DESTINOS_2Y4(140),
    COMBO_COMPLETO_TRAE_TODOS(320),
    

    private int valor;

    private Destinos(int valor) {
        this.valor = valor;
    }

    public int getValor() {
        return valor;
    }


}
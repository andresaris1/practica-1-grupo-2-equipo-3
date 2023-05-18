package gestorAplicacion;

public enum Destinos {
    TORRE_EIFFEL(60),
    MUSEO_LOUVRE(80),
    ARCO_TRIUNFO(50),
    NOTRE_DAME(70),
    PALACIO_VERSALLES(90);

    private int valor;

    private Destinos(int valor) {
        this.valor = valor;
    }

    public int getValor() {
        return valor;
    }
}

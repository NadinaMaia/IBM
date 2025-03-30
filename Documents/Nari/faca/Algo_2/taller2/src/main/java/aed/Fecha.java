package aed;

public class Fecha {
    private int dia;
    private int mes;

    public Fecha(int x, int y) {
        this.dia = x;
        this.mes = y;
    }

    public Fecha(Fecha fecha) {
        this.dia = fecha.dia;
        this.mes = fecha.mes;
    }

    public Integer dia() {
        return dia;
    }

    public Integer mes() {
        return mes;
    }

    @Override
    public String toString() {
        return dia + "/" + mes;
    }

    @Override
    public boolean equals(Object otra) {
        boolean otroEsNull = (otra==null);

        boolean esFecha = (otra.getClass() == this.getClass());

        if (otroEsNull || esFecha==false){
            return false;
        }
        else{
            Fecha fechadistinta = (Fecha) otra;
            return fechadistinta.dia == this.dia && fechadistinta.mes == this.mes;
        }
    }

    public void incrementarDia() {
        int max = diasEnMes(mes);
        if (dia == max){
            dia = 1;
            if (mes == 12){
                mes = 1;
            }
            else{
                mes += 1;
            }
        }
        else{
            dia += 1;
        } 
    }

    private int diasEnMes(int mes) {
        int dias[] = {
                // ene, feb, mar, abr, may, jun
                31, 28, 31, 30, 31, 30,
                // jul, ago, sep, oct, nov, dic
                31, 31, 30, 31, 30, 31
        };
        return dias[mes - 1];
    }
}

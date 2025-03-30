package aed;

public class Agenda {
    private Fecha fecha;
    private ArregloRedimensionableDeRecordatorios recordatorios;

    public Agenda(Fecha fechaActual) {
        this.fecha = fechaActual;
        this.recordatorios = new ArregloRedimensionableDeRecordatorios();
    }

    public void agregarRecordatorio(Recordatorio recordatorio) {
        recordatorios.agregarAtras(recordatorio);
    }

    @Override
    public String toString() {
        StringBuilder MostrarRecordatorios= new StringBuilder();

        for(int j = 0; j < recordatorios.longitud(); j++){
            Recordatorio puntero = recordatorios.obtener(j);
            if (puntero.fecha().equals(fecha)){
                if(MostrarRecordatorios.length() > 0){
                    MostrarRecordatorios.append("\n");
                }
                MostrarRecordatorios.append(puntero.toString());
            }
        }
        return fechaActual() + "\n" + "=====" + "\n" + MostrarRecordatorios.toString() + "\n";
    }

    public void incrementarDia() {
        this.fecha.incrementarDia();
    }

    public Fecha fechaActual() {
        int dia = this.fecha.dia();
        int mes = this.fecha.mes();
        Fecha fechaactual = new Fecha(dia, mes);
        return fechaactual;
    }
}
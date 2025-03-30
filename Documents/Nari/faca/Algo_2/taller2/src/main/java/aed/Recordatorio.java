package aed;

public class Recordatorio {
    private String mensaje;
    private Fecha fecha;
    private Horario horario;

    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
         this.mensaje = mensaje;
         this.fecha = new Fecha(fecha);
         this.horario = new Horario(horario);
    }

    public Horario horario() {
        return horario;
    }

    public Fecha fecha() {
        return new Fecha(this.fecha);
    }

    public String mensaje() {
        return mensaje;
    }

    @Override
    public String toString() {
        return mensaje + " @ " + fecha + " " + horario;
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull = otro==null;

        boolean esRecordatorio = otro.getClass() == this.getClass();

        if (otroEsNull || esRecordatorio==false){
            return false;
        }
        else{
            Recordatorio recdist = (Recordatorio) otro;
            return recdist.fecha.equals(this.fecha) &&
                   recdist.mensaje.equals(this.mensaje) &&
                   recdist.horario.equals(this.horario);
        }
    }
}

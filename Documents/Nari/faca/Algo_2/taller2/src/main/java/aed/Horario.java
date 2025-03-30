package aed;

public class Horario {
    private int hora;
    private int minutos;

    public Horario(int x, int y) {
        hora = x;
        minutos = y;
    }

    public Horario(Horario ingresaHorario) {
        this.hora = ingresaHorario.hora;
        this.minutos = ingresaHorario.minutos;
    }

    public int hora() {
        return hora;
    }

    public int minutos() {
        return minutos;
    }

    @Override
    public String toString() {
        return hora + ":" + minutos;
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull = otro==null;
    
        boolean claseDistinta = otro.getClass() != this.getClass();
        
        if (otroEsNull || claseDistinta){
            return false;
        }  
        else{
            Horario horariodistinto = (Horario) otro;
            return horariodistinto.minutos == this.minutos && horariodistinto.hora == this.hora;
        }
    }
}

package aed;

class ArregloRedimensionableDeRecordatorios {
    private Recordatorio[] arreglo;

    public ArregloRedimensionableDeRecordatorios() {
        arreglo = new Recordatorio[0];
    }

    public int longitud() {
        return arreglo.length;
    }

    public void agregarAtras(Recordatorio i) {
        Recordatorio[] nuevoArreglo = new Recordatorio[arreglo.length + 1];

        for (int j = 0; j < arreglo.length ; j++){
            nuevoArreglo[j] = arreglo[j];
        }
        
        nuevoArreglo[arreglo.length] = i;

        arreglo = nuevoArreglo;
    }

    public Recordatorio obtener(int i) {
        return this.arreglo[i];
    }

    public void quitarAtras() {
        Recordatorio[] nuevoArreglo = new Recordatorio[arreglo.length -1];

        for (int j = 0; j < nuevoArreglo.length ; j++){
            nuevoArreglo[j] = arreglo[j];
        }

        arreglo = nuevoArreglo;
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        arreglo[indice]=valor;
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        arreglo = new Recordatorio[vector.longitud()];
        for (int j = 0; j < vector.longitud() ; j++){
            arreglo[j] = vector.obtener(j);
        }
    }

    public ArregloRedimensionableDeRecordatorios copiar() {
        ArregloRedimensionableDeRecordatorios nuevoArreglo = new ArregloRedimensionableDeRecordatorios();

        for (int j = 0; j < longitud() ; j++){
            nuevoArreglo.agregarAtras(obtener(j));
        }
        return nuevoArreglo;
    }
}
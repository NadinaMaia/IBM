package aed;

import java.util.*;

public class ListaEnlazada<T> implements Secuencia<T> {
    private Nodo primero;
    private Nodo ultimo;
    private int longitud;
    
    private class Nodo {
        int valor;
        Nodo sig; //uno este nodo con su siguiente
        Nodo ant; //uno este nodo con su anterior
    }

    public ListaEnlazada() {
        throw new UnsupportedOperationException("No implementada aun");
    }

    public int longitud() {
        return longitud;
    }

    public void agregarAdelante(T elem) {
        //creamos el nuevo elemento
        nuevo.valor = elem;
        
        nuevo.sig = this.primero;
        nuevo.ant = null;
        //ponemos este nuevo elemento como el primero 
        this.primero = nuevo;
        //agregamos uno a la longitud
        this.longitud += 1;

    }

    public void agregarAtras(T elem) {
        nuevo.valor = elem;
        nuevo.sig = null;
        nuevo.ant = this.ultimo;
        this.ultimo = nuevo;
        this.longitud += 1;
    }

    public T obtener(int i) {
        int contador = 0;
        actual = this.primero;
        while (contador < i){
            actual = actual.siguiente;
            contador ++;    
            }
        return actual.valor;
        }
    }

    public void eliminar(int i) {
        if (i == 0){
            this.primero = primero.sig
            primero.ant = null;
        }
        if (i == longitud-1){
            this.ultimo = ultimo.ant;
            ultimo.sig = null;
        }
        else{
            //obtenemos nodo que hay que eliminar
            nodoABorrar = obtener(i);
            //obtenemos nodo anterior y siguiente
            nodoAnterior = nodoABorrar.ant;
            nodoSiguiente = nodoABorrar.sig;
            //modificamos los nodos anteriores y siguientes para desvincularlos
            nodoAnterior.sig = nodoABorrar.sig;
            nodoSiguiente.ant = nodoABorrar.ant;
            } 
        }
    }

    public void modificarPosicion(int indice, T elem) {
        modificar = obtener(indice);
        modificar.valor = elem;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        throw new UnsupportedOperationException("No implementada aun");
    }
    
    @Override
    public String toString() {
        throw new UnsupportedOperationException("No implementada aun");
    }

    private class ListaIterador implements Iterador<T> {
    	// Completar atributos privados

        public boolean haySiguiente() {
	        return ListaIterador.sig != null;
        }
        
        public boolean hayAnterior() {
	        return ListaIterador.ant != null;
        }

        public T siguiente() {
	        ListaIterador = ListaIterador.sig;
            return ListaIterador.valor;
        }
        
        public T anterior() {
	        ListaIterador = ListaIterador.ant;
            return ListaIterador.valor;
        }
    }

    public Iterador<T> iterador() {
	    throw new UnsupportedOperationException("No implementada aun");
    }

}

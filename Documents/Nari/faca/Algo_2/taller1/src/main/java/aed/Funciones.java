package aed;

class Funciones {
    int cuadrado(int x) {
        int res;

        res = x*x;
        return res;
    }

    double distancia(double x, double y) {
        double res;

        res = java.lang.Math.sqrt(x*x + y*y);

        return res;
    }

    boolean esPar(int n) {
    return n%2==0;
    }

    boolean esBisiesto(int n) {
        return (n % 4 == 0 && n % 100 != 0) || (n % 400 == 0);
    }

    int factorialIterativo(int n) {
        int factorial = 1;
        for(int i=1; i<=n; i++){
            factorial = factorial*i;
        }
        return factorial;
    }

    int factorialRecursivo(int n) {
        if (n==0)
            return 1;
        else
            return n*factorialRecursivo(n-1);
    }

    boolean esPrimo(int n) {
        int contador = 0;
        for(int i = 0 ; i < n; i++){
            if(n % i == 0){
                contador += 1;
            }
        }
        return contador == 2;
    }

    int sumatoria(int[] numeros) {
        int suma = 0;
        for(int i = 0; i < numeros.length; i++){
            suma += numeros[i];
        }
        return suma;
    }

    int busqueda(int[] numeros, int buscado){
        for(int i = 0; i < numeros.length; i++){
            if(numeros[i] == buscado)
                return i;
        }
        return -1;
    }

    boolean tienePrimo(int[] numeros) {
        for(int i = 0; i < numeros.length; i++){
            if(esPrimo(numeros[i])){
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for(int i = 0; i < numeros.length; i++){
            if(esPar(numeros[i])== false){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        int largo = s1.length();
        String subcadena = s2.substring(0, largo);
        if(s2 != subcadena){
            return false;
        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        int largo = s1.length();
        String subcadena = s2.substring(s2.length() - largo, s2.length());
        if(s2 != subcadena){
            return false;
        }
        return true;
    }
    
    }

import math as math

#%%Ejercicio 1.1
def imprimir_hola_mundo() -> None:
    print("Hola mundo")

# /n = renglon abajo
#%%Ejercicio 1.3
def raizDe2() -> int:
    print(round(math.sqrt(2),4))

#%%Ejercicio 1.5
def perimetro(radio) -> int:
    print(math.pi*(radio*2))

## int(numero) = transforma a entero un string 

#%%Ejercicio 2.1
def imprimir_saludo(nombre: str) -> None:
    print("Hola " + nombre)

##global x -> me dice que x es una variable global, por mas que este definida dentro de una funcion

#%%Ejercicio 2.2
def raiz_cuadrada_de(numero: int) -> float:
    raiz = round(math.sqrt(numero),2)
    print(raiz)

#%%Ejercicio2.3
def fahrenheit_a_celsius(t: float) -> float:
    cuenta = ((t - 32)*5)/9
    print(cuenta)

#%%Ejercicio 2.4
def imprimir_dos_veces(estribillo: str) -> str:
    estribillo_doble = estribillo*2
    print(estribillo_doble)

#%%Ejercicio 2.5
def es_multiplo_de(n:int, m:int) -> bool:
    if n % m == 0 :
        valor = True
    else:
        valor = False
    return(valor)

# input -> imprime y espera que ls persona lo complete

#%%Ejercicio 2.6
def es_par(numero:int) -> bool:
    if es_multiplo_de(numero, 2) == True:
        valor = True
    else:
        valor = False
    return (valor)

#%%Ejercicio 2.7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones:int) -> int: 
    cant_pizzas = 1
    while ((cant_pizzas*8) // comensales) < min_cant_de_porciones:
        cant_pizzas = cant_pizzas + 1
    return(cant_pizzas)

#%% Ejercicio 3.1
def alguno_es_0(numero1: int, numero2: int) -> bool:
    if numero1 == 0:
        return True
    elif numero2 == 0:
        return True
    else: 
        return False 
#%% Ej 3.2
def ambos_son_0(numero1: int, numero2: int) -> bool:
    if numero1 == 0 and numero2 == 0:
        return True
    else: 
        return False

#%% Ej 3.3
def es_nombre_largo(nombre: str) -> bool:
    input("Ingrese un nombre: ")
    if len(input)<= 8 or len(input)>= 3 :
        return True
    else:
        return False

#%% Ej 3.4
def es_bisiesto(año: int) -> bool:
    if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0):
        return True
    else: 
        return False

#%%  Ej 4
def peso_pino(altura_m: float) -> float:
    altura_cm = altura_m * 100
    if altura_cm <= 300:
        peso = 3*altura_cm
    else:
        altura_mayor_300 = altura_cm - 300
        peso = altura_mayor_300*2 + 900
    return peso

def es_peso_util(peso:float) -> bool:
    if peso <= 1000 and peso >= 400:
        return True
    else:
        return False
    
def sirve_pino(altura:float) -> bool:
    sirve = es_peso_util(peso_pino(altura))
    return sirve

#%% Ej 5.1
def devolver_el_doble_si_es_par(numero:int) -> int:
    if numero % 2 == 0:
        return numero*2
    else: 
        return (str(numero) + " no es par")
# si quiero que le ingrese un numero int o float
# hace falta un else



#%% Ej 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

#%% Ej 5.3
def devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero):
    if numero % 9 == 0:
        return numero*3
    elif numero % 3 == 0:
        return numero*2 #creo que va primero el de 9 
    else:
        return numero

#%% Ej 5.4
def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos de 5 letras"
    
#%% Ej 5.5
def elRango(numero:int) -> str:
    if numero > 20:
        return "Mayor a 20"
    elif numero < 5:
        return "Menor a 5"
    elif numero >= 10 and numero <= 20:
        return "Entre 10 y 20"
    else:
        return "No se especifico"

#%% Ej 6.1
def imprimir_del_1_al_10():
    contador = 1
    while contador <= 10:
            print(contador)
            contador = contador + 1

#%% Ej 6.2
def imprimir_pares(base:int, tope:int):
    maximo = tope
    numeros= []
    for i in range (base, tope, 2):
        numeros.append(i)
    return numeros

#%%  Ej 6.3
def cuenta_regresiva(empezar):
    conteo = empezar
    while conteo > 0:
        print(conteo)
        conteo = conteo - 1
    print("despegar!")

#%% Ej 6.6
def viaje_en_el_tiempo()-> None:
    partida:int = int(input("ingrese año de partida: ")) 
    while partida > 384:
        print("Viajo 20 años al pasado, estamos en el año: " + str(partida))
        partida -= 20 
    print("usted viajo al " + str(partida))

print(viaje_en_el_tiempo())

##Que es la ejecucion simbolica
    
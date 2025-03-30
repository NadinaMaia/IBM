import numpy as np
import random
#%% Ej 1.1
def pertenece(s:[int], e:int)-> bool:
    for i in range(len(s)):
        if s[i] == e:
            pertenece= True
            break
        else:
            pertenece= False
    return pertenece

#%% Ej 1.2
def divideATodos(s:[int], e: int) -> bool:
    for elemento in s:
        if elemento % e == 0:
            divide = True
        else: 
            divide = False
    return divide

#%% Ej 1.3
def sumaTotal(s: [int]) -> int:
    sumatoria:int = 0
    for elemento in s:
        sumatoria= sumatoria + elemento
    return sumatoria

#%% Ej 1.4
def ordenados(s:[int]) -> bool:
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            ordenados = True
        else:
            ordenados = False
    return ordenados

#%% Ej 1.5
def palabras_largas(lista:[int])-> bool:
    larga = False
    for palabra in lista:
        if len(palabra) >= 7:
            larga = True
            break
        else:
            larga = False
    return larga

#%% Ej 1.6
def invertir_cadena(cadena:str) -> str:
    return cadena[::-1]

def palindromo(palabra: str)->bool:
    if palabra == invertir_cadena(palabra):
        return True
    else:
        return False
    
#%% Ej 1.7
def hay_minus(contraseña:str)-> bool:
    for letra in contraseña:
        if 'a' <= letra <= 'z' or letra=='ñ':
            return True
    return False
    
def hay_mayus(contraseña:str)-> bool:
    for letra in contraseña:
        if 'A' <= letra <= 'Z' or letra=='Ñ':
            return True
    return False
    
def hay_numero(contraseña:str)-> bool:
    for letra in contraseña:
        if '0' <= letra <= '9':
            return True
    return False

def contraseña_segura(contraseña:str)-> str:
    if len(contraseña)<5:
        return 'rojo'
    elif len(contraseña)>8 and hay_mayus(contraseña) ==True and hay_minus(contraseña) == True and hay_numero(contraseña)==True:
        return 'verde'
    else:
        return 'amarillo'

#%% Ej 9
def tiene_repetidos(lista:[str])-> bool:
    repeticiones = 0
    for evaluar in lista:
        for elemento in lista:
            if evaluar == elemento:
                repeticiones += 1
        if repeticiones > 1:
            return True
        else: 
            return False
        
def tiene_vocales(palabra: str)-> bool:
    vocales = ['a','e','i','o','u']
    vocales_hay = []
    for letra in palabra:
        if pertenece(vocales, letra):
            vocales_hay.append(letra)
    if len(vocales_hay) >= 3 and tiene_repetidos(vocales_hay) == False:
        return True
    else:
        return False

#%% Ej 2.2.1
def quitar_pares(lista:[int]) -> [int]:
    largo_lista = len(lista)
    for i in range(1,largo_lista,2):
        lista[i] = 0
    return lista
    
#%% Ej 2.2.3
def es_vocal(letra:str)-> bool:
    vocales = ["a","e","i","o","u"]
    for i in range(len(vocales)):
        if letra == vocales[i]:
            res = True
            break
        else:
            res = False
    return res

def borrar_vocales(palabra: str) -> str:
    res:str = ""
    for i in range(len(palabra)):
        if es_vocal(palabra[i]) == False: 
                res += palabra[i]
    return res

def reemplazaVocales(palabra:[chr])-> [chr]:
    resultado = []
    for letra in palabra:
        if es_vocal(letra):
            resultado += "_"
        else:
            resultado += letra
    return resultado

#%% 2.2.4
def reemplazaVocales1(palabra:[chr])->[chr]:
    salida:[chr]=[]
    for i in range(0,len(palabra)):
        if (es_vocal(palabra[i])):
            salida+=" "
        else:
            salida+=palabra[i]
    return salida

#%% Ej 2.2.5
def daVueltaStr(palabra:str)->str:
    salida:str= ""
    long=len(palabra)
    for i in range(long-1,-1,-1):
        salida+=palabra[i]
    return salida
print(daVueltaStr("hola"))

#%% Ej 2.2.6
def eliminarRepetidos(palabra:[chr])-> [chr]:
    return True

#%% Ej 2.3
def aprobado(notas:[int])-> int:
    promedio = promediar(notas)
    if son_aprobadas(notas) == True:
        if promedio >= 7:
            res = 1
        else:
            res = 2
    else:
        res = 3
    return res

#%%
def estudiantes()->[str]:
    res:[str]=[]
    nombre=""
    while(nombre!="listo"):
        nombre=input("Ingrese un nombre: ")
        if(nombre!='listo'):
            res.append(nombre)
    return res

#%% Ej 4.2
def historial_sube():
    saldo = 0
    movimientos = []
    movimiento = ""
    while movimiento != "X":
        movimiento = input("C,  D,  X :")
        if movimiento == "C":
            monto = input("ingrese monto a cargar: ")
            registro = ["C", monto]
            movimientos.append(registro)
        elif movimiento == "D":
            monto = input("ingrese monto a descontar: ")
            registro = ["D", monto]
            movimientos.append(registro)
    return movimientos

def promediar(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += lista[i]
    return (sumatoria/len(lista))

def son_aprobadas(calificaciones):
    son = True
    for i in range(len(calificaciones)):
        if calificaciones[i] < 4:
            son = False
    return son

#%% Ej 2.4.3
def tirar_carta()->int:
    cartas = [1,2,3,4,5,6,7,10,11,12]
    carta = random.choice(cartas)
    return carta

def puntos(lista):
    puntos = 0
    cond_especiales = [10,11,12]
    for elemento in lista:
        if pertenece(cond_especiales,elemento): 
            puntos += 0.5
        else:
            puntos += elemento
    return puntos

def jugar():
    puntos_jug = 0
    cartas_jugador = []
    preguntar = input("Desea tirar una carta? (si/no): ")
    while preguntar == "si":
        tirada = tirar_carta()
        print("Te salio la carta " + str(tirada))
        cartas_jugador.append(tirada)
        print("tus cartas son:" + str(cartas_jugador))
        puntos_jug = puntos(cartas_jugador)
        if puntos_jug > 7.5:
            print("perdiste :/")
            break
        elif puntos_jug == 7.5:
            print("ganaste 1 millon de dolares =D!!!")
            break
        else:
            print("tus puntos son " + str(puntos_jug))
            preguntar = input("Desea tirar otra carta? (si/no): ")
    print("tus puntos son " + str(puntos_jug))
    return "Fin del juego"

#%% Ej 2.5.1
def perteneceACadaUno(s: [[int]], e:int, res:[bool])-> None:
    res = []
    for lista in s:
        if pertenece(lista, e):
            res.append(True)
        else:
            res.append(False)
    return res

#%% Ej 2.5.4
def matriz(d):
    m = np.random.randint(1,10,(d,d))
    return m
#5.2
def esMatrizCuadrada(input:[[int]])->bool:
    for i in range (0,len(input)):
        if (len(input)!=len(input[i])):
            return False
    return True



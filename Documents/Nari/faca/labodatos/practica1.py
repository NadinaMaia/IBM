#%%Ej 1
def pasar_obelisco(espesor:float, objetivo:float):
    espesor_metros = espesor * 0.001
    altura = 0 
    billete_por_dia = 0
    while altura < objetivo:
        billete_por_dia += 1
        altura = billete_por_dia*espesor_metros
    print("tomaron " + str(billete_por_dia) + " dias en pasar el objetivo")

#%% Ej 2
def rebotes(altura_inicial:int):
    contador = 1
    altura_actual = altura_inicial
    while altura_actual > 0 and contador <= 10:
        print(str(contador) + " " + str(altura_actual))
        altura_actual = 0.6 * altura_actual
        contador += 1

#%% Ej 3 
def frase_neutra(frase):
    vocales = ["a","e","i","o","u"]
    palabras = frase.split(" ")
    frase_t_lista = []
    for palabra in palabras:
        ultima_posicion = len(palabra) - 1 # posicion de la ultima letra
        ultima_letra = palabra[ultima_posicion] # letra de la ultima posicion
        ante_ultima = ultima_posicion - 1
        if ultima_letra in vocales:
            palabra_t = palabra[:ultima_posicion] + "e"
            frase_t_lista.append(palabra_t)
        elif palabra[ante_ultima] in vocales:
            palabra_t = palabra[:ante_ultima] + "e" + palabra[ultima_posicion]
            frase_t_lista.append(palabra_t)
        else:
            frase_t_lista.append(palabra)
    ##reconstruccion de frase
    frase_t = ""
    for palabra in frase_t_lista:
        frase_t = frase_t + " " + palabra
    
    print(frase_t)

#%% Ej 4
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

#%% Ej 5
def dos_pertenece(lista):
    if 2 in lista:
        return True
    else:
        return False
 #%% Ej 6
def pertenece(lista, elem):
     if elem in lista:
         return True 
     else:
         return False

#%% Ej 7
def mas_larga(lista1, lista2):
    if len(lista1) > len(lista2):
        return lista1
    else:
        return lista2

#%% Ej 8
def cant_e(lista):
    contador = 0
    for caracter in lista:
        if caracter == "e":
            contador += 1
    return contador

#%% Ej 9
def sumar_unos(lista):
    for i in range(len(lista)):
        lista[i] += 1
    return lista

#%% Ej 10
def mezclar(cadena1, cadena2):
    res = ""
    contador = 0
    cadena_mas_larga =  mas_larga(cadena1, cadena2)
    while contador < len(cadena_mas_larga):
        res = res + cadena1[contador] + cadena2[contador]
        contador += 1
    return res   
        
#%% Diapositiva 20

vocales = ["a","e","i","o","u"]

def traductor_geringoso(lista):
    lista_t = []
    for palabra in lista:
        palabra_t = ""
        for letra in palabra:
            if letra in vocales:
                palabra_t = palabra_t + letra + "p" + letra
            else:
                palabra_t = palabra_t + letra
        lista_t.append(palabra_t)
    dic_traductor = dict(zip(lista,lista_t))
    print(dic_traductor)

## zip empareja primer elemento con primer elemento, segundo con segundo, etc


#with open(r'C:\Users\soler\Documents\Nari\faca\labodatos\Clase 02 - archivos-20240131\datame.txt', 'rt', encoding='utf-8') as file:
#    data = file.read() 
#file.close() 
#data 
#print(data)

################################ porque es necesario el csv.reader
import csv

ruta_archivo = r'C:\Users\soler\Documents\Nari\faca\labodatos\Clase 02 - archivos-20240131\cronograma_sugerido.csv'    
def registros(nombre_archivo):    
    lista = []    
    with open(nombre_archivo, 'rt',encoding='utf-8') as f:        
        filas = csv.reader(f)        
        encabezado = next(filas)        
        for fila in filas:            
            registro = dict(zip(encabezado,fila)) # armo el diccionario de cada fila            
            lista.append(registro)          # lo agrego a la lista    
    return lista

#%% diapo 34
import random

def generarala_tirar():
    res = []
    for i in range(5):
        tirada = random.randint(1, 6)
        res.append(tirada)
    return res

################################ como hago para que tome (1,2,3) == (3,2,1) para la full
################################ diapo 34, cronograma sugerido
################################ lo de utf-8 les pasa en otras compus o es solo en la mia?
################################ donde le dice que lo separe por coma en el csv?
################################ los limites suelen estar incluidos?
#%% diapo 34
def materias_cuatrimestre(nombre_archivo,n):
    lista = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        filas = csv.reader(file)
        encabezado = next(filas)
        for fila in filas:
            diccionario = dict(zip(encabezado, fila))
            if diccionario[encabezado[0]] == str(n):
                lista.append(diccionario)
    return lista

#%% diapo 40
import numpy as np

vector = np.arange(2,20,2)

vector = np.linspace(2,20,10)

a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))


################################## expliquen porfa lo de abajo 
################################## quien es directorio

import pandas as pd 

import os 

archivo = 'arbolado-en-espacios-verdes.csv' 

fname = os.path.join(directorio,archivo) 

df = pd.read_csv(fname)

print(df.head())

################################## cuando pide crear un dataframe de jacaranda, se refiere a .copy() y luego elimino los que no son jacaranda?
################################## o df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy() ya realiza la copia solo con los de jacaranda?

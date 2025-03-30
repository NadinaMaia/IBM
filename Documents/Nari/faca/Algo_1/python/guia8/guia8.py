from queue import LifoQueue as Pila
from queue import Queue as Cola
import random as random

#%% Hecho en clase
#Ej 2 
def clonar_sin_comentarios(nombre_archivo:str) -> None:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readline()

    archivo_nuevo = []
    for l in lineas:
        s = l.strip()
        if len(s) == 0 or (not "#" == s[0]):
            archivo_nuevo.append(l)
    archivo.close()

    salida = open("sinComentarios.txt", "w")
    for l in archivo_nuevo:
        salida.write(l)
    salida.close()
    return salida
    
#class_TestCantidadElemento(unittest.TestCase):
#armo las funciones 

#%%Ej 10
pila_test = Pila()
pila_test.put(1)
pila_test.put(5)
pila_test.put(8)
pila_test.put(2)

def buscarElMaximo(p):
    maximo = p.get()
    while not p.empty():
        i = p.get()
        if maximo < i:
            maximo = i
    return maximo

##
#def agrupar_longitud(nombre_archivo:str)-> dict:
#    longitud_en_letras = {}
#    archivo = open("nombre_archivo","r")
#    contenido = archivo.read()
#    

#%% Ej guia 
#%% Ej 1
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

#%% Ej 2
def existe_palabra(nombre_archivo:str, palabra:str)->bool:
    archivo = open(nombre_archivo,"r")
    for linea in archivo.readlines():
        if palabra in linea:
            return True
    return False
 
#%% Ej 3
def cantidad_apariciones(nombre_archivo:str,palabra:str)-> int:
    archivo = open(nombre_archivo, "r")
    contador = 0
    contenido = archivo.read().split()
    for puntero in contenido:
        if puntero == palabra:
            contador += 1
    archivo.close()
    return contador 

#%% Ej 3
def invertir_archivo(nombre_archivo:str)-> None:
    archivo_original = open(nombre_archivo, "r")
    archivo_invertido = open("reverso.txt", "w")
    lineas = archivo_original.readlines()[::-1]
    for linea in lineas:
        archivo_invertido.write(linea)
    return archivo_invertido

#%% Ej 4
def agregar_frase_final(nombre_archivo:str, frase:str) -> None:
    archivo = open(nombre_archivo, "a")
    archivo.write(frase)
    archivo.close

#%% Ej 5
def agregar_frase_principio(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,'r+') 
    contenido = archivo.read()
    archivo.seek(0,0)
    archivo.write(frase.rstrip('\r\n') + '\n' + contenido)
## diferencia entre r y r+
#no entiendo nada de este codigo

#%% Ej 7
def promedioEstudiante(lu:str)-> float:
    archivo = open("notas.csv","r")
    lineas = archivo.readlines()
    notas_alumno = 0
    n_total = 0
    for linea in lineas:
        datos = linea.split()
        if datos[0] == lu:
            notas_alumno += datos[3]
            n_total += 1
    promedio = notas_alumno/n_total
    return promedio

#%% Ej 8
def generar_nros_al_azar(n:int, desde:int, hasta:int) -> Pila:
    res = Pila()
    for i in range(n):
        res.put(random.randint(desde,hasta))
    return res
 
#%% Ej 9
def cantidad_elementos(p:Pila)->int:
    contenido=[]
    contador:int=0
    while not p.empty():
        contenido.append(p.get())
        contador+=1
    for elemento in contenido[::-1]:
        p.put(elemento)
    return contador

#%% Ej 10
def buscar_el_maximo(p:Pila)-> int:
    maximo = p.get()
    while not p.empty():
        comparar = p.get()
        if maximo < comparar:
            maximo = comparar
    return maximo

#%% Ej 11
def esta_bien_balanceada(s:str)->bool:
    res = False
    p = Pila()
    for elemento in s: #porque con paso neg?
        p.put(elemento)
        balance = 0 
    while not p.empty():
        digito = p.get()
        if digito == ")":
            balance += 1
        if digito == "(":
            balance -= 1
    if balance == 0:
        res = True
    return res

#%% Ej 13
def nros_azar_encolados(n:int, desde:int, hasta:int)-> Cola:
    p = generar_nros_al_azar(n,desde,hasta)
    c = Cola()
    while not p.empty():
        c.put(p.get())
    return c

#%% Ej 14
def cantidad_elementos(n)-> int:
    c = Cola()
    for i in range(n):
        c.put(random.randint(1,10))
    contador = 0 
    while not c.empty():
        c.get()
        contador += 1
    return contador

#%% Ej 15
def buscar_el_maximo_cola()-> int:
    c = Cola()
    for i in range(random.randint(4,10)):
        c.put(random.randint(1,10))
    
    lista = []
    print("veamos los elementos de la cola")
    while not c.empty():
        elem = c.get()
        lista.append(elem)
        print(elem)
    for elemento in lista[::-1]:
        c.put(elemento)
    
    maximo = c.get()
    while not c.empty():
        comparar = c.get()
        if maximo < comparar:
            maximo = comparar
    print("El maximo de la cola es " + str(maximo))

#%% Ej 19 
def agrupar_por_longitud(nombre_archivo:str)-> dict:
    archivo = open(nombre_archivo, "r")
    palabras = archivo.read().split()

    diccionario:dict = {}
    for palabra in palabras:
        clave =  len(palabra)
        if clave in diccionario:
            diccionario[clave] += 1
        else:
            diccionario[clave] = 1
    archivo.close()
    return diccionario

#%% Ej 21
def la_palabra_mas_frecuente(nombre_archivo:str)->str:
    archivo = open(nombre_archivo,"r")
    palabras = archivo.read().split()
    dic:dict = {}
    for palabra in palabras:
        if palabra in dic:
            dic[palabra] += 1
        else:
            dic[palabra] = 1

    palabra_freq = ""
    freq_max = 0
    for clave in dic:
        if dic[clave]> freq_max:
            freq_max = dic[clave]
            palabra_freq = clave
    return palabra_freq

#for palabra,frecuencia in frec.items():
#    if frecuencia>frecuencia_max:
#        frecuencia_max=frecuencia
#        palabra_mas_frecuente=palabra

#%% Ej 22
def visitar_sitio(histo:dict, usuario:str, sitio:str)-> None:
    if usuario in histo:
        histo[usuario].put(sitio)
    else:
        histo[usuario] = Pila()
        histo[usuario].put(sitio)

def navegar_atras(histo:dict, usuario:str):
    global ultimo_borrado 
    ultimo_borrado = histo[usuario].get()
    return histo

def navegar_adelante(histo:dict,usuario:str):
    return histo[usuario].put(ultimo_borrado)

historiales={} 
visitar_sitio(historiales,"Usuario1","google.com") 
visitar_sitio(historiales,"Usuario1","facebook.com")
navegar_atras(historiales,"Usuario1")
visitar_sitio(historiales,"Usuario2","youtube.com")
navegar_adelante(historiales,"Usuario1")


cola = Pila()
cola.put(2)
cola.put(3)
cola.put(4)
cola.put(5)

def entender(c):
    lista = []
    print("veamos los elementos de la cola")
    while not c.empty():
        elem = c.get()
        lista.append(elem)
        print(elem)
    for elemento in lista:
        accion = c.put(elemento)
        print("estoy" + str(elemento))
    while not c.empty():
        elem = c.get()
        lista.append(elem)
        print(elem)        
    return None

print(entender(cola))
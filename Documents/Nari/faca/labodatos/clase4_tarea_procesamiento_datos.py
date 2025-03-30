import numpy as np

empleados_01 = np.array([
                        ["DNI","Salario", "Edad", "Cantidad de hijos"],
                        [20222333, 20000, 45, 2],
                        [33456234, 25000, 40, 0],
                        [45432345, 10000, 41, 1],
                        [44236276, 18000, 36, 0]
                        ])
######################## porque b es de 2 dimensiones, segun diapo 38

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # 2 dimensiones
#datos.shape devuelve (fila,columna)
#%%
def superanSalarioActividad01(datos, umbral):
    res = []
    cant_filas = datos.shape[0]
    for i in range(1, cant_filas):
        salario = float(datos[i][3])
        if salario > umbral:
            res.append(datos[i])
    return np.array(res)

#print(superanSalarioActividad01(empleados_01, 15000))

########### chat gpt lo soluciona poniendo salario = float(datos[i][3])  # Convertir el salario a un tipo de dato numérico
########### pero porque dice que datos[i][3] == str(umbral)

## Cuanto costo implementar la funcion?
## yo diria que poco porque su tiempo de produccion fue un ratito
## si agrego mas filas va a seguir funcionando, pero si cambio el orden de las columnas no 
## para evitar esto, voy a realizar una nueva funcion donde identifique la columna salario 

#%%
def superanSalarioActividad03(datos, umbral):
    res = []
    cant_filas = datos.shape[0]
    cant_columnas = datos.shape[1] 
    columna_de_salario = 0
    for j in range(cant_columnas):
        if datos[0][j] == "Salario":
            columna_de_salario = j
    for i in range(1, cant_filas):
        salario = float(datos[i][columna_de_salario])
        if salario > umbral:
            res.append(datos[i])
    return np.array(res)

print(superanSalarioActividad03(empleados_01, 15000))

#%% 
empleados_04 = np.array([
                        ["DNI", 20222333, 33456234, 45432345, 44236276],
                        ["Salario", 20000, 25000, 10000, 18000]
                        ["Edad", 45, 40,41, 36]
                        ["Cantidad de hijos", 2, 0, 1, 0]
                        ])

def superanSalarioActividad04(datos, umbral):
    res = []
    cant_filas = datos.shape[0]
    cant_columnas = datos.shape[1] 
    fila_de_salario = 0
    for i in range(cant_filas):
        if datoa[0][i] == "Salario":
            fila_de_salario = i
    for j in range(cant_columnas):
        if datos[fila_de_salario][j] > umbral:
            lista = []
            for k in range(cant_filas):
                lista.append(datos[k][j])
                
            res.append()

print(superanSalarioActividad04(empleados_04, 15000))

#%% evidentemente, invertir las columnas a filas fue muy costoso ya que complico la funcion



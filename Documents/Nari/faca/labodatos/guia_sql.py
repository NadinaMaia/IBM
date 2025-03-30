"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Nadina Soler
"""
#%%
# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val

def main():

    print()
    print("# =============================================================================")
    print("# Creamos/Importamos los datasets que vamos a utilizar en este programa")
    print("# =============================================================================")

    carpeta = r"C:\Users\soler\Documents\Nari\faca\labodatos\Guía Práctica - SQL - Archivos adjuntos-20240207\\"


    casos      = pd.read_csv(carpeta+"casos.csv")    
    departamento = pd.read_csv(carpeta+"departamento.csv")    
    grupoetario   = pd.read_csv(carpeta+"grupoetario.csv")    
    provincia    = pd.read_csv(carpeta+"provincia.csv")    
    tipoevento= pd.read_csv(carpeta+"tipoevento.csv")    
    
    
   
# -*- coding: utf-8 -*-

   
#%% SECCION A
#a. 
    consultaSQL = """
                   SELECT descripcion
                   FROM departamento
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)    
    

#b.
    consultaSQL = """
                   SELECT DISTINCT descripcion
                   FROM departamento
                   """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   
               
#c.
    consultaSQL = """
                   SELECT DISTINCT id, descripcion
                   FROM departamento
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   


#d.
    consultaSQL = """
                   SELECT * 
                   FROM departamento
                                     """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   

#e.
    consultaSQL = """
                   SELECT DISTINCT id AS codigo_depto, descripcion AS nombre_depto
                   FROM departamento
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   
    

#f.
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM departamento
                   WHERE id_provincia = 54
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   
    

#g.
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM departamento
                   WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   

#h.
    consultaSQL = """
                    SELECT DISTINCT *
                    FROM departamento
                    WHERE id_provincia >= 50 AND id_provincia <= 59
                   """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
     
#%% SECCION B

# a. PREGUNTAR SI TA BIEN, me pedia cant casos o casos por depto?
    consultaSQLa1 = """
                  SELECT casos.id_depto, casos.cantidad, deptos.id_provincia
                  FROM casos 
                  INNER JOIN departamento AS deptos 
                  ON deptos.id = casos.id_depto
                  """
    imprimirEjercicio([departamento], consultaSQLa1, sql^consultaSQLa1)
    
    casos_depto = sql^consultaSQLa1
    
    consultaSQLa2 = """
                  SELECT SUM(cd.cantidad) as cant_casos, p.descripcion
                  FROM casos_depto AS cd
                  INNER JOIN provincia AS p
                  ON cd.id_provincia = p.id
                  WHERE p.descripcion = 'Chaco'
                  GROUP BY p.descripcion
                  """
    imprimirEjercicio([departamento], consultaSQLa2, sql^consultaSQLa2)
    
    casos_chaco = sql^consultaSQLa2
    
#b.
   
#c 
    consultaSQLa1 = """
                  SELECT casos.id_depto, casos.cantidad, deptos.id_provincia
                  FROM casos 
                  INNER JOIN departamento AS deptos 
                  ON deptos.id = casos.id_depto
                  """
    imprimirEjercicio([departamento], consultaSQLa1, sql^consultaSQLa1)
    
    casos_depto = sql^consultaSQLa1
    
    consultaSQLa2 = """
                  SELECT SUM(cd.cantidad) as cant_casos, p.descripcion
                  FROM casos_depto AS cd
                  INNER JOIN provincia AS p
                  ON cd.id_provincia = p.id
                  WHERE p.descripcion = 'Chaco'
                  GROUP BY p.descripcion
                  """
    imprimirEjercicio([departamento], consultaSQLa2, sql^consultaSQLa2)
    
    casos_chaco = sql^consultaSQLa2
  
#d
###uso la tabla antes creada: casos_depto en el punto a de arriba
    consultaSQLb2 = """
                  SELECT SUM(cd.cantidad) as cant_casos, d.descripcion
                  FROM casos_depto AS cd
                  INNER JOIN provincia AS p
                      ON cd.id_provincia = p.id
                  INNER JOIN departamento AS d
                      ON cd.id_depto = d.id
                  WHERE p.descripcion = 'Buenos Aires' AND cd.cantidad > 10
                  GROUP BY cd.id_depto, d.descripcion
                  """
    imprimirEjercicio([departamento], consultaSQLb2, sql^consultaSQLb2)
    
    casos_bsas = sql^consultaSQLb2
    
#%% SECCION C
###### ME DEVUELVE VACIO AMBOS
#a. devolver lista con nombres de deptos que no tienen casos asociados
    consultaSQL = """
                  SELECT depto.descripcion
                  FROM departamento AS depto 
                  LEFT OUTER JOIN casos AS c 
                  ON depto.id = c.id_depto
                  WHERE c.id_depto = NULL
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
    
    casos_depto = sql^consultaSQL
    
#b. devolver lista con tipos de eventos que no tienen ningun caso ningun caso asociado
######### NO SE COMO HACERLO
    consultaSQL = """
                  SELECT te.descripcion, c.id_tipoevento
                  FROM tipoevento AS te 
                  LEFT OUTER JOIN casos AS c 
                  ON te.id = c.id_tipoevento
                  GROUP BY descripcion, c.id_tipoevento
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
    
    casos_depto = sql^consultaSQL
    
#%% SECCION D
#a. calcular cant total de casos que hay en la tabla casos
    consultaSQL = """
                  SELECT SUM(cantidad) AS suma_total
                  FROM casos
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
       
#b.
    consultaSQL = """
                  SELECT id_tipoevento, anio, SUM(cantidad) AS cantidad
                  FROM casos
                  GROUP BY id_tipoevento, anio
                  ORDER BY anio ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)

#c.
    consultaSQL = """
                  SELECT id_tipoevento, anio, SUM(cantidad) AS cantidad
                  FROM casos
                  WHERE anio = 2019
                  GROUP BY id_tipoevento, anio
                  ORDER BY anio ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)

#d. cant deptos por provincia. info ordenada por codigo de provincia
    consultaSQL = """
                  SELECT id_provincia, COUNT (id) AS cant_deptos
                  FROM departamento
                  GROUP BY id_provincia
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)

#e. deptos con menos casos en 2019
    consultaSQL = """
                  SELECT id_depto, SUM(cantidad) AS cantidad_depto
                  FROM casos
                  WHERE cantidad <= ALL
                  GROUP BY id_depto
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
    
    casos_depto = sql^consultaSQL
########## diapo 75, having? que es una funcion de grupo    
    consultaSQL = """
                  SELECT MIN(cantidad) AS cantidad
                  FROM casos_depto
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
    
#g. promedio cant.casos por año y provincia
###### analizar tabla salida
###### no entiendo la consigna
    consultaSQL = """
                  SELECT p.descripcion, c.anio, AVG(c.cantidad) AS cantidad_depto
                  FROM casos AS c
                  INNER JOIN departamento AS d 
                  ON d.id = c.id_depto
                  INNER JOIN provincia AS p 
                  ON p.id = d.id_provincia
                  GROUP BY p.descripcion, c.anio
                  ORDER BY p.descripcion ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)

#h. listar para cada provincia y anio, deptos que mas cant casos tuvieron
    consultaSQL = """
                  SELECT p.descripcion, c.anio, SUM(c.cantidad) AS cantidad_depto
                  FROM casos AS c
                  INNER JOIN departamento AS d 
                  ON d.id = c.id_depto
                  INNER JOIN provincia AS p 
                  ON p.id = d.id_provincia
                  GROUP BY p.descripcion, c.anio
                  ORDER BY p.descripcion ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)              
#i. mostrat cant de casos total, max, min, promedio que tuvo la provincia de buenos aires en 2019
#### max y min por depto?
    consultaSQL = """
                  SELECT p.descripcion, c.anio, SUM(c.cantidad) AS cantidad_depto
                  FROM casos AS c
                  INNER JOIN departamento AS d 
                      ON d.id = c.id_depto
                  INNER JOIN provincia AS p 
                  ON p.id = d.id_provincia
                  GROUP BY p.descripcion, c.anio
                  ORDER BY p.descripcion ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)              
#j. misma consulta pero solo para casos con cant total mayor a mil casos
       
#%% SECCION E
#a. depto con mayor cant de casos sin usar max, order by o limit
##### no me anda
    consultaSQL = """
                  SELECT c1.id_depto, SUM(c1.cantidad) AS cantidad1
                  FROM casos AS c1
                  HAVING cantidad1 >= ALL(
                      SELECT SUM(c2.cantidad) AS cantidad2
                      FROM casos AS c2
                      WHERE c1.id_depto = c2.id_depto
                      GROUP BY c2.id_depto
                      )
                  GROUP BY c1.id_depto
                  ORDER BY c1.id_depto ASC
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   

#%% SECCION F
#a. devolver tipo de eventos con casos asociados
    consultaSQL = """
                  SELECT te.id, te.descripcion
                  FROM tipoevento AS te
                  WHERE te.id IN (
                      SELECT c.id_tipoevento
                      FROM casos AS c
                      )
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)  
    
#a. devolver tipo de eventos sin casos asociados
    consultaSQL = """
                  SELECT te.id, te.descripcion
                  FROM tipoevento AS te
                  WHERE te.id NOT IN (
                      SELECT c.id_tipoevento
                      FROM casos AS c
                      )
                  """
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)
    
#%% SECCION G
#a.  
######### no entiendo porque no anda
    consultaSQL = """
                  SELECT te.id, te.descripcion
                  FROM tipoevento AS te
                  WHERE te.id EXISTS (
                      SELECT c.id_tipoevento
                      FROM casos AS c
                      WHERE te.id = c.id_tipoevento # es necesario? lo agregue porque lo vi en la diapo, no se que hace
                      )
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)   
#b.          

#%% SECCION H
#a. Listar las provincias que tienen una cantidad total de casos mayor al promedio 
#de casos delpaís.Hacer el listado agrupado por año.
    consultaSQL = """
                  SELECT p.descripcion, SUM(c.cantidad) AS cantidad
                  FROM casos AS c
                  INNER JOIN departamento AS d
                      ON d.id = c.id_depto
                  INNER JOIN provincia AS p
                      ON d.id_provincia = p.id
                  WHERE cantidad < (
                      SELECT AVG(cantidad)
                      FROM casos AS c
                      )
                  GROUP BY p.descripcion
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL)      
### el promedio da 5, esta bien?  
## si pongo menor da muchas provincias con cantidad mayor a 5

#%% SECCION I
#a.
    consultaSQL = """
                  SELECT id, descripcion
                  FROM departamento
                  ORDER BY descripcion DESC, id ASC
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 
    
#b.   
    consultaSQL = """
                  SELECT descripcion
                  FROM provincia
                  WHERE descripcion LIKE 'M%'
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#c.
    consultaSQL = """
                  SELECT descripcion
                  FROM provincia
                  WHERE descripcion LIKE 'S___a%'
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 
#d.
    consultaSQL = """
                  SELECT descripcion
                  FROM provincia
                  WHERE descripcion LIKE '%a'
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#e.
    consultaSQL = """
                  SELECT descripcion
                  FROM provincia
                  WHERE descripcion LIKE '_____'
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#f.
    consultaSQL = """
                  SELECT descripcion
                  FROM provincia
                  WHERE descripcion LIKE '%do%'
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#g.
    consultaSQL = """
                  SELECT id, descripcion
                  FROM provincia
                  WHERE descripcion LIKE '%do%' AND id < 30
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#h.

#### tengo forma de que busque San y san?
    consultaSQL = """
                  SELECT id AS codigo_depto, descripcion AS nombre_depto
                  FROM departamento
                  WHERE descripcion LIKE '%San%'
                  ORDER BY descripcion DESC
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#i. 
###### me pide nombre de depto pero dice 'casos de las provincias
###### chequear si resultado esta bien
###### tucuman nombre_depto capital?
    consultaSQL = """      
                  SELECT p.descripcion AS nombre_prov,
                         d.descripcion AS nombre_depto,
                         c.anio AS anio,
                         c.semana_epidemiologica AS semana_epi,
                         ge.descripcion AS grupo_etario,
                         SUM(c.cantidad) AS cant_casos
                  FROM provincia AS p
                  INNER JOIN departamento AS d
                      ON p.id = d.id_provincia
                  INNER JOIN casos AS c
                      ON c.id_depto = d.id 
                  INNER JOIN grupoetario AS ge
                      ON ge.id = c.id_grupoetario     
                  GROUP BY d.descripcion,
                           p.descripcion,
                           c.anio,
                           c.semana_epidemiologica,
                           ge.descripcion
                  ORDER BY cant_casos DESC,
                           nombre_prov ASC,
                           nombre_depto ASC,
                           anio ASC, 
                           grupo_etario ASC 
                  LIMIT 15
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

#j. idem item anterior pero tuplas con maximo en cantidad

#%% SECCION J
#a. 
####### me devuelde todos los ajustes en columnas, 
#####pero quiero la resultante nomas
    consultaSQL = """
                  SELECT id, 
                         REPLACE(descripcion, 'á', 'a') AS descripcion,
                         REPLACE(descripcion, 'é', 'e') AS descripcion,
                         REPLACE(descripcion, 'í', 'i') AS descripcion,
                         REPLACE(descripcion, 'ó', 'o') AS descripcion,
                         REPLACE(descripcion, 'ú', 'u') AS descripcion                  
                  FROM departamento
                  ORDER BY descripcion ASC
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 
#b.
    consultaSQL = """
                  SELECT id, 
                         REPLACE(descripcion, 'á', 'a') AS descripcion,
                         REPLACE(descripcion, 'é', 'e') AS descripcion,
                         REPLACE(descripcion, 'í', 'i') AS descripcion,
                         REPLACE(descripcion, 'ó', 'o') AS descripcion,
                         REPLACE(descripcion, 'ú', 'u') AS descripcion,
                         UPPER(descripcion) AS descripcion
                  FROM departamento
                  ORDER BY descripcion ASC
                  """   
    imprimirEjercicio([departamento], consultaSQL, sql^consultaSQL) 

       
                                             
#%% FUNCIONES
# =============================================================================
# FUNCIONES PARA LA GENERACIÓN DE DATAFRAMES 
# =============================================================================

def imprimirEjercicio(listaDeDataframesDeEntrada, consultaSQL, dataframeResultadoDeConsultaSQL):
    print("# -----------------------------------------------------------------------------")
    print() 
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(dataframeResultadoDeConsultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()
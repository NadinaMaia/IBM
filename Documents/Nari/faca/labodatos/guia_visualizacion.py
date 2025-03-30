# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:45:13 2024

@author: soler
"""
import seaborn 
from inline_sql import sql, sql_val

data_ping = seaborn.load_dataset('penguins')

#%% Ej 2
#% a. que representa cada linea del dataframe?

    ## hago una consulta para ver que hay en la tabla
    consulta = sql^"""
                SELECT *
                FROM data_ping
                LIMIT 5
    """
    print(consulta)
    
    ## cada linea representa los datos de un pinguino
    ## su especie, de que isla es, datos del pico y alas, masa y sexo
    
#% b. cuantas muestras hay en total?

    consulta = sql^"""
                SELECT COUNT(*) AS 'cant_registros'
                FROM data_ping
    """
    print(consulta)
    

#% c. cuales son las especies de pinguinos consideradas

    consulta = sql^"""
                SELECT DISTINCT species AS 'especies'
                FROM data_ping
    """
    print(consulta)
        

#% d. cuales son las islas estudiadas?

    consulta = sql^"""
                SELECT DISTINCT island AS 'islas_estudiadas'
                FROM data_ping
    """
    print(consulta)
        
#% e. para cada pinguino, con que datos contamos?

   #% especie, isla, datos de pico, alas, masa y sexo
      
    
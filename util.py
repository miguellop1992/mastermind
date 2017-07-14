""" Autor: Miguel Lopez
    C.I. : 20381676
"""
import os
import re
from enum import Enum

# Mostrar otra vez el menu
clear = lambda: os.system('cls')

#Mascara para los numericos
enter = re.compile("[0-9]") 

""" Funcion para parsear a integer
"""
def to_int(value):
    try:
        return int(value)
    except ValueError :
        return None

""" Funcion para parsear a array si estan 
    las condiciones o a integer
"""
def to_array(value):
    try:
        # Si la longitud es mayor a 1
        # Lo convertimos en array
        if value.__len__()>1:
            arr = value.split(',')
            #Revisamos que sea entero
            for val in arr:
                if(enter.match(val) is None):
                    return None
            #Si es entero y la longitud es 4 cumple 
            #Con las caracteristicas definidas y lo 
            #Retornamos        
            return arr if arr.__len__() == 4 else None 
        return to_int(value)
    except ValueError :
        return None

""" Autor: Miguel Lopez
    C.I. : 20381676
"""
import random

class CodeBreaker:
    def __init__(self):
        #Lista de valores por turno
        self.__turn=[]
    """ Funcion para ver si se puede agregar o 
        no los valores del turno
    """
    def addTurn(self,values):
        try:
            if(self.__turn.index(values)>-1):
                return False
        except ValueError:
            self.__turn.append(values)
            return True

class CodeMaker:
    WIN='nnnn'

  
    """ Funcion para comenzar el juego
    """
    def begin(self):
        self.__secret = [
             str(random.randrange(0, 9)),
             str(random.randrange(0, 9)),
             str(random.randrange(0, 9)),
             str(random.randrange(0, 9))
        ]

    """ Funcion para evaluar los valores 
        ingresados por el jugador
    """
    def eval(self, values):
        res = ""
        indexs=[]
        #Se comprueba si coincide posicion y numero
        for i in range(0, values.__len__()):
            if values[i] == self.__secret[i]:
                res += 'n'
            else:
                indexs.append(i)
        
        #Se comprueba si coincide  numero
        if indexs.__len__() > 0 :
            for i in indexs:
                try:
                    if self.__secret.index(values[i]) > -1 :
                        res += 'b'
                except ValueError:
                    pass
        return res

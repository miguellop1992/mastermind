""" Autor: Miguel Lopez
    C.I. : 20381676
"""

from model import CodeMaker, CodeBreaker
from util import clear, to_array


class Table:
    
    ROW = 10
    tabrow = []
    index = 10
    
    def __init__(self):
        self.codemaker = CodeMaker()
        self.codebreaker = CodeBreaker()


    """ Funcion para imprimir el tablero
    """
    def __print(self):

        len = self.tabrow.__len__()
        lenfor = len - 1
        # size= Table.ROW if len <= Table.ROW else len

        print("")
        print("")

        for i in range(Table.ROW - 1, -1, -1):
            print("   +--------+-----+-----+-----+-----+")
            if lenfor >= i and self.tabrow[i] != None:
                print("%02d " % (i + 1) + self.tabrow[i])
            else:
                print("%02d +        +     +     +     +     +" % (i + 1))
        print("   +--------+-----+-----+-----+-----+")
    
    """ Funcion para comenzar el juego
    """
    def begin(self):
        self.codemaker.begin()
        self.tabrow = []
        self.__renter()
    
    """ Funcion para imprimir si el jugador perdio o gano
    """
    def __winner(self,win=True):
        if win: 
            self.__print()
            print()
            print("+------------------------------------------+")
            print("+ Felicitaciones has GANADO!!!!            +")
            print("+------------------------------------------+")
        else :
            print()
            print("+------------------------------------------+")
            print("+ Has PERDIDO!!!! :( :( :( :(              +")
            print("+------------------------------------------+")
        print()
        print("  Presione:")
        print("   1.- Para un nuevo juego")
        print("   0.- Para salir")
        inp = to_array(input("Ingrese su opcion: "))

        if(inp == 0):#Salir de juego
            exit()
        elif(inp == 1):#Reiniciar el juego
            self.begin()
        else:#Mostrar otra vez el menu
            self.__winner(win)
        

    """ Funcion para evaluar los datos ingresados
        por el jugador y revisar si gano, perdio o 
        continua jugando
    """    
    def __update(self, values):
        res = self.codemaker.eval(values)
        
        self.tabrow.append(
            "+  {:<4s}  +{:^5s}+{:^5s}+{:^5s}+{:^5s}+".format(res, *values))
        
        if(res==self.codemaker.WIN):
            self.__winner()
        elif self.tabrow.__len__()==self.ROW:
            self.__winner(False)
        else:    
            self.__renter()

    """ Funcion para imprimir las instrucciones del juego
    """
    def __instruc(self):
        print()
        print("+------------------------------------------+")
        print("+ Instrucciones:                           +")
        print("+  n: Significa que en la fila un numero y +")
        print("+     posicion coinciden                   +")
        print("+  b: Significa que en la fila un numero   +")
        print("+     coincide                             +")
        print("+------------------------------------------+")
        self.__renter(False)
    
    """ Funcion para imprimir el menu el juego y
        pedir los valores del juego
    """
    def __renter(self,showTable=True):

        if showTable : 
            # clear()
            self.__print()
         
        print()
        print("+------------------------------------------+")
        print("+ Ingrese los numeros separados por coma,  +")
        print("+ como en este ejemplo: 1,8,7,6            +")
        print("+------------------------------------------+")
        print()
        print("  Presione:")
        print("   1.- Para un nuevo juego")
        print("   2.- Para ver instrucciones")
        print("   3.- Ver tablero")
        print("   0.- Para salir")
        inp = to_array(input("Ingrese su opcion: "))

        if(inp == 0):#Salir del juego
            exit()
        elif(inp == 1):#Reiniciamos el juego
            self.begin()
        elif(inp == 2):#Mostramos las instrucciones
            self.__instruc()
        elif(inp == 3):#Mostramos el tablero con el menu
            self.__renter()
        elif type(inp) is list: #Ingrasamos los valores 

            #Validamos que no se guarde en el tablero
            #Varias veces los mismos valores
            if self.codebreaker.addTurn(inp):
                self.__update(inp)
            else:
                print()
                print("+------------------------------------------+")
                print("+ Ya se han ingreso esto valores:          +")
                print("+    {0},{1},{2},{3}                               +".format(*inp))
                print("+------------------------------------------+")
                self.__renter(False)
        else:#Mostrar otra vez el menu
            self.__renter()

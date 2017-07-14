""" Autor: Miguel Lopez
    C.I. : 20381676
"""
from table import Table
from util import  clear,to_int

class Menu:

    def __init__(self):
        #Instanciamos el tablero
        self.table=Table()
    
    """ Funcion para imprimir en consola las instrucciones 
        del juego
    """
    def __instruc(self):
        print()
        print("         ███▓▒░░.Mastermind.░░▒▓███         ")
        print("+------------------------------------------+")
        print("+ Para jugar, debe saber que en este juego +")
        print("+ se eligen 4 numeros al azar del 0 al 9,  +")
        print("+ para que usted revelar cuales son los    +")
        print("+ numeros y el orden.                      +")
        print("+------------------------------------------+")
        print()

    """ Funcion de arranque del juego
    """
    def main(self):
        #Limpiamos consola, imprimimos las instrucciones 
        #y pedimos una opcion
        clear()
        self.__instruc()
        print("  Presione:")
        print("   1.- Para comenzar")
        print("   0.- Para salir")

        option=to_int(input(" Ingrese su opcion: "))
        
        if option==1: #Iniciar el juego
            clear()
            self.table.begin()
        elif option == 0: #Salir del juego
            exit() 
        else: # Volver a mostrar el menu
            self.main()
                    





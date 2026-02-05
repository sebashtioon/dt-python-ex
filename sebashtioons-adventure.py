import time
import os

_in_main_menu : bool = False

difficulties : list = ["ez", "mid", "expert+"]


# utility

def _cls(): # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def _ok() -> bool: # display ok option
    print("type anything to continue...")
    ok = input("")

def gameQuit():
    _cls()

def gameStart():
    pass


def mainMenu():
    _cls()
    _in_main_menu = True
    print("--------------------")
    print("ebashtioons adventure")
    print("--------------------")

    print("please select an option:")

    print("\n1. play")
    print("2. settings")
    print("3. how to play")
    print("4. quit")


    option = input("")

    _cls()
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        _cls()
        print("thing")

    elif option == 4:
        gameQuit()


def main():
    mainMenu()



main()
import time
import os

_in_main_menu : bool = False

difficulties : list = ["ez", "mid", "expert+"]


# utility
def _cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def mainMenu():
    _in_main_menu = True
    print("--------------------")
    print("ebashtioons adventure")
    print("--------------------")

    print("please select an option:")

    print("\n1. play")
    print("2. settings")
    print("3. quit")

    option = input("")

    _cls()


def main():
    mainMenu()


def gameStart():
    pass


main()
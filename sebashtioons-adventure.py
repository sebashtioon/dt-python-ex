import time

_in_main_menu : bool = False


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

def main():
    mainMenu()


main()
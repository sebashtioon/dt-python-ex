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
    return True

def type_text(text: str, delay: float = 0.04, end: str = "\n") -> None:
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    if end:
        print(end, end="", flush=True)


# core (the actual fucking game and functionality)

def gameQuit():
    _cls()

def gameTutorial():
    _cls()
    print("--------------------")
    print("to be done")
    print("--------------------")
    if _ok():
        mainMenu()

def gameSettings():
    _cls()
    print("--------------------")
    print("to be done")
    print("--------------------")
    if _ok():
        mainMenu()



# ok actual game

def gameStart():
    _cls()
    firstDialogue()

def firstDialogue() -> bool:
    type_text("i arrived at school on a chilly, windy morning", 0.07)
    time.sleep(1.0)















def mainMenu(invalid_option : bool = False):
    _cls()
    _in_main_menu = True

    if invalid_option:
        print("\033[31mplease select a valid option\033[0m")
    
    print("--------------------")
    print("sebashtioons adventure")
    print("--------------------")

    print("please select an option:")

    print("\n1. play")
    print("2. settings")
    print("3. how to play")
    print("4. quit")
    
    option = input("")
    
    if option == "1":
        gameStart()
    elif option == "2":
        gameSettings()
    elif option == "3":
        gameTutorial()
    
    elif option == "4":
        gameQuit()
    
    else:

        mainMenu(True)

# c++ core
def main():
    mainMenu()

# go
main()
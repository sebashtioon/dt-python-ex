import time
import os
import random

_in_main_menu : bool = False

difficulties : list = ["ez", "mid", "expert+"]

# so we can make ppl easily
class character:
    def __init__(self, name="", age="", pr_obj="", pr_acc="", pr_poss=""):
        self.name = name
        self.age = age
        self.pr_obj = pr_obj
        self.pr_acc = pr_acc
        self.pr_poss = pr_poss


# pre randomized story values
__main_friends = {

}


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

def fake_loader(label: str = "loading", length: int = 20, min_delay: float = 0.03, max_delay: float = 0.12) -> None:
    print(f"{label}...", flush=True)
    progress = 0
    while progress <= length:
        # simulate buffer stalls with occasional longer pauses
        stall = random.random() < 0.12
        delay = random.uniform(max_delay, max_delay * 2.5) if stall else random.uniform(min_delay, max_delay)
        bar = "#" * progress + "-" * (length - progress)
        print(f"[{bar}]", end="\r", flush=True)
        time.sleep(delay)
        progress += random.choice([0, 1, 1, 2])
    print(f"[{'#' * length}]", flush=True)
    _cls()


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
    fake_loader()
    firstDialogue()

def firstDialogue() -> bool:
    type_text("i arrived at school on a chilly, windy morning", 0.07)
    time.sleep(0.9)

    type_text("i hadnt slept too well last night, ", 0.1, "")
    time.sleep(0.6)
    type_text("too much math homework", 0.07)














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
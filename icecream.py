import time
iceCreams = []

def addIceCream(icecream):
    iceCreams.append(icecream)

def printIceCreams():
    for i, ic in enumerate(iceCreams, 1):
        print(f"{i}. {ic}")


def main():

    print("-- welcome to the ice creamery --")
    print("------------------")

    # user adds their own ice creams
    first_ice_cream = input("Enter an icecream flavour: ")
    second_ice_cream = input("Enter another icecream flavour: ")
    third_ice_cream = input("Enter yet another icecream flavour: ")
    addIceCream(first_ice_cream)
    addIceCream(second_ice_cream)
    addIceCream(third_ice_cream)

    # add my own
    addIceCream("pistachio")
    addIceCream("rocky road")
    addIceCream("caramel")

    print("------------------")
    print("woah, those are some awesome flavours.\ni added 3 more for some more variation:")

    print("------------------")
    printIceCreams()
    print("------------------")

    times_tried : int = 0
    number_picked : int = 0
    
    # keep asking until the input is between 1 and 6
    while number_picked < 1 or number_picked > 6:
        if times_tried > 0:
            number_picked = int(input("bro its not hard... enter a number between 1 and 6: "))
        else:
           number_picked = int(input("go ahead, enter a number between 1 and 6: "))
        
        times_tried += 1

    print("------------------")

    if times_tried >= 4:
        print("jeez, was it that hard ??")
        print("------------------")
    
    print(f"you picked... {str(number_picked)}")
    time.sleep(1.5)
    print(f"that was {iceCreams[number_picked - 1]}")
    time.sleep(0.8)
    print("but")
    time.sleep(1.5)
    print(f"it is no longer {iceCreams[number_picked - 1]} !!!")
    time.sleep(2.5)

    iceCreams[number_picked - 1] = "FERRARI !!!"
    print("FERRARI !!!!!!!!!!!!!")

    time.sleep(1.5)
    print("anyways here's your new ice cream selection lol")

    time.sleep(1.5)
    print("------------------")

    printIceCreams()


    





main()
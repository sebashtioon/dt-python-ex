iceCreams = []

def addIceCream(icecream):
    iceCreams.append(icecream)


def main():
    first_ice_cream = input("Enter an icecream flavour: ")
    second_ice_cream = input("Enter another icecream flavour: ")
    third_ice_cream = input("Enter yet another icecream flavour: ")
    
    addIceCream(first_ice_cream)
    addIceCream(second_ice_cream)
    addIceCream(third_ice_cream)



main()
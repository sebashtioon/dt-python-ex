iceCreams = []

def addIceCream(icecream):
    iceCreams.append(icecream)


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

    # iterate through all ice creames and print them individually
    for ic in iceCreams:
        print(ic)

    print("------------------")

main()
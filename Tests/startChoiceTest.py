def startChoice():
    choice = " "
    while not choice in "PSBR":
        print("You can:")
        print("P = Examine boulder pile")
        print("S = Go to the structure")
        print("B = Walk towards the beeping")
        print("R = Run!")
        choice = input("What do you want to do? [P/S/B/R]")
    return choice
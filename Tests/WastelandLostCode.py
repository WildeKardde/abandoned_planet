import random

# Location: Wasteland
def doWasteland():
    # Display text
    print(Strings.get("Wasteland"))
    # What can the player do?
    choices = [
        ["B", "Return back the direction think you came from"],
        ["C", "Continue moving forward"],
        ["L", "Explore to the left"],
        ["R", "Try moving to the right"]
    ]
    # Prompt for user action
        choice = Utils.getUserChoice(choices)
    # Perform action
    # use random to select one of 10 locations.
    # One location will be doWastelandC() allowing return to the Dunes.
    # Eight locations will be doWasteland()
    # One location will be doWastelandD() leading to end of game
    # If Inventory introduced, canteen or survival supplies will prevent doWastelandD()
    # If Inventory introduced, compass will default result to doWastelandC()
    choice = random.choice("OWWWWWWWWD")
    if choice == 'O':
        doWastelandC()
    elif choice == 'W':
        print("You move further into the rocky wastes.....does that stone look familiar to you?")
        doWasteland()
    elif choice == 'D':
        doWastelandD()

# Location: Wasteland Outcropping
def doWastelandC():
    # Display text
    print(Strings.get("WastelandC"))
    # What can the player do?
    choices = [
        ["C", "Continue into the rocky wastelands"],
        ["B", "Return to the Sand Dunes"],
        ["R", "Run!"]
    ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    # Perform action
    if choice == 'C':
        doWasteland()
    if choice == 'B':
        doDunes()
    elif choice == 'R':
        doRun()
        
# Location: Wasteland Death
def doWastelandD():
    # Display text
    print(Strings.get("WastelandD"))
    gameover()
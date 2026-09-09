################################################
# Space Adventure
# by Ben & Shmuel
#############################################

# Imports
import Strings, Utils, random, Player
import Inventory as inv
from colorama import init, Fore

# Create player object
p = Player.Player()

# Initialize colorama
init()

# Welcome to the player
def doWelcome():
    # Display text
    print(Fore.GREEN+Strings.get("Welcome", Name))

# Location: Start
def doStart():
    # Display text
    # Display text
    print(Fore.GREEN+Strings.get("Start", Name))
    # What can the player do?
    choices = [
        ["P", "Examine pile of boulders"],
        ["S", "Go to the structure"],
        ["B", "Walk towards the beeping"],
        ["D", "Head to the dunes"],
        ["R", "Run!"],
        ["I", "Inventory"],
        ["M", "My Status"]
    ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
        # Perform action
    if choice == 'P':
        doBoulders()
    elif choice == 'D':
        doDunes()
    elif choice == 'S':
        doStructure()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()
    elif choice == "I":
        inv.display()
        doStart()
    elif choice == "M":
        p.display()
        doStart()

# Location: Boulders
def doBoulders():
    # Track this visit
    p.visitBoulder()
    # Display text
    if p.getBoulderVisits() == 1:
        print(Fore.GREEN+Strings.get("Boulders", Name))
    elif p.getBoulderVisits() == 3:
        print(Fore.CYAN+Strings.get("BouldersKey", Name))
        inv.takeStructureKey()
    else:
        print(Fore.GREEN+Strings.get("Boulders2", Name))
    # Does the player have the key?
    #  if not inv.hasStructureKey():
        # No, display text
    #      print(Strings.get("BouldersKey"))
        # Add key to inventory
    #      inv.takeStructureKey()
    #  else:
        # Yes, so display regular boulder message
    #     print(Strings.get("Boulders"))
    # Go back to start
    doStart()

# Location: Dunes
def doDunes():
    # Display text
    print(Fore.GREEN+Strings.get("Dunes", Name))
    # What can the player do?
    choices = [
        ["W", "Continue into the wastes"],
        ["C", "Go towards the wreckage"],
        ["B", "Go back near the structure"],
        ["R", "Run!"],
        ["I", "Inventory"],
        ["M", "My Status"]
    ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    # Perform action
    if choice == 'W':
        doWasteland()
    elif choice == "C":
        doCrashsite()
    elif choice == 'B':
        doStart()
    elif choice == 'R':
        doRun()
    elif choice == 'I':
        inv.display()
        doDunes()
    elif choice == "M":
        p.display()
        doDunes()

# Location: Wasteland
def doWasteland():
    # Display text
    print(Fore.GREEN+Strings.get("Wasteland", Name))
    # What can the player do?
    choices = [
        ["B", "Return back the direction think you came from"],
        ["C", "Continue moving forward"],
        ["L", "Explore to the left"],
        ["R", "Try moving to the right"],
        ["I", "Inventory"],
        ["M", "My Status"]
    ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    WastelandChoices=["O","W", "W", "W", "W", "W", "W", "W", "W","D"]
    # Perform action
    # use random to select one of 10 locations.
    # One location will be doWastelandC() allowing return to the Dunes.
    # Eight locations will be doWasteland()
    # One location will be doWastelandD() leading to end of game
    # If Inventory introduced, canteen or survival supplies will prevent doWastelandD()
    if inv.hasSurvivalRations():
        WastelandChoices.remove("D")
    # If Inventory introduced, compass will default result to doWastelandC()
    if inv.hasCompass():
        WastelandChoices=["O"]

    choice = random.choice(WastelandChoices)
    if choice == 'O':
        doWastelandC()
    elif choice == 'W':
        print(Fore.GREEN+"You move further into the rocky wastes.....does that stone look familiar to you?")
        doWasteland()
    elif choice == 'D':
        doWastelandD()
    elif choice == 'I':
        inv.display()
        doWasteland()
    elif choice == "M":
        p.display()
        doWasteland()

# Location: Wasteland Outcropping
def doWastelandC():
    # Display text
    print(Fore.GREEN+Strings.get("WastelandC", Name))
    # What can the player do?
    choices = [
        ["C", "Continue into the rocky wastelands"],
        ["B", "Return to the Sand Dunes"],
        ["R", "Run!"],
        ["I", "Inventory"],
        ["M", "My Status"]
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
    elif choice == 'I':
        inv.display()
        doWastelandC()
    elif choice == 'M':
        p.display()
        doWastelandC()

# Location: Wasteland Death
def doWastelandD():
    # Display text
    print(Fore.RED+Strings.get("WastelandD", Name))
    gameOver()

# Location: Crashsite
def doCrashsite():
    # Display text
    print(Fore.GREEN+Strings.get("Crashsite", Name))
    print(Fore.CYAN+Strings.get("CrashRations", Name))
    inv.takeSurvivalRations()
    # What can the player do?
    choices = [
        ["D", "Return to the Sand Dunes"],
        ["S", "Search the wreckage"],
        ["R", "Run!"],
        ["I", "Inventory"],
        ["M", "My Status"]
        ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    # Perform action
    if choice == 'D':
        doDunes()
    elif choice == 'S':
        doCrashSearch()
    elif choice == 'R':
        doRun()
    elif choice == 'I':
        inv.display()
        doCrashsite()
    elif choice == 'M':
        p.display()
        doCrashsite()

# Action: Search Crashsite
def doCrashSearch():
    # Display text
    print(Fore.CYAN+Strings.get("CrashCompass", Name))
    inv.takeCompass()
    doCrashsite()

# Location: Structure
def doStructure():
    # Display text
    print(Fore.GREEN+Strings.get("Structure", Name))
    # What can the player do?
    choices = [
        ["S", "Back to start"],
        ["D", "Open the door"],
        ["B", "Walk towards the beeping"],
        ["R", "Run!"],
        ["I", "Inventory"],
        ["M", "My Status"]
    ]
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    # Perform action
    if choice == 'S':
        doStart()
    elif choice == 'D':
        doStructureDoor()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()
    elif choice == 'I':
        inv.display()
        doStructure()
    elif choice == 'M':
        p.display()
        doStructure()

# Location: Structure door
def doStructureDoor():
    # Display text
    print(Fore.GREEN+Strings.get("StructureDoor", Name))
    if inv.hasStructureKey():
        print(Fore.GREEN+Strings.get("StructureDoorKey", Name))
    else:
        print(Fore.RED+Strings.get("StructureDoorNoKey", Name))
    # What can the player do?
    choices = [
        ["S", "Back to structure"],
        ["R", "Run!"]
    ]
    # Does user have the key?
    if inv.hasStructureKey():
        # Yep, add unlock to choices
        choices.insert(0, ["U","Unlock the door"])
    # Prompt for user action
    choice = Utils.getUserChoice(choices)
    # Perform action
    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()
    elif choice == 'U':
        doEnterStructure()

# Location: Explore beeping
def doBeeping():
    pass

# Player ran
def doRun():
    # Display text
    print(Fore.GREEN+Strings.get("Run", Name))
    p.died()
# Checks player Lives, returns to start if lives left, game over if not
    doStart() if p.isAlive() else gameOver()

# Game over
def gameOver():
    print(Fore.RED+Strings.get("GameOver", Name))
    print(Fore.WHITE+"")

# Location: Behind the Structure Door
def doEnterStructure():
    pass

# Actual game starts here

# Game Prep
p.setName()
Name = p.getName()

# Display welcome message
doWelcome()
# Game start location
doStart()


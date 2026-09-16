########
# Inventory.py
# Inventory system
########

# Imports
from colorama import Fore

inv = {
    "Compass": False,
    "Kinetic Shield": False,
    "Laser Blaster": False,
    "Prybar": False,
    "Rebreather": False,
    "StructureKey": False,
    "Survival Gear Kit": False,
    "Coins": 0,
    "Auto-Restore": 0,
    "Electro-Stun Grenades": 0,
    "Health Hypospray": 0,
    "Survival Rations": 0
}

# Add key to inventory
def takeStructureKey():
    inv["StructureKey"] = True

# Remove key from inventory
def dropStructureKey():
    inv["StructureKey"] = False

# Does the player have the key?
def hasStructureKey():
    return inv["StructureKey"]

# Add coins to inventory
def takeCoins(coins):
    inv["Coins"] += coins

# Remove coins from inventory
def dropCoins(coins):
    inv["Coins"] -= coins

# How many coins does the player have?
def numCoins():
    return inv["Coins"]

# Add compass to inventory
def takeCompass():
    inv["Compass"] = True

# Does the player have the compass?
def hasCompass():
    return inv["Compass"]

# Add survival rations to inventory
def takeSurvivalRations():
    inv["Survival Rations"] += 1

# Does the player have the survival rations?
def hasSurvivalRations():
    return inv["Survival Rations"]

# Use Survival Ration
def dropSurvivalRations():
    inv["Survival Rations"] -= 1

# Get Survival Kit
def takeSurvivalKit():
    inv["Survival Gear Kit"] = True

def hasSurvivalKit():
    return inv["Survival Gear Kit"]

def dropSurvivalKit():
    inv["Survival Gear Kit"] = False

# Prybar Functions
def takePrybar():
    inv["Prybar"] = True

def hasPrybar():
    return inv["Prybar"]

# Rebreather Functions
def takeRebreather():
    inv["Rebreather"] = True

def hasRebreather():
    return inv["Rebreather"]

# Kinetic Shield Functions
def takeShield():
    inv["Kinetic Shield"] = True

def hasShield():
    return inv["Kinetic Shield"]

# Laser Blaster functions
def takeBlaster():
    inv["Laser Blaster"] = True

def hasBlaster():
    return inv["Laser Blaster"]

# Auto Restore functions
def takeRestore():
    inv["Auto-Restore"] += 1

def hasRestore():
    return inv["Auto-Restore"]

def dropRestore():
    inv["Auto-Restore"] -= 1

# Electro-Stun Grenade functions
def takeGrenade(grens):
    inv["Electro-Stun Grenades"] += grens

def hasGrenade():
    return inv["Electro-Stun Grenades"]

def dropGrenade():
    inv["Electro-Stun Grenades"] -= 1

# Health Hypospray functions
def takeHypospray():
    inv["Health Hypospray"] += 1

def hasHypospray():
    return inv["Health Hypospray"]

def dropHypospray():
    inv["Health Hypospray"] -= 1

# Display inventory
def display():
    print(Fore.CYAN+"*** Inventory ***")
    if hasCompass():
        print(Fore.CYAN+"You have a magnetic compass,\n"
              "the arm sways slightly as you move.")
    if hasShield():
        print(Fore.CYAN+"You have a personal kinetic\n"
              "Shield generator, helping to keep you safe.")
    if hasBlaster():
        print(Fore.CYAN+"You have a Laser Blaster.  The\n"
                        "Charge Indicator shows it is ready.")
    if hasPrybar():
        print(Fore.CYAN+"You have a half-meter long\n"
              "Titanium prybar.")
    if hasRebreather():
        print(Fore.CYAN+"You have a Rebreather, in case\n"
              "you find yourself submerged in water.")
    if hasSurvivalKit():
        print(Fore.CYAN+"You have a Survival Kit from the\n"
                "Crash Site.  The lid is secure on it,\n"
                "securing it's contents from you.")
    if hasStructureKey():
        print(Fore.CYAN+"You have a key that flashes blue")
    print(Fore.CYAN+"You have", numCoins(), "coins")
    print(Fore.CYAN+"You have", hasRestore(), "Auto-Restore systems")
    print(Fore.CYAN+"You have", hasGrenade(), "Electro-Stun Grenades")
    print(Fore.CYAN+"You have", hasHypospray(), "Health Hypospray units")
    print(Fore.CYAN+"You have", hasSurvivalRations(), "Survival food bars")
    print(Fore.CYAN+"*****************")


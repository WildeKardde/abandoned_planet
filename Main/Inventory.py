########
# Inventory.py
# Inventory system
########

inv = {
    "StructureKey": False,
    "Compass": False,
    "Survival Rations": False,
    "Coins": 0
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
    inv["Survival Rations"] = True

# Does the player have the survival rations?
def hasSurvivalRations():
    return inv["Survival Rations"]

# Display inventory
def display():
    print("*** Inventory ***")
    print("You have", numCoins(), "coins")
    if hasStructureKey():
        print("You have a key that flashes blue")
    if hasCompass():
        print("You have a magnetic compass,\n"
              "the arm sways slightly as you move.")
    if hasSurvivalRations():
        print("You have a box labeled Survival Gear.\n"
              "It contains a canteen of water, some food\n"
              "wafers, and a shiny metallic blanket.")
    print("*****************")


############
# Items
# Items that may be purchased
############

items = [
    {
        "id":"health",
        "description":"Health restoration hypospray.",
        "key":"H",
        "cost":10
    },
    {
        "id":"blaster",
        "description":"Laser blaster.",
        "key":"B",
        "cost":25
    },
    {
        "id":"grenades",
        "description":"3 Electro-Stun Grenades.",
        "key":"G",
        "cost":30
    },
    {
        "id":"shield",
        "description":"Kinetic shield which halves enemy damage.",
        "key":"S",
        "cost":50
    },
    {
        "id":"life",
        "description":"Auto-Restore",
        "key":"L",
        "cost":100
    },
]

# Get available items
# Return in format used by getUserChoice()
def getItems():
    # Variable for result
    result = []
    # Loop through items
    for item in items:
        # Create empty list
        i = []
        # Add key
        i.append(item["key"])
        # Add description and cost
        i.append(item["description"]+" ("+str(item["cost"])+")")
        # Add this item to the results
        result.append(i)
    # Return it
    return result
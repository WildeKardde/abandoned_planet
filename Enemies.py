##########
# Enemies
# Defines enemies, supporting functions
##########

# List of enemies
# Each needs a short name, a description,
# strength (Higher number = need to do more damage to kill)
# and defense (lower number = easier to hit)

enemies = [
    {
        "id":"slug",
        "description":"Space slug",
        "strength":10,
        "damageMin":1,
        "damageMax":3,
        "defense":2
    },
    {
        "id":"eel",
        "description":"Radioactive eel",
        "strength":50,
        "damageMin":10,
        "damageMax":15,
        "defense":1
    },
    {
        "id":"alien",
        "description":"Green tentacled alien",
        "strength":25,
        "damageMin":5,
        "damageMax":10,
        "defense":3
    }
]
#############
# Strings.py
# Externalized Strings
#############

def get(id):
    if id == "Welcome":
        return ("Welcome adventurer!\n"
                "You wake in a dze, recalling nothing useful.\n"
                "Stumbling, you reach for the door, it opens in "
                "anticipation.\nYou step outside.  Nothing is "
                "familiar.\nThe landscape is dusty, vast, tinged "
                "red, barren.\nYou notice that you are wearing "
                "a spacesuit.  Huh?")
    elif id == "Start":
        return ("You look around.  Red dust, a pile of boulders, "
                "more dust.\nThere are talls dunes rising behind "
                "the boulders\nThere's an odd octagon shaped "
                "structure in front of you.\nYou hear beeping "
                "nearby.  It stopped.  No, it didn't.")
    elif id == "Boulders":
        return ("Seriously?  They are boulders.\n"
                "Big, heavy, boring boulders.")
    elif id == "Crashsite":
        return ("A tangle of wreckage rising like the bones of some "
                "ancient metallic creature.\nIf you squint, you can "
                "think you see that it may once have been a spaceship.")
    elif id == "Dunes":
        return ("Tall sand dunes rise above you.\nClimbing to the "
                "crest, you see a horizon of broken rocks and more "
                "dust.\nNear the bottom of the dunes, you see a glint "
                "of metal inside of a crater.")
    elif id == "Wasteland":
        return ("Scattered, broken rocks fill the plain.\nYou see a "
                "tall outcropping rise above the flat near you.")
    elif id == "WastelandC":
        return ("Scattered, broken rocks fill the plain.\nYou are at "
                "the base of a tall stone outcropping, easy to climb.\n"
                "Deciding to do so, you are able to see an easy path "
                "to follow to return to the Dunes that border the desert.")
    elif id == "WastelandD":
         return ("The stony desert surrounds you.\nYou are unable to "
                 "find any escape, the meager dust\nswallowing the "
                 "footprints you left behind.\nYou collapse to the "
                 "ground, tired, thirsty, exhausted....and beaten.")
    elif id == "Structure":
        return ("You examine the odd structure.\n"
                "Eerily unearthly sounds seem to be coming from "
                "inside.\nYou see no doors or windows.\nWell, that "
                "outline might be a door, good luck opening it.\n"
                "And that beeping.  Where is it coming from?")
    elif id == "StructureDoor":
        return ("The door appears to be locked.\nYou see a small "
                "circular hole.  Is that the keyhole?")
    elif id == "StructureDoorNoKey":
        return("You move your hand towards it, it flashes blue "
               "and closes!\nWell, that didn't work as planned.")
    elif id == "Run":
        return ("You run, for a moment.\n"
                "And then you are floating.  Down down down.\n"
                "You've fallen into a chasm, never to be seen "
                "again.\nNot very brave, are you?")
    elif id == "GameOver":
        return "Game over!"
    elif id == "StructureDoorKey":
        return("You look at the key you are holding.\n"
               "It is flashing blue, as is the keyhole.")
    elif id == "BouldersKey":
        return ("You look closer.  Was that a blue flash?\n"
                "You reach between the boulders and find ...\n"
                "It looks like a key, it occasionally flashes blue.")
    elif id == "CrashCompass":
        return ("Amongst the wreckage you see a glint of glass.\n"
                "It appears to be a magnetic compass, the\n"
                "arm swinging slightly.")
    elif id == "CrashRations":
        return ("Pulling a scorched panel off a section of frame,\n"
                "you find a box marked 'Emergency Supplies'")
    elif id == "Boulder2":
        return("What's with you and boulders?\n"
               "They are still big, heavy, boring boulders.")
    else:
        return ""
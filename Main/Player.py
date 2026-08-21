##########
# Player.py
# player class
##########

# Define player class
class player:
    # Properties
    name = "Adventurer"
    livesLeft = 3
    boulderVisits = 0
    CrashsiteVisits = 0

# p = player()
# for att in dir(p):
#     print (att, getattr(p, att))

    # Get name property
    def getName(self):
        return self.name

    # Get number of lives left
    def getLivesLeft(self):
        return self.livesLeft

    # Player died
    def died(self):
        if self.liveLeft > 0:
            self.livesLeft-=1

    # Is player alive
    def isAlive(self):
        return True if self.livesLeft > 0 else False

    # Get number of times boulders were visited
    def getBoulderVisits(self):
        return self.boulderVisits

    # Player visited the boulders
    def visitBoulder(self):
        self.boulderVisits += 1

    # Get number of times crash site was visted
    def getCrashsiteVisits(self):
        return self.CrashsiteVisits

    # Player visited the crashsite
    def visitCrashsite(self):
        self.CrashsiteVisits += 1
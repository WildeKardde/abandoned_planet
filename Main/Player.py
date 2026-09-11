##########
# PlayerN.py
# player class
##########

# Define player class
class Player:
    # Properties
    name = "Adventurer"
    livesLeft = 3
    boulderVisits = 0
    crashsiteVisits = 0
    maxHealth = 100
    health = maxHealth

# p = player()
# for att in dir(p):
#     print (att, getattr(p, att))

    # Set name property
    def setName(self):
        self.name = input ("What would you like your character to be named?  ")

    # Get name property
    def getName(self):
        return self.name

    # Get number of lives left
    def getLivesLeft(self):
        return self.livesLeft

    # Player died
    def died(self):
        if self.livesLeft > 0:
            self.livesLeft -= 1

    # Is player alive
    def isAlive(self):
        return True if self.livesLeft > 0 else False

    # Get number of times boulders were visited
    def getBoulderVisits(self):
        return self.boulderVisits

    # Player visited the boulders
    def visitBoulder(self):
        self.boulderVisits += 1

    # Get number of times crash site was visited
    def getCrashsiteVisits(self):
        return self.crashsiteVisits

    # Player visited the crashsite
    def visitCrashsite(self):
        self.crashsiteVisits += 1

    # Add lives to player
    def addLife(self, lives = 1):
        # Increment lives
        self.livesLeft += lives
        # And fill up health
        self.health = self.maxHealth

    # Lose lives
    def loseLife(self, lives = 1):
        # Decrement lives
        self.livesLeft -= lives
        # Make sure didn't go below 0
        if self.livesLeft < 0:
            # It did, so set to 0
            self.livesLeft = 0
        # If no lives
        if self.livesLeft == 0:
            # No health either
            self.health = 0
        # If lives left
        elif self.livesLeft >= 1:
            # Reset health to full
            self.health = self.maxHealth

    # Get health value
    def getHealth(self):
        return self.health

    # Add health
    def addHealth(self, healthChange):
        self.health += healthChange
        # Make sure not over maxHealth
        if self.health > self.maxHealth:
            # Went too high, reset to max
            self.health = self.maxHealth

    # Lose health
    def loseHealth(self, healthChange):
        self.health -= healthChange
        # Make sure not < 0
        if self.health < 0:
            # Lose a life
            self.loseLife()

    # Show Lives and Health
    def display(self):
        print ("You have ", self.getLivesLeft(), " remaining lives.")
        print ("Your health is at: ", self.getHealth())

    # Determine Health via percentage of total
    def healthPercent(self):
        healthCurrent = self.health
        healthMax = self.maxHealth
        hpercent = 100 * (healthCurrent / healthMax)
        return hpercent





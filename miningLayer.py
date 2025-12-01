# layers
# 0 none
# 1 rock
# 2 iron
# 3 gold
# 4 - 10 ores
# 11 heli

class MiningLayer:

    def update(self):
        if(self.material == 0):
            self.name = "none"
        elif(self.material == 1):
            self.name = "rock"
        elif(self.material == 2):
            self.name = "iron"
        elif(self.material == 3):
            self.name = "gold"
        elif(self.material == 11):
            self.name = "heli"

    def __init__(self, known, material):
        self.known = known
        self.material = material
        self.name = "unde"
        self.update()

    def setKnown(self, known):
        self.known = known

    def getPrintout(self):
        if(self.material == 0):
            return("    ")
        else:
            if(self.known):
                return(self.name)
            else:
                return("----")
    
    def removeLayer(self):
        self.material = 0
        self.update()
        
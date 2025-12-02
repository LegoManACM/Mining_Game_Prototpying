# layers
# 0 none
# 1 rock
# 2 iron
# 3 gold
# 4 - 10 ores
# 11 heli

def nameFromLayerID(material):
    if(material == 0):
        return("none")
    elif(material == 1):
        return("rock")
    elif(material == 2):
        return("iron")
    elif(material == 3):
        return("gold")
    elif(material == 11):
        return("heli")
    else:
        return(-1)

class MiningLayer:

    def update(self):
        self.name = nameFromLayerID(self.material)

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
        
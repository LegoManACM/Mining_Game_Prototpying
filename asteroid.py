from miningLayer import MiningLayer

class Asteroid:
    def __init__(self, layers):
        self.layers = layers

    def getFirstSolid(self):
        firstSolid = -1
        for layer in self.layers:
            if(layer.material != 0 and firstSolid == -1):
                firstSolid = self.layers.index(layer)
        return(firstSolid)
    
    def fullyMined(self):
        for i in range(len(self.layers) - 1):
            if(self.layers[i].material != 0):
                return(False)
        return(True)
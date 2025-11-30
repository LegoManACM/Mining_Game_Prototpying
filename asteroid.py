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
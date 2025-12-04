from miningAction import MiningAction
from miningLayer import MiningLayer

class MiningActionScan(MiningAction):

    def __init__(self, name, speed, power):
        super().__init__(name, speed)
        self.power = power

    def use(self, game):
        modifiedLayers = game.asteroid.layers
        toScan = game.asteroid.getFirstSolid()
        if(toScan != -1):
            for i in range(toScan, toScan + self.power + 1):
                if(i < len(game.asteroid.layers)):
                    modifiedLayers[i].known = True
            
        return(modifiedLayers, [], self.speed)
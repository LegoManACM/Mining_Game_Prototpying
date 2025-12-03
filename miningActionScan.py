from miningLayer import MiningLayer

class MiningActionScan:

    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed

    def use(self, game):
        modifiedLayers = game.asteroid.layers
        toScan = game.asteroid.getFirstSolid()
        if(toScan != -1):
            for i in range(toScan, toScan + self.power + 1):
                if(i < len(game.asteroid.layers)):
                    modifiedLayers[i].known = True
            
        return(modifiedLayers, [], self.speed)
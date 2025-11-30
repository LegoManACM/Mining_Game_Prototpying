from miningAction import MiningAction
class MiningActionBlast (MiningAction):

    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def use(self, game):
        modifiedLayers = game.Asteroid.layers
        toDrill = game.Asteroid.getFirstSolid()
        if(toDrill != -1):
            for i in range(toDrill, toDrill + self.power):
                if(i < len(game.asteroid.layers)):
                    modifiedLayers[i].removeLayer()

        return super().use(modifiedLayers)
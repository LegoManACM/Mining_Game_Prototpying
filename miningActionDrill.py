from miningAction import MiningAction
class MiningActionDrill (MiningAction):

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def use(self, game):
        modifiedLayers = game.Asteroid.layers
        toDrill = game.Asteroid.getFirstSolid()
        if(toDrill != -1):
            modifiedLayers[toDrill].removeLayer()

        return super().use(modifiedLayers)
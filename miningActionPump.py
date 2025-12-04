from miningAction import MiningAction
class MiningActionPump (MiningAction):

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.speed = speed

    def use(self, game):
        modifiedLayers = game.asteroid.layers
        collectedResources = []
        toPump = game.asteroid.getFirstSolid() + 1
        if(toPump != -1):
            if(toPump <= len(modifiedLayers)):
                if(modifiedLayers[toPump].material == 11):
                    collectedResources.append(modifiedLayers[toPump].material)
                    modifiedLayers[toPump].removeLayer()
                    modifiedLayers[toPump].known = True
                    modifiedLayers[toPump].update() 

        return modifiedLayers, collectedResources, self.speed
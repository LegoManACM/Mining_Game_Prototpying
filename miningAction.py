from miningLayer import MiningLayer

class MiningAction:

    def __init__(self, name):
        self.name = name

    def use(self, game):
        return (game.asteroid.layers)
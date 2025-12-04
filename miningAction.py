from miningLayer import MiningLayer

class MiningAction:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def use(self, game):
        return (game.asteroid.layers)
    
    def getPrint(self):
        turnTicks = ">" * self.speed
        spaces = " " * (4-self.speed)
        return(turnTicks + spaces + " " + self.name)
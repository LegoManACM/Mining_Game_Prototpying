from asteroid import Asteroid
from miningLayer import MiningLayer

from miningAction import MiningAction
from miningActionDrill import MiningActionDrill
from miningActionBlast import MiningActionBlast

class Game:

    def setupGame(self):
        layers = [MiningLayer(True,  0),
                  MiningLayer(True,  1),
                  MiningLayer(False, 1),
                  MiningLayer(False, 2),
                  MiningLayer(True,  2),
                  MiningLayer(False, 1),
                  MiningLayer(True,  3),
                  MiningLayer(False, 3)]

        self.asteroid = Asteroid(layers)

        self.actions = [MiningActionDrill("Standard Drill", 1),
                        MiningActionDrill("Advanced Drill", 2),
                        MiningActionBlast("Standard Blast", 3),
                        MiningActionBlast("Standard Blast", 5)]


    def __init__(self, turns):
        self.turns = turns
        self.currentTurn = 0
        self.setupGame()
        self.gameLoopState = 0

    def doGameLoop(self):
        if(self.gameLoopState == 0):   # choose mining action
            pass
        elif(self.gameLoopState == 1): # collect resources
            pass
        elif(self.gameLoopState == 2): # wrap-up
            pass

    def playGame(self):
        playing = True
        while playing:
            self.doGameLoop()



    


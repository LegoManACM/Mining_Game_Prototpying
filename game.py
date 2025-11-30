from asteroid import Asteroid
from miningLayer import MiningLayer

from miningAction import MiningAction
from miningActionDrill import MiningActionDrill
from miningActionBlast import MiningActionBlast
from miningActionScan import MiningActionScan

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
                        MiningActionBlast("Advanced Blast", 5),
                        MiningActionScan("Standard Scan",   3)]


    def __init__(self, turns):
        self.turns = turns
        self.currentTurn = 0
        self.setupGame()
        self.gameLoopState = 0

    def presentMiningLayers(self):
        for layer in self.asteroid.layers:
            print("[" + layer.getPrintout() + "]")

    def presentMiningActions(self):
        print("\nAvailible Actions")
        for i in range(0, len(self.actions)):
            print(">>-> " + str(i) + " " + self.actions[i].name)

    def doActionLoop(self):
        cInput = ""
        deliberating = True
        while deliberating:
            self.presentMiningActions()
            cInput = input("\n...")
            if(int(cInput) != None):
                if(int(cInput) < len(self.actions) and int(cInput) >= 0):
                    deliberating = False
                    cInput = int(cInput)
                else:
                    print("enter a number between 0 and " + str(len(self.actions) - 1))
            else:
                print("please enter an integer")
                
        self.asteroid.layers = self.actions[cInput].use(self)


    def doGameLoop(self):
        if(self.gameLoopState == 0):   # choose mining action
            self.presentMiningLayers()
            self.gameLoopState += 1     
        elif(self.gameLoopState == 1): # collect resources
            self.doActionLoop()    
            self.gameLoopState = 0
        elif(self.gameLoopState == 2): # wrap-up
            pass

    def playGame(self):
        playing = True
        while playing:
            self.doGameLoop()



    


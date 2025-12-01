from asteroid import Asteroid
from miningLayer import MiningLayer

from miningAction import MiningAction
from miningActionDrill import MiningActionDrill
from miningActionBlast import MiningActionBlast
from miningActionScan import MiningActionScan
from miningActionPump import MiningActionPump

from time import sleep
import os

class Game:

    def setupGame(self):
        layers = [MiningLayer(True,  0),
                  MiningLayer(True,  1),
                  MiningLayer(False, 11),
                  MiningLayer(False, 2),
                  MiningLayer(True,  2),
                  MiningLayer(False, 1),
                  MiningLayer(True,  3),
                  MiningLayer(False, 3)]

        self.asteroid = Asteroid(layers)

        self.actions = [MiningActionDrill("Standard Drill", 1),
                        #MiningActionDrill("Advanced Drill", 1),
                        MiningActionBlast("Standard Blast", 2),
                        #MiningActionBlast("Advanced Blast", 5),
                        MiningActionScan("Standard Scan",   2),
                        MiningActionPump("Standard Pump", 1)]
                        


    def __init__(self, turns):
        self.turns = turns
        self.currentTurn = 0
        self.shipIntegrity = 3
        self.setupGame()
        self.gameLoopState = 0
        self.playing = True

    def damageShip(self, amount):
        self.shipIntegrity -= amount
        if(self.shipIntegrity <= 0):
            self.gameLoopState = -1

    def presentMiningLayers(self):
        toReturn = ""
        for layer in self.asteroid.layers:
            toReturn += ("[" + layer.getPrintout() + "]")
            toReturn += "\n"
        return(toReturn)

    def presentMiningActions(self):
        toReturn = ""
        toReturn += "Mounted Equiptment"
        for i in range(0, len(self.actions)):
            toReturn += ("\n>>-> " + str(i) + " " + self.actions[i].name)
        return(toReturn)

    def presentMiningMenu(self):
        linesLayers = self.presentMiningLayers().splitlines()
        linesActions = self.presentMiningActions().splitlines()

        toPrint = ""

        rows = len(linesLayers)
        if(len(linesActions) > rows):
            rows = len(linesActions)
        
        for i in range(0, rows):
            toPrint += "|  "
            if(i < len(linesLayers)):
                toPrint += linesLayers[i]
            toPrint += "  |  "
            if(i < len(linesActions)):
                toPrint += linesActions[i]
            toPrint += "\n"

        print(toPrint)


    def inputErrorMessage(self):
        os.system('cls')
        print("\n\n\n")
        print("[Please enter an integer 0 - " + str(len(self.actions) - 1) + "]")
        sleep(5)

    def doActionLoop(self):
        cInput = ""
        deliberating = True
        while deliberating:
            os.system('cls')
            self.presentMiningMenu()
            cInput = input("\nSelect Equiptment:\n     ")
            if(cInput.isdigit()):
                if(int(cInput) != None):
                    if(int(cInput) < len(self.actions) and int(cInput) >= 0):
                        deliberating = False
                        cInput = int(cInput)
                    else:
                        self.inputErrorMessage()
            else:
                self.inputErrorMessage()
                
        self.asteroid.layers = self.actions[cInput].use(self)


    def doGameLoop(self):
        if(self.gameLoopState == -1):
            print("Ship Destroyed\nGame Over\n\nClosing in:\n5")
            sleep(1)
            print("4")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            self.playing = False
        elif(self.gameLoopState == 0):   # choose mining action
            os.system('cls')
            self.gameLoopState += 1     
        elif(self.gameLoopState == 1): # collect resources
            self.doActionLoop()    
            self.gameLoopState = 2
        elif(self.gameLoopState == 2): # wrap-up
            first = self.asteroid.getFirstSolid()
            if(first != -1):
                self.asteroid.layers[first].known = True
                self.asteroid.layers[first].update()
                self.gameLoopState = 3
            else:
                self.gameLoopState = 4
        elif(self.gameLoopState == 3):
            first = self.asteroid.getFirstSolid()
            if(first != -1):
                if(self.asteroid.layers[first].material == 11):
                    self.gameLoopState = 2
                    self.damageShip(1)
                    self.asteroid.layers[first].removeLayer()
                    self.asteroid.layers[first].update()
                    print("\n\nStruck By Gas Pocket")
                    sleep(3)
                else:
                    self.gameLoopState = 0
                    

            #self.gameLoopState = 0
        elif(self.gameLoopState == 4):
            print("Asteroid complete\nClosing in:\n5")
            sleep(1)
            print("4")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            self.playing = False

    def playGame(self):
        self.playing = True
        while self.playing:
            self.doGameLoop()



    


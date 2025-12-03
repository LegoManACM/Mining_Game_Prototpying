from asteroid import Asteroid
from miningLayer import MiningLayer
from miningLayer import nameFromLayerID

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
                        MiningActionScan("Standard Scan", 2, 2),
                        MiningActionPump("Standard Pump", 1)]
                        


    def __init__(self, turns):
        self.turns = turns
        self.currentTurn = 0
        self.shipIntegrity = 3
        self.setupGame()
        self.gameLoopState = 0
        self.playing = True
        self.shipInventory = []
        self.maxShipInventory = 5
        self.storageInventory = []
        self.money = 10

    def countOut(self):
        print("\nClosing In:")
        for i in range(5):
            print(" [" + str(5-i) + "]", end="\r")
            sleep(1)
        self.playing = False

    def damageShip(self, amount):
        self.shipIntegrity -= amount
        if(self.shipIntegrity <= 0):
            self.gameLoopState = -1

    def presentMiningLayers(self):
        topLayer = self.asteroid.getFirstSolid()
        toReturn = ""
        for i in range(len(self.asteroid.layers) - 1):
            capsulePrint = " [ ", " ] "
            if(i == topLayer):
                capsulePrint = ">[ ", " ]<"
            toReturn += (capsulePrint[0] + self.asteroid.layers[i].getPrintout() + capsulePrint[1])
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
            toPrint += "| "
            if(i < len(linesLayers)):
                toPrint += linesLayers[i]
            toPrint += " |  "
            if(i < len(linesActions)):
                toPrint += linesActions[i]
            toPrint += "\n"

        print(toPrint)
        sleep(0.5)
        print("Current Turn: " + str(self.currentTurn) + "/" + str(self.turns))


    def inputErrorMessage(self):
        os.system('cls')
        print("\n\n\n")
        print("[Please enter an integer 0 - " + str(len(self.actions) - 1) + "]")
        sleep(1)

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

        itemUse = self.actions[cInput].use(self)
        newLayers = itemUse[0]
        turnsTaken = itemUse[2]
        self.currentTurn += turnsTaken
        self.asteroid.layers = newLayers

        self.shipInventory.extend(itemUse[1])

    def doHaulPrintout(self):
        os.system('cls')
        print("Collected:\n")
        resources = []
        toPrint = ""
        for i in [1,2,3,11]:
            ofTypei = [x for x in self.shipInventory if x == i]
            resources.append(ofTypei)
            toPrint += nameFromLayerID(i) + "-[" + str(len(ofTypei)) + "]\n"
        print(toPrint)


    def doGameLoop(self):
        if(self.gameLoopState == -1):
            print("Ship Destroyed\nGame Over")
            self.countOut()
        elif(self.gameLoopState == 0):   # clear screen
            os.system('cls')
            self.gameLoopState += 1     
        elif(self.gameLoopState == 1): # take action
            self.doActionLoop()    
            self.gameLoopState = 2
        elif(self.gameLoopState == 2): # wrap-up
            first = self.asteroid.getFirstSolid()
            if(first != -1):
                self.asteroid.layers[first].known = True
                self.asteroid.layers[first].update()
            self.gameLoopState = 3
        elif(self.gameLoopState == 3): # check for gas leakage
            first = self.asteroid.getFirstSolid()
            self.gameLoopState = 4  
            if(first != -1):
                if(self.asteroid.layers[first].material == 11):
                    self.gameLoopState = 2
                    self.damageShip(1)
                    self.asteroid.layers[first].removeLayer()
                    self.asteroid.layers[first].update()
                    print("\n\nStruck By Gas Pocket")
                    sleep(3)
        elif(self.gameLoopState == 4):
            if(self.asteroid.fullyMined() == True or self.currentTurn >= self.turns):
                self.gameLoopState = -2
            else:
                self.gameLoopState = 0
                       
        elif(self.gameLoopState == -2):
            print("Asteroid complete")
            sleep(3)
            self.doHaulPrintout()
            sleep(2)
            input("Press return to continue...")
            self.countOut()

    def playGame(self):
        self.playing = True
        while self.playing:
            self.doGameLoop()



    


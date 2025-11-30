from time import sleep
from miningLayer import MiningLayer
from miningAction import MiningAction
from game import Game

game = Game(5)


def printoutLayers():
    for layer in game.asteroid.layers:
        print("[" + layer.getPrintout() + "]")

playing = True
while playing:

    print("\n")
    print("Layers")
    printoutLayers()
    print("\n")

    cInput = input("...")


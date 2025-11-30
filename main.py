from time import sleep
from miningLayer import MiningLayer
from miningAction import MiningAction
from game import Game

game = Game(5)

playing = True
while playing:

    game.playGame()


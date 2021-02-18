import random
import sys

import pygame

from constantes import SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game
from menu import Menu

pygame.init()

pygame.display.set_caption("BoomeurMan")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

global ScoreP1
global ScoreP2

ScoreP1 = 0
ScoreP2 = 0


def loadmenu():
    menu = Menu()
    background = menu.background
    background = pygame.transform.scale(background, (1920, 1080))
    while menu.onMenu:
        screen.blit(background, (0, 0))
        menu.buttons.draw(screen)
        pygame.display.flip()
        menu.update()


def loadlevel(level, Score1, Score2):
    game = Game(level, Score1, Score2)  # Initialise la partie
    background = game.background
    background = pygame.transform.scale(background, (1920, 1080))
    while not game.game_ended:
        screen.blit(background, (0, 0))
        # Dessine les objets
        game.Unbreakable.draw(screen)
        game.Breakable.draw(screen)
        game.bombes.draw(screen)
        game.explosions.draw(screen)
        game.players.draw(screen)
        game.powerUp.draw(screen)
        game.icones.draw(screen)
        game.Trous.draw(screen)
        # Fin Dessine les objets
        pygame.display.flip()  # Recharger l'ecran
        game.update()
    if game.ScoreP1 == True:
        global ScoreP1
        ScoreP1 += 1
    if game.ScoreP2 == True:
        global ScoreP2
        ScoreP2 += 1
    del game


def gameloop():  # gameloop
    loadmenu()
    while ScoreP1 != 3 and ScoreP2 != 3:
        screen.fill((109, 109, 109))
        loadlevel(random.randint(0, 2), ScoreP1, ScoreP2)


gameloop()
sys.exit()

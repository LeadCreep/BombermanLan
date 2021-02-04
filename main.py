from menu import Menu
import pygame
from game import Game
from constantes import SCREEN_HEIGHT, SCREEN_WIDTH
import sys


pygame.init()

pygame.display.set_caption("BoomeurMan")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def loadmenu():
    menu = Menu()
    background = menu.background
    background = pygame.transform.scale(background, (1920, 1080))
    while menu.onMenu:
        screen.blit(background, (0, 0))
        menu.buttons.draw(screen)
        pygame.display.flip()
        menu.update()


def loadlevel(level):
    game = Game(level)  # Initialise la partie
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
    del game


def gameloop():  # gameloop
    loadmenu()
    screen.fill((109, 109, 109))
    loadlevel(0)


gameloop()
sys.exit()

import pygame
from game import Game
from constantes import SCREEN_HEIGHT, SCREEN_WIDTH
import sys


pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/maptest.png")
background = pygame.transform.scale(background, (1920, 1080))

game = Game()  # Initialise la partie


def gameloop():  # gameloop
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
        pygame.display.flip()  # Recharger l'ecrans
        game.update()


gameloop()
sys.exit()

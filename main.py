import pygame
import sys
from pygame.locals import *
from game import Game
from constantes import *
from datetime import datetime, timedelta
pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/background.png")

debugfps = 0

game = Game()

# gameloop
while 1:
    debugfps = datetime.now()
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.walls_groupe.draw(screen)
    game.bombes.draw(screen)
    game.explosions.draw(screen)
    pygame.display.flip()
    game.update()
    print(datetime.now() - debugfps)

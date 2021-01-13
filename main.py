import pygame
from game import Game
from constantes import SCREEN_HEIGHT, SCREEN_WIDTH


pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/map.png")

game = Game()

# gameloop
while 1:
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.Unbreakable.draw(screen)
    game.Breakable.draw(screen)
    game.bombes.draw(screen)
    game.explosions.draw(screen)
    game.players.draw(screen)
    game.powerUp.draw(screen)
    pygame.display.flip()
    game.update()

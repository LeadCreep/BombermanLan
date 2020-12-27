import pygame

from constantes import SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game

pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/map.png")

debugfps = 0

game = Game()

# gameloop
while 1:
    #debugfps = datetime.now()
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.walls_groupe.draw(screen)
    game.bombes.draw(screen)
    game.explosions.draw(screen)
    game.players.draw(screen)
    pygame.display.flip()
    game.update()
    # print(th_R.message_recu)
    #print(datetime.now() - debugfps)

import pygame
import sys
import socket
from pygame.locals import *
from game import Game
from constantes import *
from datetime import datetime, timedelta
from connect import BoiteDeDialogue, ThreadEmission, ThreadReception
pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/background.png")

debugfps = 0

game = Game()

# Connection au Serveur


def connection():
    Boite = BoiteDeDialogue()
    Boite.runFenetre()
    HOST = Boite.AdresseIp
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion.connect((HOST, PORT))
    except socket.error:
        print("Connection Non Etablie")
        sys.exit()
    print("Connection Etablie !")
    global th_E
    th_E = ThreadEmission(connexion)
    th_R = ThreadReception(connexion)
    th_E.name = "Ha bon"
    th_R.name = "Bah il prend pas ses balles"
    th_E.start()
    th_R.start()
<<<<<<< HEAD
    th_E.envoyer(str(Boite.nom))
=======
    th_E.envoyer(Boite.Nom)
>>>>>>> 40db61b25d746271624ffcfd1690aed5d851bd52


connection()

# gameloop
while 1:
    debugfps = datetime.now()
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.walls_groupe.draw(screen)
    game.bombes.draw(screen)
    game.explosions.draw(screen)
    game.bots.draw(screen)
    pygame.display.flip()
    game.update()
    print(datetime.now() - debugfps)

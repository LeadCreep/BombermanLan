#from datetime import datetime
import json
import socket
import sys

import pygame

from connect import BoiteDeDialogue, ThreadEmission, ThreadReception
from constantes import PORT, SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game

pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/background.png")

debugfps = 0

game = Game()

# Connection au Serveur


Boite = BoiteDeDialogue()
Boite.runFenetre()
HOST = Boite.AdresseIp
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((HOST, PORT))
except socket.error:
    print("Connection Non Etablie")
    sys.quit()
print("Connection Etablie !")
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()
th_E.envoyer(str(Boite.nom))
# th_E.envoyer("FIN")


def sendPlayerPos():
    th_E.envoyer(json.dumps([game.player.x, game.player.y]))


def placeBots():
    try:
        print(th_R.message)
        coBot = th_R.message
        print(type(coBot))
        game.playerBot1.place(coBot[0], coBot[1])

    except TypeError:
        coBot = th_R.message_recu
        print("Erreur d'attribus")
        print(type(coBot))


# gameloop
while 1:
    #debugfps = datetime.now()
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.walls_groupe.draw(screen)
    game.bombes.draw(screen)
    game.explosions.draw(screen)
    game.bots.draw(screen)
    pygame.display.flip()
    game.update()
    sendPlayerPos()
    placeBots()
    # print(th_R.message_recu)
    #print(datetime.now() - debugfps)

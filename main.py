#from datetime import datetime
import json
import socket
import sys
from datetime import datetime

import pygame

from connect import BoiteDeDialogue, ThreadEmission, ThreadReception
from constantes import PORT, SCREEN_HEIGHT, SCREEN_WIDTH
from game import Game


# Connection au Serveur
Boite = BoiteDeDialogue()
Boite.runFenetre()
HOST = Boite.AdresseIp
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((HOST, PORT))
except socket.error:
    print("[", str(datetime.now()), "]", "Connection Non Etablie")
    sys.quit()
print("[", str(datetime.now()), "]", "Connection Etablie !")
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()
th_E.envoyer(str(Boite.nom))

pygame.init()

pygame.display.set_caption("BombermanMVM")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("assets/map.png")

debugfps = 0

game = Game()


def sendPlayerPos():
    th_E.envoyer(json.dumps([str(Boite.nom), game.player.x, game.player.y]))


def placeBots():
    try:
        coBot = th_R.message
        game.playerBot1.place(coBot[1], coBot[2])

    except TypeError:
        print("TypeError")


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

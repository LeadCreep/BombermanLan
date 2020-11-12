import pygame
import sys
from pygame.locals import *
from bombes import Bombe
from player import Player
from walls import Wall
from constantes import *
from levels import *


class Game:
    def __init__(self):
        # GENERATION DU JOUEUR
        self.player = Player(self, 9, 5)
        self.walls_groupe = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.generate_map()
        self.bombeIsDecounting = False
        self.explosionAppening = False

    def update(self):  # Update méthode
        self.event()
        self.player.update()
        if self.bombeIsDecounting == True:
            self.bombe.update()
        if self.explosionAppening == True:
            self.bombe.explosion.update()

    def check_collision(self, sprite, group):  # Check la collision
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def generate_map(self):  # Generer la map
        uLongeurWall = 0
        uHauteurWall = 0
        TailleDeMap = TAILLE_DE_MAP
        for i in liste_levels[0]:
            if i == 1:
                wall = Wall(self, OFFSET_WIDTH+uLongeurWall,
                            OFFSET_HEIGHT+uHauteurWall)
                self.walls_groupe.add(wall)
            uLongeurWall += 1
            if uLongeurWall == TAILLE_DE_MAP:
                uLongeurWall = 0
                uHauteurWall += 1

    def quit(self):  # Quitter
        pygame.quit()
        sys.exit()

    def event(self):  # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUITER LE JEU
                self.quit()
            if event.type == pygame.KEYDOWN:  # QUAND LE BOUTTON EST PRESS
                if event.key == K_UP:
                    self.player.move(dy=-1)
                if event.key == K_DOWN:
                    self.player.move(dy=1)
                if event.key == K_LEFT:
                    self.player.move(dx=-1)
                if event.key == K_RIGHT:
                    self.player.move(dx=1)
                if event.key == K_SPACE:
                    if self.bombeIsDecounting == False and self.explosionAppening == False:
                        self.bombe = Bombe(self, self.player.x, self.player.y)
                        self.bombeIsDecounting = True
                        self.bombe.mettreEnPlaceBombe()

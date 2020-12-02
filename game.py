import sys

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP

from bombes import Bombe
from bots import Bot
from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TAILLE_DE_MAP
from levels import liste_levels
from player import Player
from walls import Wall


class Game:
    def __init__(self):
        # GENERATION DU JOUEUR
        self.player = Player(self, 9, 5)
        self.walls_groupe = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.bots = pygame.sprite.Group()
        self.generate_map()
        self.playerBot1 = Bot(self, 10, 5, 0)
        self.bombeIsDecounting = False
        self.explosionAppening = False
        self.deathState = False
        self.bombe = None

    def update(self):  # Update méthode
        self.event()
        self.playerBot1.update()
        self.player.update()
        if self.bombeIsDecounting:
            self.bombe.update()
        if self.explosionAppening:
            self.bombe.explosion.update()
        for explosion in self.explosions:
            if self.player.rect.x == explosion.rect.x and self.player.rect.y == explosion.rect.y:
                self.deathState = True
                self.player.image = self.player.imageliste[1]

    def check_collision(self, sprite, group):  # Check la collision
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def generate_map(self):  # Generer la map
        uLongeurWall = 0
        uHauteurWall = 0
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
                if not self.deathState:
                    if event.key == K_UP:
                        self.player.move(dy=-1)
                    if event.key == K_DOWN:
                        self.player.move(dy=1)
                    if event.key == K_LEFT:
                        self.player.move(dx=-1)
                    if event.key == K_RIGHT:
                        self.player.move(dx=1)
                    if event.key == K_SPACE:
                        if not self.bombeIsDecounting and not self.explosionAppening:
                            self.bombe = Bombe(
                                self, self.player.x, self.player.y)
                            self.bombeIsDecounting = True
                            self.bombe.mettreEnPlaceBombe()

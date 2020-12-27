import sys

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_KP0, K_w, K_a, K_s, K_d, K_e

from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TAILLE_DE_MAP
from levels import liste_levels
from player import Player
from walls import Wall


class Game:
    def __init__(self):
        # GENERATION DU JOUEUR
        self.players = pygame.sprite.Group()
        self.player = Player(self, 9, 5)
        self.player2 = Player(self, 10, 5)
        self.player2.image = self.player2.imageliste[1]
        self.walls_groupe = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.generate_map()
        self.bombeIsDecounting = False
        self.explosionAppening = False
        self.bombe = None

    def update(self):  # Update méthode
        self.event()
        for player in self.players:
            player.update()
            if player.bombeIsDecounting:
                player.bombe.update()
            if player.explosionAppening:
                player.bombe.explosion.update()
        for explosion in self.explosions:
            for player in self.players:
                if player.rect.x == explosion.rect.x and player.rect.y == explosion.rect.y:
                    player.deathState = True

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
                if not self.player.deathState:
                    if event.key == K_UP:  # Bouger en Haut
                        self.player.move(dy=-1)
                    if event.key == K_DOWN:  # Bouger en Bas
                        self.player.move(dy=1)
                    if event.key == K_LEFT:  # Bouger a Gauche
                        self.player.move(dx=-1)
                    if event.key == K_RIGHT:  # Bouger a Droite
                        self.player.move(dx=1)
                    if event.key == K_KP0:  # Générer la Bombe
                        if not self.player.bombeIsDecounting and not self.player.explosionAppening:
                            self.player.bombeIsDecounting = True
                            self.player.SetBombe()
                if not self.player2.deathState:
                    if event.key == K_w:  # Bouger en Haut
                        self.player2.move(dy=-1)
                    if event.key == K_s:  # Bouger en Bas
                        self.player2.move(dy=1)
                    if event.key == K_a:  # Bouger a Gauche
                        self.player2.move(dx=-1)
                    if event.key == K_d:  # Bouger a Droite
                        self.player2.move(dx=1)
                    if event.key == K_e:  # Générer la Bombe
                        if not self.player2.bombeIsDecounting and not self.player2.explosionAppening:
                            self.player2.bombeIsDecounting = True
                            self.player2.SetBombe()

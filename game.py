import random
import sys

import pygame
from pygame.constants import K_q, K_z
from pygame.locals import (K_DOWN, K_KP0, K_LEFT,
                           K_RIGHT, K_UP, K_d, K_e, K_q, K_s, K_z)

from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TAILLE_DE_MAP
from levels import liste_levels
from player import Player, SpawnPoint
from walls import Breakable_Walls, Wall


class Game:
    def __init__(self):
        # GENERATION DU JOUEUR
        self.Unbreakable = pygame.sprite.Group()
        self.Breakable = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.spawns = []
        self.generate_map()
        self.SpawnPlayers()
        self.player2.image = self.player2.imageliste[1]
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
        for thing in self.Breakable:
            thing.isDestroyed()
        for explosion in self.explosions:
            for player in self.players:
                if player.rect.x == explosion.rect.x and player.rect.y == explosion.rect.y:
                    player.deathState = True

    def check_collision(self, sprite, group):  # Check la collision
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def generate_map(self):  # Generer la map
        uLongeurWall = 0
        uHauteurWall = 0
        for i in liste_levels[1]:
            if i == 1:
                wall = Wall(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Unbreakable.add(wall)
            elif i == 2:
                breakableWall = Breakable_Walls(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Breakable.add(breakableWall)
            elif i == 3:
                spawn = SpawnPoint(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.spawns.append(spawn)
            uLongeurWall += 1
            if uLongeurWall == TAILLE_DE_MAP:
                uLongeurWall = 0
                uHauteurWall += 1

    def SpawnPlayers(self):
        spawnChoisi = random.choice(self.spawns)
        self.player = Player(self, spawnChoisi.x, spawnChoisi.y)
        self.spawns.remove(spawnChoisi)
        # 2eme Joueur
        spawnChoisi = random.choice(self.spawns)
        self.player2 = Player(self, spawnChoisi.x, spawnChoisi.y)
        self.spawns.remove(spawnChoisi)

    def quit(self):  # Quitter
        pygame.quit()
        sys.exit()

    def event(self):  # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUITER LE JEU
                self.quit()
            if event.type == pygame.KEYDOWN:  # QUAND LE BOUTTON EST PRESS
                if not self.player.deathState:
                    if event.key == K_z:  # Bouger en Haut
                        self.player.move(dy=-1)
                    if event.key == K_s:  # Bouger en Bas
                        self.player.move(dy=1)
                    if event.key == K_q:  # Bouger a Gauche
                        self.player.move(dx=-1)
                    if event.key == K_d:  # Bouger a Droite
                        self.player.move(dx=1)
                    if event.key == K_e:  # Générer la Bombe
                        if not self.player.bombeIsDecounting and not self.player.explosionAppening:
                            self.player.bombeIsDecounting = True
                            self.player.SetBombe()
                if not self.player2.deathState:
                    if event.key == K_UP:  # Bouger en Haut
                        self.player2.move(dy=-1)
                    if event.key == K_DOWN:  # Bouger en Bas
                        self.player2.move(dy=1)
                    if event.key == K_LEFT:  # Bouger a Gauche
                        self.player2.move(dx=-1)
                    if event.key == K_RIGHT:  # Bouger a Droite
                        self.player2.move(dx=1)
                    if event.key == K_KP0:  # Générer la Bombe
                        if not self.player2.bombeIsDecounting and not self.player2.explosionAppening:
                            self.player2.bombeIsDecounting = True
                            self.player2.SetBombe()

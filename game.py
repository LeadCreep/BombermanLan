#####IMPORTS#####
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
#####IMPORTS#####


class Game:
    def __init__(self):  # Démarrage du jeu
        self.Unbreakable = pygame.sprite.Group()
        self.Breakable = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.spawns = []
        self.generate_map()
        self.SpawnPlayers()
        self.player2.image = self.player2.imageliste[1]
        self.bombeIsDecounting = self.explosionAppening = False
        self.bombe = None

    def update(self):  # Update méthode qui tourne toutes les frames
        self.event()  # Update pour les touches
        for player in self.players:  # Updates pour joueurs et bombes
            player.update()
            if player.bombeIsDecounting:
                player.bombe.update()
            if player.explosionAppening:
                player.bombe.explosion.update()
            for explosion in self.explosions:
                if player.rect.x == explosion.rect.x and player.rect.y == explosion.rect.y:
                    player.deathState = True
        for thing in self.Breakable:  # Update pour les choses cassables
            thing.isDestroyed()

    def generate_map(self):  # Generer la map
        uLongeurWall = 0
        uHauteurWall = 0
        for i in liste_levels[0]:  # Scan D'objets dans le level
            if i == 1:  # Mur
                wall = Wall(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Unbreakable.add(wall)
            elif i == 2:  # Mur cassable
                breakableWall = Breakable_Walls(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Breakable.add(breakableWall)
            elif i == 3:  # SpawnPoint
                spawn = SpawnPoint(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.spawns.append(spawn)
            uLongeurWall += 1
            if uLongeurWall == TAILLE_DE_MAP:
                uLongeurWall = 0
                uHauteurWall += 1

    def SpawnPlayers(self):  # Choisir 2 point de spawn parmi tout ceux de la map
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
        for event in pygame.event.get():  # Pour Chaque Evenement
            if event.type == pygame.QUIT:  # Quitter le jeu
                self.quit()
            if event.type == pygame.KEYDOWN:  # Quand un boutton est pressé
                if not self.player.deathState:  # Touches Player 1
                    if event.key == K_z:  # Bouger en Haut
                        self.player.move(dy=-1)
                    if event.key == K_s:  # Bouger en Bas
                        self.player.move(dy=1)
                    if event.key == K_q:  # Bouger a Gauche
                        self.player.move(dx=-1)
                    if event.key == K_d:  # Bouger a Droite
                        self.player.move(dx=1)
                    if event.key == K_e and not self.player.bombeIsDecounting and not self.player.explosionAppening:  # Générer la Bombe
                        self.player.SetBombe()
                if not self.player2.deathState:  # Touches Player 2
                    if event.key == K_UP:  # Bouger en Haut
                        self.player2.move(dy=-1)
                    if event.key == K_DOWN:  # Bouger en Bas
                        self.player2.move(dy=1)
                    if event.key == K_LEFT:  # Bouger a Gauche
                        self.player2.move(dx=-1)
                    if event.key == K_RIGHT:  # Bouger a Droite
                        self.player2.move(dx=1)
                    if event.key == K_KP0 and not self.player2.bombeIsDecounting and not self.player2.explosionAppening:  # Générer la Bombe
                        self.player2.SetBombe()

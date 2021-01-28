#####IMPORTS#####
import random

import pygame
from pygame.locals import (K_DOWN, K_KP0, K_LEFT, K_RIGHT, K_UP, K_d, K_e, K_q,
                           K_s, K_z, K_ESCAPE)

from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TAILLE_DE_MAP
from levels import liste_levels
from player import Player, SpawnPoint, Icone
from powerup import PW2, PWLongRange, SpawnerPW
from walls import Breakable_Walls, Trou, Wall
#####IMPORTS#####


class Game:
    def __init__(self):  # Démarrage du jeu
        self.game_ended = False
        self.Unbreakable = pygame.sprite.Group()
        self.Breakable = pygame.sprite.Group()
        self.bombes = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.powerUp = pygame.sprite.Group()
        self.icones = pygame.sprite.Group()
        self.Trous = pygame.sprite.Group()
        self.spawns = []
        self.PWspawns = []
        self.TypesPW = ['LongRange']
        self.generate_map()
        self.spawnPlayers()
        self.spawnPowerUps()
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
        for thing in self.powerUp:  # Update pour les power ups
            thing.update()

    def generate_map(self):  # Generer la map
        uLongeurWall = 0
        uHauteurWall = 0
        for object in liste_levels[2]:  # Scan D'objets dans le level
            if object == 1:  # Mur
                wall = Wall(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Unbreakable.add(wall)
            elif object == 2:  # Mur cassable
                breakableWall = Breakable_Walls(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Breakable.add(breakableWall)
            elif object == 3:  # SpawnPoint
                spawn = SpawnPoint(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.spawns.append(spawn)
            elif object == 4:  # Spawns des PowerUps
                PWspawn = SpawnerPW(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.PWspawns.append(PWspawn)
            elif object == 5:  # Trous
                trou = Trou(
                    self, OFFSET_WIDTH+uLongeurWall, OFFSET_HEIGHT+uHauteurWall)
                self.Trous.add(trou)
            uLongeurWall += 1
            if uLongeurWall == TAILLE_DE_MAP:
                uLongeurWall = 0
                uHauteurWall += 1

        # Générer les icones des joueurs
        icone1 = Icone(self, 96, 100)
        self.icones.add(icone1)
        icone2 = Icone(self, 1569, 100)
        icone2.image = icone2.imageliste[1]
        self.icones.add(icone2)

    def spawnPlayers(self):  # Choisir 2 point de spawn parmi tout ceux de la map
        spawnChoisi = random.choice(self.spawns)
        self.player = Player(self, spawnChoisi.x, spawnChoisi.y)
        self.spawns.remove(spawnChoisi)
        # 2eme Joueur
        spawnChoisi = random.choice(self.spawns)
        self.player2 = Player(self, spawnChoisi.x, spawnChoisi.y)
        self.spawns.remove(spawnChoisi)

    def spawnPowerUps(self):  # Spawn les power ups
        for spawn in self.PWspawns:
            chance = random.random()
            power = None
            if chance < 0.70:
                powerChoisi = random.choice(self.TypesPW)
                if powerChoisi == 'LongRange':
                    power = PWLongRange(self, spawn.x, spawn.y)
                elif powerChoisi == 'PW2':
                    power = PW2(self, spawn.x, spawn.y)
                self.powerUp.add(power)

    def quit(self):  # Quitter
        self.game_ended = True

    def event(self):  # Events
        for event in pygame.event.get():  # Pour Chaque Evenement
            if event.type == pygame.QUIT:  # Quitter le jeu
                self.quit()
            if event.type == pygame.KEYDOWN:  # Quand un boutton est pressé
                if event.key == K_ESCAPE:
                    self.quit()  # Quitter le jeu
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
                        self.player.setBombe()
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
                        self.player2.setBombe()

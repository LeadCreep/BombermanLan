from datetime import time, timedelta, datetime
import pygame

from constantes import TILESISE
from bombes import Bombe


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.imageliste = [pygame.image.load(
            "assets/players/player1.png"), pygame.image.load(
            "assets/players/player2.png"), pygame.image.load("assets/players/deathState.png")]
        counter = 0
        for image in self.imageliste:
            self.imageliste[counter] = pygame.transform.scale(
                image, (64, 64))
            counter += 1
        self.image = self.imageliste[0]
        self.game = game
        self.rect = self.image.get_rect()
        self.range = 2  # Portée de la bombe
        self.x = x
        self.y = y
        self.game.players.add(self)
        self.deathState = False
        self.bombe = None
        self.bombeIsDecounting = False
        self.explosionAppening = False

    # Déplacer le joueur
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    # Tester la collision de la prochaine position : Retourne Vrai si la prochaine possition est la même que celle d'un mur/joueur/bombe
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.Unbreakable:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for wall in self.game.Breakable:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for bombe in self.game.bombes:
            if bombe.x == self.x + dx and bombe.y == self.y + dy:
                return True
        for player in self.game.players:
            if player.x == self.x + dx and player.y == self.y + dy:
                return True
        for trou in self.game.Trous:
            if trou.x == self.x + dx and trou.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE
        if self.deathState:
            self.image = self.imageliste[2]

    def setBombe(self):
        self.bombeIsDecounting = True
        self.bombe = Bombe(self, self.x, self.y)


# Classe des points d'apparition
class SpawnPoint(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/explosions/BLANK.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = y * TILESISE
        self.rect.x = x * TILESISE


class Icone(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.imageliste = [pygame.image.load(
            "assets/players/player1_icon.png"), pygame.image.load("assets/players/player2_icon.png")]
        self.image = self.imageliste[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

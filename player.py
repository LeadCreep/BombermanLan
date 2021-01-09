import pygame

from constantes import TILESISE
from bombes import Bombe


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.imageliste = [pygame.image.load(
            "assets/players/player1.png"), pygame.image.load(
            "assets/players/player2.png"), pygame.image.load("assets/players/deathState.png")]
        self.image = self.imageliste[0]
        self.game = game
        self.rect = self.image.get_rect()
        self.velocity = 1
        self.x = x
        self.y = y
        self.game.players.add(self)
        self.deathState = False
        self.bombe = None
        self.bombeIsDecounting = False
        self.explosionAppening = False

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

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
        return False

    def update(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE
        if self.deathState:
            self.image = self.imageliste[2]

    def SetBombe(self):
        self.bombeIsDecounting = True
        self.bombe = Bombe(self, self.x, self.y)


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

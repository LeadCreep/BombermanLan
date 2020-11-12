import pygame
import time
from bombes import Bombe
from constantes import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/players/player1.png")
        self.game = game
        self.rect = self.image.get_rect()
        self.velocity = 1
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls_groupe:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        for bombe in self.game.bombes:
            if bombe.x == self.x + dx and bombe.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE

import pygame

from constantes import TILESISE


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/wall.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = y * TILESISE
        self.rect.x = x * TILESISE
        self.game = game


class Breakable_Walls(Wall):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/player.png")

    def isDestroyed(self):
        for explosion in self.game.explosions:
            if explosion.x == self.x and explosion.y == self.y:
                self.game.Breakable.remove(self)

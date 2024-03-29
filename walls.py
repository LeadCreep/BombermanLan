import pygame

from constantes import TILESISE


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/walls/wall.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = y * TILESISE
        self.rect.x = x * TILESISE
        self.game = game


class Breakable_Walls(Wall):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/walls/Breakable_Wall.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

    def isDestroyed(self):  # Le Détruire si une explosion a la meme place
        for explosion in self.game.explosions:
            if explosion.x == self.x and explosion.y == self.y:
                self.game.Breakable.remove(self)


class Trou(Wall):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/walls/Trou.png")


class Trap(Wall):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/walls/pic.png")

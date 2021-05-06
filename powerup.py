import pygame

from constantes import TILESISE


class SpawnerPW(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/explosions/BLANK.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = y * TILESISE
        self.rect.x = x * TILESISE


class PowerUp(pygame.sprite.Sprite):  # Class de base des power ups
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/explosions/BLANK.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE


class PWLongRange(PowerUp):  # Augmente la porté de la bombe
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/PowerUp/LongRange.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

    def recup(self):
        for player in self.game.players:
            if self.x == player.x and self.y == player.y:
                self.game.powerUp.remove(self)
                player.range += 1

    def update(self):
        self.recup()


class Fire(PowerUp):  # Print Yes !
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load("assets/explosions/EXPLOSION1.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

    def recup(self):
        for player in self.game.players:
            if self.x == player.x and self.y == player.y:
                self.game.powerUp.remove(self)
                player.deathState = True

    def update(self):
        self.recup()

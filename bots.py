import pygame

from constantes import TILESISE


class Bot(pygame.sprite.Sprite):
    def __init__(self, game, x, y, NumeroPlayer):
        super().__init__()
        self.game = game
        self.game.bots.add(self)
        self.imageliste = [pygame.image.load(
            "assets/players/player1.png"), pygame.image.load("assets/players/deathState.png")]
        self.image = self.imageliste[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def place(self, x, y):
        self.rect.x = x * TILESISE
        self.rect.y = y * TILESISE

    def update(self):
        self.place(self.x, self.y)

    def setSkin(self, numJoueur):
        print(numJoueur)

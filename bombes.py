from datetime import datetime, timedelta

import pygame

from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TILESISE, TAILLE_DE_MAP


class Bombe(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.explosion = None
        self.game.bombes.add(self)
        self.imageliste = [pygame.image.load("assets/bombes/bomb1.png"), pygame.image.load("assets/bombes/bomb2.png"), pygame.image.load(
            "assets/bombes/bomb3.png"), pygame.image.load("assets/bombes/bomb4.png"), pygame.image.load("assets/bombes/bomb5.png")]
        self.image = self.imageliste[0]
        self.rect = self.image.get_rect()
        self.timeCreated = datetime.now()
        self.x = x
        self.y = y

    def mettreEnPlaceBombe(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE

    def update(self):
        self.explode_Bombe()
        if self.game.explosionAppening:
            self.explosion.update()

    def explode_Bombe(self):
        if timedelta(seconds=3) <= datetime.now() - self.timeCreated:
            self.explosion = Explosion(
                self.game, self.x, self.y, True, True, True, True)
            self.game.bombes.remove(self)
            self.game.explosionAppening = True
            self.game.bombeIsDecounting = False
        if timedelta(seconds=1) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[1]
        if timedelta(seconds=1.5) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[2]
        if timedelta(seconds=2) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[3]
        if timedelta(seconds=2.5) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[4]


class Explosion(pygame.sprite.Sprite):
    def __init__(self, game, x, y, up, left, right, down):
        super().__init__()
        self.game = game
        self.timeCreated = datetime.now()
        self.image = pygame.image.load("assets/explosions/EXPLOSION1.png")
        self.rect = self.image.get_rect()
        self.maxRange = 13
        self.range = 0
        self.x = x
        self.y = y
        self.mettreEnPlace()
        self.game.explosionAppening = True
        self.Propagation()

    def update(self):
        for explosion in self.ListeDesExplosions:
            explosion.update()

    def mettreEnPlace(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE

    def Propagation(self):
        self.ListeDesExplosions = []
        for longeurup in range(self.maxRange):
            self.ListeDesExplosions.append(ExplosionPlusLoin(
                self.game, self.x, self.y-longeurup))
        for longeurleft in range(self.maxRange):
            self.ListeDesExplosions.append(ExplosionPlusLoin(
                self.game, self.x-longeurleft, self.y))
        for longeurright in range(self.maxRange):
            self.ListeDesExplosions.append(ExplosionPlusLoin(
                self.game, self.x+longeurright, self.y))
        for longeurdown in range(self.maxRange):
            self.ListeDesExplosions.append(ExplosionPlusLoin(
                self.game, self.x, self.y+longeurdown))


class ExplosionPlusLoin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.imageliste = [pygame.image.load("assets/explosions/EXPLOSION1.png"), pygame.image.load("assets/explosions/EXPLOSION2.png"), pygame.image.load(
            "assets/explosions/EXPLOSION3.png"), pygame.image.load("assets/explosions/EXPLOSION4.png"), pygame.image.load("assets/explosions/EXPLOSION5.png"), pygame.image.load("assets/explosions/BLANK.png")]
        self.image = self.imageliste[0]
        self.rect = self.image.get_rect()
        self.game.explosions.add(self)
        self.timeCreated = datetime.now()
        self.x = x
        self.y = y
        self.inWall = True
        self.mettreEnPlace()
        for wall in self.game.walls_groupe:
            if wall.x == self.x and wall.y == self.y or self.y < OFFSET_HEIGHT or self.y > OFFSET_HEIGHT+TAILLE_DE_MAP-2 or self.x < OFFSET_WIDTH or self.x > OFFSET_WIDTH+TAILLE_DE_MAP-1:
                self.inWall = True
                break
            else:
                self.inWall = False

    def mettreEnPlace(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE

    def update(self):
        if not self.inWall:
            self.TempsDeVie()
        else:
            self.image = self.imageliste[5]
            self.game.explosions.remove(self)

    def TempsDeVie(self):
        if timedelta(seconds=0.2) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[1]
        if timedelta(seconds=0.5) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[2]
        if timedelta(seconds=0.7) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[3]
        if timedelta(seconds=1) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[4]
        if timedelta(seconds=1.2) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[5]
        if timedelta(seconds=1.21) <= datetime.now() - self.timeCreated:
            self.game.explosionAppening = False
            self.game.explosions.remove(self)
            self.game.explosions.empty()

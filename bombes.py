from datetime import datetime, timedelta

import pygame

from constantes import OFFSET_HEIGHT, OFFSET_WIDTH, TAILLE_DE_MAP, TILESISE


# Classe Bombe
class Bombe(pygame.sprite.Sprite):
    def __init__(self, player, x, y):
        super().__init__()
        self.player = player
        self.explosion = None
        self.player.game.bombes.add(self)
        self.imageliste = [pygame.image.load("assets/bombes/bomb1.png"), pygame.image.load("assets/bombes/bomb2.png"), pygame.image.load(
            "assets/bombes/bomb3.png"), pygame.image.load("assets/bombes/bomb4.png"), pygame.image.load("assets/bombes/bomb5.png")]
        counter = 0
        for image in self.imageliste:
            self.imageliste[counter] = pygame.transform.scale(
                image, (64, 64))
            counter += 1
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
        self.mettreEnPlaceBombe()
        if self.player.explosionAppening:
            self.explosion.update()

    # Annimation
    def explode_Bombe(self):
        if timedelta(seconds=1) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[1]
        if timedelta(seconds=1.5) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[2]
        if timedelta(seconds=2) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[3]
        if timedelta(seconds=2.5) <= datetime.now() - self.timeCreated:
            self.image = self.imageliste[4]
        if timedelta(seconds=3) <= datetime.now() - self.timeCreated:
            self.explosion = Explosion(
                self.player, self.x, self.y)
            self.player.game.bombes.remove(self)
            self.player.explosionAppening = True
            self.player.bombeIsDecounting = False


# Générateur de l'explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, player, x, y):
        super().__init__()
        self.player = player
        self.timeCreated = datetime.now()
        self.image = pygame.image.load("assets/explosions/EXPLOSION1.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.mettreEnPlace()
        self.player.explosionAppening = True
        self.Propagation()

    # Update de toutes les explosions
    def update(self):
        for explosion in self.ListeDesExplosions[0]:
            explosion.update()
        for explosion in self.ListeDesExplosions[1]:
            explosion.update()
        for explosion in self.ListeDesExplosions[2]:
            explosion.update()
        for explosion in self.ListeDesExplosions[3]:
            explosion.update()

    def mettreEnPlace(self):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE

    # Execution de la création des explosions
    def Propagation(self):
        self.ListeDesExplosions = [[], [], [], []]
        self.ExplodeLineUp()
        self.ExplodeLineDown()
        self.ExplodeLineLeft()
        self.ExplodeLineRight()

    # Creer Les Explosions sur les 2 axes
    def ExplodeLineUp(self):
        for longeurup in range(self.player.range):
            self.ListeDesExplosions[0].append(ExplosionPlusLoin(
                self.player, self.x, self.y - longeurup))
            for explosion in self.ListeDesExplosions[0]:
                for thing in self.player.game.Unbreakable:
                    if explosion.x == thing.x and explosion.y == thing.y:
                        return

    def ExplodeLineDown(self):
        for longeurdown in range(self.player.range):
            self.ListeDesExplosions[1].append(ExplosionPlusLoin(
                self.player, self.x, self.y + longeurdown))
            for explosion in self.ListeDesExplosions[1]:
                for thing in self.player.game.Unbreakable:
                    if explosion.x == thing.x and explosion.y == thing.y:
                        return

    def ExplodeLineLeft(self):
        for longeurleft in range(self.player.range):
            self.ListeDesExplosions[2].append(ExplosionPlusLoin(
                self.player, self.x-longeurleft, self.y))
            for explosion in self.ListeDesExplosions[2]:
                for thing in self.player.game.Unbreakable:
                    if explosion.x == thing.x and explosion.y == thing.y:
                        return

    def ExplodeLineRight(self):
        for longeurright in range(self.player.range):
            self.ListeDesExplosions[3].append(ExplosionPlusLoin(
                self.player, self.x+longeurright, self.y))
            for explosion in self.ListeDesExplosions[3]:
                for thing in self.player.game.Unbreakable:
                    if explosion.x == thing.x and explosion.y == thing.y:
                        return


# Image de l'explosion et son annimation
class ExplosionPlusLoin(pygame.sprite.Sprite):
    def __init__(self, player, x, y):
        super().__init__()
        self.player = player
        self.imageliste = [pygame.image.load("assets/explosions/EXPLOSION1.png"), pygame.image.load("assets/explosions/EXPLOSION2.png"), pygame.image.load(
            "assets/explosions/EXPLOSION3.png"), pygame.image.load("assets/explosions/EXPLOSION4.png"), pygame.image.load("assets/explosions/EXPLOSION5.png"), pygame.image.load("assets/explosions/BLANK.png")]
        counter = 0
        for image in self.imageliste:
            self.imageliste[counter] = pygame.transform.scale(
                image, (64, 64))
            counter += 1
        self.image = self.imageliste[0]
        self.rect = self.image.get_rect()
        self.player.game.explosions.add(self)
        self.timeCreated = datetime.now()
        self.x = x
        self.y = y
        self.inWall = False
        self.mettreEnPlace()
        for thing in self.player.game.Unbreakable:  # Si il est dans un mur ne pas le générer
            if thing.x == self.x and thing.y == self.y or self.y < OFFSET_HEIGHT or self.y > OFFSET_HEIGHT+TAILLE_DE_MAP-2 or self.x < OFFSET_WIDTH or self.x > OFFSET_WIDTH+TAILLE_DE_MAP-1:
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
            self.player.game.explosions.remove(self)

    # Annimation
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
            self.player.explosionAppening = False
            self.player.game.explosions.remove(self)
            self.player.game.explosions.empty()

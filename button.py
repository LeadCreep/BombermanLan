import pygame


class BUTTON(pygame.sprite.Sprite):
    def __init__(self, menu, x, y, i):
        super().__init__()
        self.menu = menu
        self.imagelist = [pygame.image.load("assets/buttons/play/play1.png"), pygame.image.load("assets/buttons/play/play2.png"),
                          pygame.image.load("assets/buttons/quit/KIT1.png"), pygame.image.load("assets/buttons/quit/KIT2.png")]
        self.image = self.imagelist[i + 0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.i = i
        menu.buttons.add(self)

    def onHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.imagelist[self.i+1]
        else:
            self.image = self.imagelist[self.i+0]

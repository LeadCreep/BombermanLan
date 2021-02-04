import pygame


class BUTTON(pygame.sprite.Sprite):
    def __init__(self, menu, x, y):
        super().__init__()
        self.menu = menu
        self.image = pygame.image.load("assets/buttons/play/play1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        menu.buttons.add(self)

    def onHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = pygame.image.load("assets/buttons/play/play2.png")
        else:
            self.image = pygame.image.load("assets/buttons/play/play1.png")

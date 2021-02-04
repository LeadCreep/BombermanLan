from button import BUTTON
import pygame
from pygame.constants import K_SPACE, MOUSEBUTTONDOWN


class Menu:
    def __init__(self):
        self.onMenu = True
        self.background = pygame.image.load("assets/backgrounds/menu.png")
        self.buttons = pygame.sprite.Group()
        self.bouton_start = BUTTON(self, 50, 50)
        #self.bouton_quit = BUTTON(self, 500, 50)

    def startgame(self):
        self.onMenu = False

    def update(self):
        self.event()
        for button in self.buttons:
            button.onHover()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    self.startgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bouton_start.rect.collidepoint(pygame.mouse.get_pos()):
                    self.startgame()
                # if self.bouton_quit.rect.collidepoint(pygame.mouse.get_pos()):
                    # pygame.quit()

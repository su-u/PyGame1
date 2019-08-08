import pygame
from pygame.locals import *


class Enemy(pygame.sprite.Sprite):
    """自機"""
    speed = 1
    display = Rect(0, 0, 1280, 720)

    def __init__(self, _display):
        # self.display = _display
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.display.bottom

    def update(self):
        pass

    def display_set(self, _display):
        self.display = _display

    def judge(self, octo_cat):
        pass

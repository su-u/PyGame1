import pygame
from pygame.locals import *
import sys

import bullet


class Player(pygame.sprite.Sprite):
    """自機""" 
    speed = 8
    display = Rect(0, 0, 1280, 720)

    def __init__(self, _display):
        # self.display = _display
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.display.bottom

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        self.rect.clamp_ip(self.display)

        if pressed_keys[K_SPACE]:
            bullet.Bullet((self.rect.right, self.rect.centery), self.display)

    def display_set(self, _display):
        self.display = _display

import pygame
from pygame.locals import *
import os
import sys

class Bullet(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, pos):
       pygame.sprite.Sprite.__init__(self, self.containers)
       self.image = pygame.image.load("data/ball.png").convert()
       self.rect = self.image.get_rect()
       self.rect.center = pos

    def update(self):
        # 上に飛んでいき、画面外に出たら消滅
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.kill()
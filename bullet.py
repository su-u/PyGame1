import pygame
from pygame.locals import *
import os
import sys

class Bullet(pygame.sprite.Sprite):
    speed = 5
    display = Rect(0, 0, 0, 0)

    def __init__(self, pos, dis):
       pygame.sprite.Sprite.__init__(self, self.containers)
       self.image = pygame.image.load("data/ball.png").convert()
       self.rect = self.image.get_rect()
       self.rect.center = pos
       self.display = dis;

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > self.display.right:
            self.kill()


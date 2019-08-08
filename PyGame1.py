import pygame;
from pygame.locals import *
import os
import sys
from PyGameDisplay import DisplaySize, Aspect
import Player
import bullet

import FileManager


def main():
    pygame.init()
    display = DisplaySize.DisplaySize(1280, 720, Aspect.AspectEnum.A16_9)
    screen = pygame.display.set_mode(display.get_display_size())
    pygame.display.set_caption(u"Game")

    all = pygame.sprite.RenderUpdates()
    Player.Player.containers = all
    Player.Player.image = FileManager.FileManager.load_image("player.png", 150, 150)
    player = Player.Player(display.get_display_rect)

    bullet.Bullet.containers = all

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

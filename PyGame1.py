import pygame
from pygame.locals import *
import sys
from PyGameDisplay import DisplaySize, Aspect

def main():
    dis = DisplaySize.DisplaySizeClass(1920, 1080, Aspect.AspectEnum.A16_9)
    pygame.init() # 初期化
    screen = pygame.display.set_mode(dis.get_display_size()) # ウィンドウサイズの指定
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定

    while(True):
        screen.fill((255,63,10,)) # 背景色の指定。RGBだと思う  
        pygame.draw.rect(screen, (255,255,0), Rect(10,10,20,50))
        pygame.display.update() # 画面更新

        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
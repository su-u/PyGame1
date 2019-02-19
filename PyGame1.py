import pygame;
from pygame.locals import *
import os
import sys
from PyGameDisplay import DisplaySize, Aspect
import Player
import bullet
import traceback

SCR_RECT = Rect(0, 0, 640, 480)

def main():
    #dis = DisplaySize.DisplaySize(1920, 1080, Aspect.AspectEnum.A16_9)
    #pygame.init() # 初期化
    #screen = pygame.display.set_mode(dis.get_display_size()) # ウィンドウサイズの指定
    #pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
    pygame.init();
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"Game")

    # スプライトグループを作成して登録
    all = pygame.sprite.RenderUpdates()
    Player.Player.containers = all
    # スプライトの画像を登録
    Player.Player.image = load_image("player.png")
    # 自機を作成
    plyaer = Player.Player()
    
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

def load_image(filename, colorkey=None):
    """画像をロードして画像と矩形を返す"""
    filename = os.path.join("data", filename)
    try:
        image = pygame.image.load(filename)
    except (pygame.error, message):
        print("Cannot load image:"), filename
        traceback.print_exc()
        raise (SystemExit, message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


if __name__ == "__main__":
    main()
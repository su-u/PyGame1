import pygame
from pygame.locals import *
import sys
import os

class FileManager(object):
    """ファイル処理関係"""

    @staticmethod
    def load_image(filename, width = None,height = None):
        """画像をロードして画像と矩形を返す"""
        filename = os.path.join("data", filename)
        try:
            image = pygame.image.load(filename)
        except (pygame.error, message):
            print("Cannot load image:"), filename
            traceback.print_exc()
            raise (SystemExit, message)
        image = image.convert()
        #if colorkey is not None:
        #    if colorkey is -1:
        #        colorkey = image.get_at((0,0))
        #    image.set_colorkey(colorkey, RLEACCEL)

        if width is None:
            return image
        else:
            return pygame.transform.scale(image,(width,height))

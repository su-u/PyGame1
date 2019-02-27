from . import Aspect
import pygame;
from pygame.locals import *
import os
import sys

class DisplaySize(object):
    """description of class"""

    __base_size = Rect(0, 0, 0, 0)
    __diplay_size = Rect(0, 0, 0, 0)
    
    __aspect = 0

    __player_size = Rect(0,0,0,0)

    def __init__(self, size_x, size_y, asp):
       self.__diplay_size.width = size_x
       self.__diplay_size.height = size_y
       self.__base_size.width, self.__base_size.height = Aspect.AspectEnum.MaxDisplaySize(asp)

    def get_width(self):
        return self.__diplay_size.width

    def get_height(self):
        return self.__diplay_size.height

    def get_display_size(self):
        return (self.__diplay_size.width, self.__diplay_size.height)

    def get_display_rect(self):
        print(self.__display_size)
        return __diplay_size
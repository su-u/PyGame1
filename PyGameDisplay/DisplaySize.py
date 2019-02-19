from . import Aspect
import pygame;
from pygame.locals import *
import os
import sys

class DisplaySize(object):

    PLAYER_SIZE = (50,50)

    """description of class"""
    __base_size = Rect(0, 0, 0, 0)
    __diplay_size = Rect(0, 0, 0, 0)
    
    __aspect = 0

    __player_size = Rect(0,0,0,0)

    def __init__(self, size_x, size_y, asp):
       self.__diplay_size_x = size_x
       self.__diplay_size_y = size_y
       self.__base_size_x, self._w_base_size_y = Aspect.AspectEnum.MaxDisplaySize(asp)

    def get_x(self):
        return self.__diplay_size_x

    def get_y(self):
        return self.__diplay_size_y

    def get_display_size(self):
        return (self.__diplay_size_x, self.__diplay_size_y)

    

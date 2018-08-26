from . import Aspect
class DisplaySizeClass(object):
    """description of class"""
    __base_size_x = 0
    __base_size_y = 0
    __diplay_size_x = 0
    __diplay_size_y = 0
    __aspect = 0

    def __init__(self, size_x, size_y, asp):
       self.__diplay_size_x = size_x
       self.__diplay_size_y = size_y
       self.__base_size_x, self.__base_size_y = Aspect.Aspect.MaxDisplaySize(asp)

    def get_x(self):
        return self.__diplay_size_x

    def get_y(self):
        return self.__diplay_size_y

    def get_display_size(self):
        return (self.__diplay_size_x, self.__diplay_size_y)



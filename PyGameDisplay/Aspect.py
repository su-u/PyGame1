from enum import IntEnum, auto

class AspectEnum(IntEnum):
    """description of class"""
    A4_3  = 1
    A16_9 = 2
    A19_10 = 3

    @staticmethod
    def MaxDisplaySize(asp):
        if asp == 1:
            return (1440, 1080)
        elif asp == 2:
            return (1920, 1080)
        elif asp == 3:
            return (1920, 1200)
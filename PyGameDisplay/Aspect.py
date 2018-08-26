from enum import IntEnum, auto

class AspectEnum(IntEnum):
    """description of class"""
    A4_3  = auto()
    A16_9 = auto()
    A19_10 = auto()

    def MaxDisplaySize(self, asp):
        if asp == A4_3:
            return (1440, 1080)
        elif asp == A16_9:
            return (1920, 1080)
        elif asp == A19_10:
            return (1920, 1200)
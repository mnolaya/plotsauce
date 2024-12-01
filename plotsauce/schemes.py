import enum
import itertools

class BrightScheme(enum.Enum):
    BLUE = '#447788'
    CYAN = '#66CCEE'
    GREEN = '#228833'
    YELLOW = '#CCBB44'
    RED = '#EE6677'
    PURPLE = '#AA3377'
    GREY = '#BBBBBB'

class HighContrastScheme(enum.Enum):
    WHITE = '#FFFFFF'
    YELLOW = '#DDAA33'
    RED = '#BB5566'
    BLUE = '#004488'
    BLACK = '#000000'

class VibrantScheme(enum.Enum):
    BLUE = '#0077BB'
    CYAN = '#33BBEE'
    TEAL = '#009988'
    ORANGE = '#EE7733'
    RED = '#CC3311'
    MAGENTA = '#EE3377'
    GREY = '#BBBBBB'

def cycle_scheme(color_scheme: enum.Enum) -> itertools.cycle:
    '''
    Create a itertools.cycle object for a color scheme.
    '''
    return itertools.cycle([color.value for color in color_scheme])

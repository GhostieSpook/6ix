
import colorsys
import discord
import random

class Colour:

    __slots__ = ('value',)

    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int parameter, received %s instead.' % value.__class__.__name__)

        self.value = value

    def _get_byte(self, byte):
        return (self.value >> (8 * byte)) & 0xff

    def __eq__(self, other):
        return isinstance(other, Colour) and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '#{:0>6x}'.format(self.value)

    def __repr__(self):
        return '<Colour value=%s>' % self.value

    def __hash__(self):
        return hash(self.value)

    @property
    def r(self):
        return self._get_byte(2)

    @property
    def g(self):
        return self._get_byte(1)

    @property
    def b(self):
        return self._get_byte(0)

    def to_rgb(self):
        return (self.r, self.g, self.b)

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls((r << 16) + (g << 8) + b)

    @classmethod
    def from_hsv(cls, h, s, v):
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return cls.from_rgb(*(int(x * 255) for x in rgb))

    @classmethod
    def default(cls):
        return cls(0)

    @classmethod
    def teal(cls):
        return cls(0x1abc9c)

    @classmethod
    def dark_teal(cls):
        return cls(0x11806a)

    @classmethod
    def green(cls):
        return cls(0x2ecc71)

    @classmethod
    def dark_green(cls):
        return cls(0x1f8b4c)

    @classmethod
    def blue(cls):
        return cls(0x3498db)

    @classmethod
    def dark_blue(cls):
        return cls(0x206694)

    @classmethod
    def purple(cls):
        return cls(0x9b59b6)

    @classmethod
    def dark_purple(cls):
        return cls(0x71368a)

    @classmethod
    def magenta(cls):
        return cls(0xe91e63)

    @classmethod
    def dark_magenta(cls):
        return cls(0xad1457)

    @classmethod
    def gold(cls):
        return cls(0xf1c40f)

    @classmethod
    def dark_gold(cls):
        return cls(0xc27c0e)

    @classmethod
    def orange(cls):
        return cls(0xe67e22)

    @classmethod
    def dark_orange(cls):
        return cls(0xa84300)

    @classmethod
    def red(cls):
        return cls(0xe74c3c)

    @classmethod
    def dark_red(cls):
        return cls(0x992d22)

    @classmethod
    def lighter_grey(cls):
        return cls(0x95a5a6)

    @classmethod
    def dark_grey(cls):
        return cls(0x607d8b)

    @classmethod
    def light_grey(cls):
        return cls(0x979c9f)

    @classmethod
    def darker_grey(cls):
        return cls(0x546e7a)

    @classmethod
    def blurple(cls):
        return cls(0x7289da)
    @classmethod
    def greyple(cls):      
        return cls(0x99aab5)
    @classmethod
    def black(cls):       
        return cls(0x000000)
    @classmethod
    def pink(cls):        
        return cls(0xFF69B4)  
    @classmethod
    def rand(cls):
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        return randcolor  
Color = Colour

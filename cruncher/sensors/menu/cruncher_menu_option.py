from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


class CruncherMenuOption:
    def __init__(self, name, label, action, options=()):
        self.__font = ImageFont.truetype(fonts.BitbuntuFull, 10)

        self.name = name
        self.label = label
        self.action = action
        self.options = options
        self.size = self.__font.getsize(name)
        self.width, self.height = self.size

    def trigger(self):
        if(self.action != None):
            self.action(*self.options)

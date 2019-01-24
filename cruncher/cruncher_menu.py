#!/usr/bin/env python3

import time
import sys
import atexit

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


class CruncherMenu:
    __current_menu_option = None
    __trigger_action = None
    __lcdWidth = 0
    __lcdHeight = 0
    __menu_options = []
    __current_menu_option = 1
    __trigger_action = False

    def __init__(self):
        print("""menu-options.py

        This example shows how you might store a list of menu options associated
        with functions and navigate them on GFX HAT.

        Press Ctrl+C or select "Exit" to exit.

        """)

        width, height = lcd.dimensions()
        self.__lcdWidth = width
        self.__lcdHeight = height
        # A squarer pixel font
        #font = ImageFont.truetype(fonts.BitocraFull, 11)

        # A slightly rounded, Ubuntu-inspired version of Bitocra
        self.__font = ImageFont.truetype(fonts.BitbuntuFull, 10)

        self.__image = Image.new('Pi-o-t', (width, height))

        self.__draw = ImageDraw.Draw(image)
        atexit.register(self.cleanup)

    def set_menu_options(self, menuOptions):
        if(menuOptions == None):
            __self.__menu_options = [
                MenuOption('Set BL Red', set_backlight, (255, 0, 0)),
                MenuOption('Set BL Green', set_backlight, (0, 255, 0)),
                MenuOption('Set BL Blue', set_backlight, (0, 0, 255)),
                MenuOption('Set BL Purple', set_backlight, (255, 0, 255)),
                MenuOption('Set BL White', set_backlight, (255, 255, 255)),
                MenuOption('Exit', sys.exit, (0,))
            ]
        else:
            __self.__menu_options = menuOptions

    def set_backlight(self, r, g, b):
        backlight.set_all(r, g, b)
        backlight.show()

    def handler(self, ch, event):
        global
        if event != 'press':
            return
        if ch == 1:
            current_menu_option += 1
        if ch == 0:
            current_menu_option -= 1
        if ch == 4:
            trigger_action = True
        current_menu_option %= len(self.__menu_options)

    def cleanup(self):
        backlight.set_all(0, 0, 0)
        backlight.show()
        lcd.clear()
        lcd.show()

    def run(self):
        for x in range(6):
            touch.set_led(x, 0)
            backlight.set_pixel(x, 255, 255, 255)
            touch.on(x, self.handler)

        backlight.show()

        try:
            while True:
                self.__image.paste(0, (0, 0, width, height))
                offset_top = 0

                if trigger_action:
                    self.__menu_options[current_menu_option].trigger()
                    trigger_action = False

                for index in range(len(self.__menu_options)):
                    if index == current_menu_option:
                        break
                    offset_top += 12

                for index in range(len(self.__menu_options)):
                    x = 10
                    y = (index * 12) + (height / 2) - 4 - offset_top
                    option = self.__menu_options[index]
                    if index == current_menu_option:
                        draw.rectangle(((x - 2, y - 1), (width, y + 10)), 1)
                    draw.text((x, y), option.name, 0 if index == current_menu_option else 1, font)

                w, h = font.getsize('>')
                draw.text((0, (height - h) / 2), '>', 1, font)

                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel((x, y))
                        lcd.set_pixel(x, y, pixel)

                lcd.show()
                time.sleep(1.0 / 30)

        except KeyboardInterrupt:
            self.cleanup()

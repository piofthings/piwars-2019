#!/usr/bin/env python3

import time
import sys
import atexit

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw
from cruncher_menu_option import CruncherMenuOption

class CruncherMenu:
    __current_menu_option = None
    #__trigger_action = None
    __lcdWidth = 0
    __lcdHeight = 0
    __menu_options = []
    __home_options = None

    __calibration_options = None

    __current_menu_option = 1
    __trigger_action = False

    __looper = False
    def __init__(self):
        print("""
        Press Ctrl+C or select "Exit" to exit.
        """)

        self.init_home_menu()
        self.init_calibration_menu()

        width, height = lcd.dimensions()
        self.__lcdWidth = width
        self.__lcdHeight = height
        # A squarer pixel font
        #font = ImageFont.truetype(fonts.BitocraFull, 11)

        # A slightly rounded, Ubuntu-inspired version of Bitocra
        self.__font = ImageFont.truetype(fonts.BitbuntuFull, 10)

        self.__image = Image.new('P', (width, height))

        self.__draw = ImageDraw.Draw(self.__image)
        atexit.register(self.cleanup)

    def init_home_menu(self):
        self.__home_options = [
            CruncherMenuOption('J2 Controller', None),
            CruncherMenuOption('Servo Calibration', self.show_wheels_calibration),
            CruncherMenuOption('Exit', sys.exit, (0,))
        ]

    def init_calibration_menu(self):
        self.__calibration_options = [
            CruncherMenuOption("Calibration Menu", None),
            CruncherMenuOption("Configure servo indexes", None),
            CruncherMenuOption("Front left Wheel", None),
            CruncherMenuOption("Front right Wheel", None),
            CruncherMenuOption("Rear left Wheel", None),
            CruncherMenuOption("Rear right Wheel", None),
            CruncherMenuOption("Save current status", None),
            CruncherMenuOption("Reload servo defaults", None),
            CruncherMenuOption("Set Actuation Angle", None),
            CruncherMenuOption("Back", self.set_menu_options)
        ]


    def set_menu_options(self, menuOptions=None):
        if(menuOptions == None):
            self.__menu_options = self.__home_options
        else:
            self.__menu_options = menuOptions

    def show_wheels_calibration(self):
        self.set_menu_options(self.__calibration_options)
        #self.paint_screen()



    def set_backlight(self, r, g, b):
        backlight.set_all(r, g, b)
        backlight.show()

    def handler(self, ch, event):
        #global
        if event != 'press':
            return
        if ch == 1:
            self.__current_menu_option += 1
        if ch == 0:
            self.__current_menu_option -= 1
        if ch == 4:
            self.__trigger_action = True
        self.__current_menu_option %= len(self.__menu_options)

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
        self.set_menu_options()
        self.paint_screen()

    def paint_screen(self):
        try:
            while True:
                self.__image.paste(0, (0, 0, self.__lcdWidth, self.__lcdHeight))
                offset_top = 0

                if self.__trigger_action:
                    self.__menu_options[self.__current_menu_option].trigger()
                    self.__trigger_action = False

                for index in range(len(self.__menu_options)):
                    if index == self.__current_menu_option:
                        break
                    offset_top += 12

                for index in range(len(self.__menu_options)):
                    x = 10
                    y = (index * 12) + (self.__lcdHeight / 2) - 4 - offset_top
                    option = self.__menu_options[index]
                    if index == self.__current_menu_option:
                        self.__draw.rectangle(((x - 2, y - 1), (self.__lcdWidth, y + 10)), 1)
                    self.__draw.text((x, y), option.name, 0 if index == self.__current_menu_option else 1, self.__font)

                w, h = self.__font.getsize('>')
                self.__draw.text((0, (self.__lcdHeight - h) / 2), '>', 1, self.__font)

                for x in range(self.__lcdWidth):
                    for y in range(self.__lcdHeight):
                        pixel = self.__image.getpixel((x, y))
                        lcd.set_pixel(x, y, pixel)

                lcd.show()
                time.sleep(1.0 / 30)

        except KeyboardInterrupt:
            self.cleanup()

menu = CruncherMenu()
menu.run()

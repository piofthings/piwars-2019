#!/usr/bin/env python3
import os
import sys
import time
import atexit

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "services")))
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "commands")))

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw
from cruncher_menu_option import CruncherMenuOption
from pi_noon_command import PiNoonCommand


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

        self.init_menus()

        width, height = lcd.dimensions()
        self.__lcdWidth = width
        self.__lcdHeight = height
        # A squarer pixel font
        self.__font = ImageFont.truetype(fonts.BitocraFull, 11)

        # A slightly rounded, Ubuntu-inspired version of Bitocra
        #self.__font = ImageFont.truetype(fonts.BitbuntuFull, 10)

        self.__image = Image.new('P', (width, height))

        self.__draw = ImageDraw.Draw(self.__image)
        atexit.register(self.cleanup)

    def init_menus(self):
        self.__home_options = [
            CruncherMenuOption('home_title', 'J2 Controller', None),
            CruncherMenuOption('home_servo_calibration', 'Servo Calibration', self.show_wheels_calibration_menu),
            CruncherMenuOption('home_servo_events', 'Events', self.show_events_menu),
            CruncherMenuOption('home_exit', 'Exit', sys.exit, (0,))
        ]
        self.__calibration_options = [
            CruncherMenuOption("sc_title", "Servo Calibration", None),
            CruncherMenuOption("sc_servo_indexs", "Servo indexes", self.show_servo_index_menu),
            CruncherMenuOption("sc_servo_zero", "Servo Zero positions", self.show_zero_position_menu),
            CruncherMenuOption("sc_save_current_status", "Save current status", None),
            CruncherMenuOption("sc_set_actuation_angle", "Set Actuation Angle", None),
            CruncherMenuOption("sc_reload_servo_defaults", "Reload servo defaults", None),
            CruncherMenuOption("sc_back", "Back", self.set_menu_options)
        ]
        self.__servo_index_options = [
            CruncherMenuOption("wi_fl_wheel_index", "FL Wheel Index", None),
            CruncherMenuOption("wi_fr_wheel_index", "FR Wheel Index", None),
            CruncherMenuOption("wi_rl_wheel_index", "RL Wheel Index", None),
            CruncherMenuOption("wi_rr_wheel_index", "RR Wheel Index", None),
            CruncherMenuOption("wi_fs_index", "FS Index", None),
            CruncherMenuOption("wi_rs_index", "RS Index", None),
            CruncherMenuOption("wi_back", "Back", self.show_wheels_calibration_menu),

        ]
        self.__servo_zero_position_options = [
            CruncherMenuOption("wc_flw", "Front left Wheel", None),
            CruncherMenuOption("wc_frw", "Front Right Wheel", None),
            CruncherMenuOption("wc_rlw", "Rear left Wheel", None),
            CruncherMenuOption("wc_rrw", "Rear right Wheel", None),
            CruncherMenuOption("wc_fs", "Front Suspension", None),
            CruncherMenuOption("wc_rs", "Rear Suspension", None),
            CruncherMenuOption("wc_back", "Back", self.show_wheels_calibration_menu),
        ]

        self.__events_menu_options = [
            CruncherMenuOption("ev_title", "Events", None),
            CruncherMenuOption("ev_space_invaders", "R:Space Invaders", None),
            CruncherMenuOption("ev_pi_noon", "R:Pi Noon", self.invoke_pi_noon_command),
            CruncherMenuOption("ev_spirit", "R:Spirit of Curiosity", None),
            CruncherMenuOption("ev_obstacles", "R:Apollo 13 Obstacles", None),
            CruncherMenuOption("ev_blastoff", "A:Blast off", None),
            CruncherMenuOption("ev_hubble", "A:Hubble", None),
            CruncherMenuOption("ev_canyon", "A:Canyon", None),
            CruncherMenuOption("ev_back", "Back", self.set_menu_options)
        ]

    def set_menu_options(self, menuOptions=None):
        if(menuOptions == None):
            self.__menu_options = self.__home_options
        else:
            self.__menu_options = menuOptions

    def show_wheels_calibration_menu(self):
        self.set_menu_options(self.__calibration_options)
        # self.paint_screen()

    def show_servo_index_menu(self):
        self.set_menu_options(self.__servo_index_options)

    def show_zero_position_menu(self):
        self.set_menu_options(self.__servo_zero_position_options)

    def set_backlight(self, r, g, b):
        backlight.set_all(r, g, b)
        backlight.show()

    def handler(self, ch, event):
        # global
        if event != 'press':
            return
        if ch == 1:
            self.__current_menu_option += 1
        if ch == 0:
            self.__current_menu_option -= 1
        if ch == 4:
            self.__trigger_action = True
        self.__current_menu_option %= len(self.__menu_options)

    def invoke_pi_noon_command(self):

    def cleanup(self):
        backlight.set_all(0, 0, 0)
        backlight.show()
        lcd.clear()
        lcd.show()

    def init_screen():
        for x in range(6):
            touch.set_led(x, 0)
            backlight.set_pixel(x, 255, 255, 255)
            touch.on(x, self.handler)

    def run(self):
        self.init_screen()

        backlight.show()
        self.set_menu_options()
        self.__looper = True
        while self.__looper:
            self.paint_screen()
            time.sleep(1.0 / 30)

    def paint_screen(self):
        try:
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

        except KeyboardInterrupt:
            self.__looper = False
            self.cleanup()


menu = CruncherMenu()
menu.run()

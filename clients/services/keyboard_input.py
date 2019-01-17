import sys
import os
import tty
import termios


class KeyboardInput:
    def __init__(self, args):
        print(args)
        pass

    def clear(self):
        '''
        Clears the terminal screen and scroll back to present
        the user with a nice clean, new screen. Useful for managing
        menu screens in terminal applications.
        '''
        os.system('cls||echo -e \\\\033c')
    #======================================================================
    # Reading single character by forcing stdin to raw mode

    def readchar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '0x03':
            raise KeyboardInterrupt
        return ch

    def readkey(self, getchar_fn=None):
        getchar = getchar_fn or self.readchar
        c1 = getchar()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1
        c3 = getchar()
        # 16=Up, 17=Down, 18=Right, 19=Left arrows
        return chr(0x10 + ord(c3) - 65)

    # End of single character reading
    #======================================================================

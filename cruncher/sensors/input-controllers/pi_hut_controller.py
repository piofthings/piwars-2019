"""Constants for ThePiHut controller"""


class PiHutController():

    #Axis
    L_JS_LEFT_RIGHT = 0 #-32767 Left most 32767 Right most
    L_JS_UP_DOWN = 1 #-32767 Upper most 32767 Lower most

    R_JS_LEFT_RIGHT = 2 #-32767 Left most 32767 Right most
    R_JS_UP_DOWN = 3 #-32767 Upper most 32767 Lower most

    """
    Button Right DPAD (the 4 buttons on the right)
    """
    BUTTON_R_DP_LEFT = 3
    BUTTON_R_DP_BOTTOM = 0
    BUTTON_R_DP_RIGHT = 1
    BUTTON_R_DP_TOP = 4

    """
    Button LEFT DPAD (the 4 buttons on the left)
    """

    """
    Values -32767 or 0
    """
    BUTTON_L_DP_LEFT = 6
    """
    Values 32767 or 0
    """
    BUTTON_L_DP_BOTTOM = 7
    """
    Values 32767 or 0
    """
    BUTTON_L_DP_RIGHT = 6
    """
    Values -32767 or 0
    """
    BUTTON_L_DP_TOP = 7

    """Home Button

    Values 0 or 1
    Button No: 12
    """
    BUTTON_HOME = 12

    """ Select Button

    Values 0 or 1
    Button No: 10
    """
    BUTTON_SELECT = 10

    """ Play button

    Values 0 or 1
    Button No: 9
    """
    #BUTTON_PLAY = 9

    """ L2 (Left Trigger)

    Values 0 or 1
    """
    LEFT_TRIGGER = 8

    """ R2 (Right Trigger)

    Values 0 or 1
    """
    RIGHT_TRIGGER = 9

    LEFT_BUMPER = 6

    RIGHT_BUMPER = 7

    START = 11

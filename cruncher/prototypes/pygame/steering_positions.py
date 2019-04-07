class SteeringPositions:
    """Steering Position constants"""

    NEUTRAL = 0
    SPOT_TURN = 1
    STRAFE_LEFT = 2
    STRAFE_RIGHT = 3

    AIM_LASER = 4
    FIRE_CANNON = 5
    TURN_OFF_SAFETY = 6

    INCREASE_FRONT_HEIGHT = 7
    DECREASE_FRONT_HEIGHT = 8
    INCREASE_REAR_HEIGHT = 9
    DECREASE_REAR_HEIGHT = 10
    SUSPENSION_RESET = 11
    #[FRONT_LEFT, FRONT_RIGHT, REAR_LEFT, REAR_RIGHT]
    defaults = None

    def __init__(self):
        self.defaults = [[0 for x in range(4)] for y in range(4)]

        self.defaults[0][0] = 105
        self.defaults[0][1] = 73.4
        self.defaults[0][2] = 143
        self.defaults[0][3] = 112

        self.defaults[1][0] = 161
        self.defaults[1][1] = 21
        self.defaults[1][2] = 75
        self.defaults[1][3] = 168

        self.defaults[2][0] = 50
        self.defaults[2][1] = 21
        self.defaults[2][2] = 75
        self.defaults[2][3] = 66

        self.defaults[3][0] = 150
        self.defaults[3][1] = 111
        self.defaults[3][2] = 168
        self.defaults[3][3] = 75

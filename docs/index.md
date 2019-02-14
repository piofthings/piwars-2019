## PiWars 2019 ~~Architecture~~ ~~Design~~ Braindump

Team Pi-o-steer's robot **LiS-J2** features two RaspberryPis, one Pi 3A+ and one Zero W. The Pi 3A+ is referred to as the ```Cruncher```, and the Zero W is the ``` Controller```

### Bot-Hub
BotHub is the NodeJS application that hosts the MQTT Server using Mosca. It will be running on the ```Cruncher``` (the Raspberry Pi 3A+).

~~The idea is to fully utilise the four cores of a RaspberryPi 3A+, we run various subsystems independently without getting low down to threads and app domains and such. MQTT will be the message bus for the various subsystems. MQTT is using Redis backplane hosted on the Pi itself and by last estimates it could do about 20K+ IOps. I can't really guess if that is enough, seems like a good start.
If the MQTT bus turns out inadequate, we will have to go back to Single-Threaded, run loop.~~

### J2 Cruncher
Cruncher has the following Hardware attachments
- ToF sensor array
- PiCamera
- 9DoF Sensor  
Combination of these sensor inputs will give it the ability to sense the Robots position and send out instructions to the ```J2 Controller``` about going left, right, faster, slower, forward and reverse.
- Joystick Controller
- GFX HAT as the main User Interface


I can't think of if the Cruncher or the Controller will trigger our Laser guided Meteor Cannon.


1. Start Joystick controller service
2. Start ToF Sensor service
3. Start BNO055 sensor service
4. Start GFX Hat service
5. Show Menu on GFX HAT and wait for response
    - Loop 60 times per second
        - If Mode = Calibrate Servos
            - Show Calibration Menu and wait in same event loop  
                1. c: Configure wheel indexes (On Adafruit PWM Board)
                2. w: Front left Wheel
                3. e: Front right Wheel
                4. s: Rear left Wheel
                5. d: Rear right Wheel
                6. r: Save current status
                7. t: Reset all to \*\_start angle in steering_status.json
                8. a: Set Steering servos Actuation Angle
                9. q: Back
        - If Mode = Event
            - Show Event Menu and continue in same run loop
            - If Event = Straight line speed, show Straight line speed Menu and wait in same run loop
                - If Menu = Start Go to 7
                - If Menu = Back go back to showing All Top level Menu items
            - If Event = Maze show Maze Menu and wait in same run loop
                - If Menu = Start Go to 8
                - If Menu = Back, go back to showing All Top level Menu items
            - If Event = Pi Noon show Pi Noon menu and wait in same run Loop
                - If Menu = Start Go to 9
                - If Menu = Back, go back to showing All Top level Menu items


6. Loop 1/100 times per second

    - Read Joystick, send it off to BluetoothClient
    - Read ToF 1, 2, 3, 4 in sequence and pass it on to BluetoothClient
    - Read BNO055 sensor service

7. Straight line speed
    -
8. Maze (Canyon of Mars)
    -
9. Pi Noon
    -

### J2 Controller

The Controller has the following Hardware attachments
- PiconZero Controller for Servo control of 6 Servos
- Cytron Motor Controller for the drive motors.
- Some kind of LED driver, we need bright LEDs as headlamps (might use PiconZero itself)
- It will need the PicoHacker HAT extension to allow access to all the pins required after the PiconZero has been plugged in.

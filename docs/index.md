## PiWars 2019 ~~Architecture~~ ~~Design~~ Braindump

Team Pi-o-steer's robot **LiS-J2** features two RaspberryPis, one Pi 3B+ and one Zero W. The Pi 3B+ is referred to as the ```Cruncher```, and the Zero W is the ``` Controller```

### Bot-Hub
BotHub is the NodeJS application that hosts the MQTT Server using Mosca. It will be running on the ```Cruncher``` (the Raspberry Pi 3A+).

The idea is to fully utilise the four cores of a RaspberryPi 3B+, we run various subsystems independently without getting low down to threads and app domains and such. MQTT will be the message bus for the various subsystems. MQTT is using Redis backplane hosted on the Pi itself and by last estimates it could do about 20K+ IOps. I can't really guess if that is enough, seems like a good start.

If the MQTT bus turns out inadequate, we will have to go back to Single-Threaded, run loop.

### J2 Cruncher
Cruncher has the following Hardware attachments
- ToF sensor array
- PiCamera
- 9DoF Sensor  
Combination of these sensor inputs will give it the ability to sense the Robots position and send out instructions to the ```J2 Controller``` about going left, right, faster, slower, forward and reverse.

I can't think of if the Cruncher or the Controller will trigger our Laser guided Meteor Cannon.

### J2 Controller

The Controller has the following Hardware attachments
- PiconZero Controller for Servo control of 6 Servos
- Cytron Motor Controller for the drive motors.
- Some kind of LED driver, we need bright LEDs as headlamps (might use PiconZero itself)
- It will need the PicoHacker HAT extension to allow access to all the pins required after the PiconZero has been plugged in.

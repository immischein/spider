from adafruit_servokit import ServoKit
from time import sleep

# Initialize the ServoKit object
kit = ServoKit(channels=16)
list_angles = [0,90,180]
while True:
    for deg in list_angles:
        kit.servo[0].angle = deg
        kit.servo[1].angle = deg
        kit.servo[2].angle = deg
        kit.servo[3].angle = deg
        kit.servo[4].angle = deg
        kit.servo[5].angle = deg
        sleep(.5)
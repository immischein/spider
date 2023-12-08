from adafruit_servokit import ServoKit
from time import sleep

# Initialize the ServoKit object
kit = ServoKit(channels=16, address = 0x40)
kit2 = ServoKit(channels=16, address = 0x41)
deg = 180
kit2.servo[0].angle = 90
kit2.servo[1].angle = 90
kit2.servo[2].angle = 180
        

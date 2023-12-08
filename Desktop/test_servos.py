from adafruit_servokit import ServoKit
from time import sleep

# Initialize the ServoKit object
kit1 = ServoKit(channels=16, address = 0x40)
kit2 = ServoKit(channels=16, address = 0x41)
deg =  90
deg2 = 70
deg3 = 180
kit1.servo[0].angle = deg
kit1.servo[1].angle = deg2
kit1.servo[2].angle = deg3
kit1.servo[3].angle = deg
kit1.servo[4].angle = deg2
kit1.servo[5].angle = deg3
kit1.servo[6].angle = deg
kit1.servo[7].angle = deg2
kit1.servo[8].angle = deg3
kit2.servo[0].angle = deg
kit2.servo[1].angle = deg2
kit2.servo[2].angle = deg3
kit2.servo[3].angle = deg
kit2.servo[4].angle = deg2
kit2.servo[5].angle = deg3
kit2.servo[6].angle = deg
kit2.servo[7].angle = deg2
kit2.servo[8].angle = deg3

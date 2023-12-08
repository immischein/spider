import numpy as np
from time import sleep
import sys
import click
from adafruit_servokit import ServoKit


@click.group()
def cmd_group():
    pass

class Spider:
    def __init__(self):
        """Initialize spider
        """        
        self.hat1 = ServoKit(channels=16, address = 0x40)
        self.hat2 = ServoKit(channels=16, address = 0x41)
        self.leg_1 = [self.hat1, [0,1,2], np.array([90,180,90])]
        self.leg_2 = [self.hat1, [3,4,5], np.array([90,180,90])]
        self.leg_3 = [self.hat1, [6,7,8], np.array([90,180,90])]
        self.leg_4 = [self.hat2, [0,1,2], np.array([90,180,90])]
        self.leg_5 = [self.hat2, [3,4,5], np.array([90,180,90])]
        self.leg_6 = [self.hat2, [6,7,8], np.array([90,180,90])]
        self.legs = [self.leg_1, self.leg_2, self.leg_3, self.leg_4, self.leg_5, self.leg_6]
        self.start_position()
    
    def move_single_leg(self, arr_deg, leg):
        """_summary_

        Args:
            arr_deg (arr): array with wanted angles for  all 3 servos 
            leg (arr): arr with information about leg hat, pins, angles.
        """        
        hat, channels, _ = leg
        hat.servo[channels[0]].angle = arr_deg[0]
        hat.servo[channels[1]].angle = arr_deg[1]
        hat.servo[channels[2]].angle = arr_deg[2]
        leg = hat, channels, np.array(arr_deg)
    
    @cmd_group.command()
    @click.option(
        '-d',
        '--arr_deg',
        default = [90,180,90],
        help = 'input should be an array with 3 different angles for the 3 different servo motors',
        show_default=True, # show default in help
    )
    def move_all_legs(self,arr_deg):
        """just simple calling move single leg function for all legs

        Args:
            arr_deg (arr): wanted angles for all legs
        """        
        for leg in self.legs:
            self.move_single_leg(arr_deg=arr_deg, leg=leg)

    @cmd_group.command()
    @click.option(
        help = 'return all legs to their starting positions',
    )
    def start_position(self):
        """Position where the spider is standing stable
        """        
        for leg in self.legs:
            self.move_single_leg([90,180,90], leg)

    def change_single(self, leg, degree):
        """Function that will change the angles of a single leg

        Args:
            leg (arr): Array with information about the leg
            degree (arr): angles that the leg needs to be changed too
        """        
        _, _, current_deg = leg
        # up 
        self.move_single_leg([current_deg[0], 150, current_deg[2]], leg)
        sleep(.3)
        self.move_single_leg([current_deg[0] + degree, 150, current_deg[2]], leg)
        sleep(.3)
        self.move_single_leg([current_deg[0], 180, 90], leg)
    
    @cmd_group.command()
    @click.option(
        help = 'all second motors will be reset to a starting position where they have no angles. [90,180,90]',
    )
    def reset_pos(self):
        """function that will reset all horizontal moving servos to 90 degrees
        """        
        self.hat1.servo[0].angle = 90
        self.hat1.servo[3].angle = 90
        self.hat1.servo[6].angle = 90
        self.hat2.servo[0].angle = 90
        self.hat2.servo[3].angle = 90
        self.hat2.servo[6].angle = 90

    @cmd_group.command()
    @click.option(
        '-d',
        '--degree',
        default = 30,
        help = 'the degrees all legs will change their horizontal angles',
        show_default=True, # show default in help
    )
    def change_all(self, degree):
        """just simple calling change single leg function for all legs

        Args:
            degree (_type_): angle of change on the horizontal axis ot the legs
        """        
        for leg in self.legs:
            self.change_single(leg=leg, degree=degree)
    

    def single_turn(self):
        """make a single turn with all legs from 90 degrees - start position
        to 180 degrees, and then reset.
        """        
        self.change_all(degree=30)
        sleep(.3)
        self.change_all(degree=30)
        sleep(.3)
        self.change_all(degree=30)
        sleep(.3)
        self.reset_pos()
    
    @cmd_group.command()
    @click.option(
        '-n',
        '--iterations',
        default = 1,
        help = 'amount of time you want to run the turn script',
        show_default=True, # show default in help
    )
    def turns(self, iterations):
        """call turn function turns times

        Args:
            turns (int): Iterations
        """        
        for _ in range(iterations):
            self.single_turn()

if __name__ == "__main__":
    cmd_group()

Arachnakiller = Spider()
Arachnakiller.turns(4)
Arachnakiller.move_all_legs([90, 180, 90])
Arachnakiller.move_all_legs([90,90,90])




        
    




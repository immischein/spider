import numpy as np
from time import sleep
import time
from adafruit_servokit import ServoKit

class Spider:
    def __init__(self):
        self.deg1,self.deg2,self.deg3 = 90, 70, 90
        """Initialize spider
        """        
        self.hat1 = ServoKit(channels=16, address = 0x40)
        self.hat2 = ServoKit(channels=16, address = 0x41)
        self.leg_1 = [self.hat1, [0,1,2], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_2 = [self.hat1, [3,4,5], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_3 = [self.hat1, [6,7,8], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_4 = [self.hat2, [0,1,2], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_5 = [self.hat2, [3,4,5], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_6 = [self.hat2, [6,7,8], np.array([self.deg1,self.deg2,self.deg3])]
        self.legs = [self.leg_1, self.leg_2, self.leg_3, self.leg_4, self.leg_5, self.leg_6]
        self.start_position()

    def move_single_leg(self, arr_deg, index_leg):
        """_summary_

        Args:
            arr_deg (arr): array with wanted angles for  all 3 servos 
            leg (index): arr with information about leg hat, pins, angles.
        """        
        hat, channels, _ = self.legs[index_leg]
        hat.servo[channels[0]].angle = arr_deg[0]
        hat.servo[channels[1]].angle = arr_deg[1]
        hat.servo[channels[2]].angle = arr_deg[2]
        self.legs[index_leg][2] = arr_deg
    
    def move_all_legs(self,arr_deg):
        """just simple calling move single leg function for all legs

        Args:
            arr_deg (arr): wanted angles for all legs
        """        
        for i, leg in enumerate(self.legs):
            self.move_single_leg(arr_deg=arr_deg, index_leg=i)

    def start_position(self):
        """Position where the spider is standing stable
        """        
        self.move_all_legs([self.deg1,self.deg2,self.deg3])

    def change_single(self, index_leg, change_deg):
        """Function that will change the angles of a single leg

        Args:
            leg (arr): Array with information about the leg
            change_deg (arr): angles that the leg needs to be changed too
        """        
        _, _, current_deg = self.legs[index_leg]
        # up 
        self.move_single_leg([current_deg[0], 150, current_deg[2]], index_leg)
        sleep(.1)
        self.move_single_leg([current_deg[0] + change_deg, 150, current_deg[2]], index_leg)
        sleep(.1)
        self.move_single_leg([current_deg[0] + change_deg, deg2, deg3], index_leg)
    
    def reset_pos(self):
        """function that will reset all horizontal moving servos to 90 degrees
        """        
        self.move_single_leg([90,self.leg_1[2][1], self.leg_1[2][2]], 0)
        self.move_single_leg([90,self.leg_2[2][1], self.leg_2[2][2]], 1)
        self.move_single_leg([90,self.leg_3[2][1], self.leg_3[2][2]], 2)
        self.move_single_leg([90,self.leg_4[2][1], self.leg_4[2][2]], 3)
        self.move_single_leg([90,self.leg_5[2][1], self.leg_5[2][2]], 4)
        self.move_single_leg([90,self.leg_6[2][1], self.leg_6[2][2]], 5)



    def change_all(self, change_deg):
        """just simple calling change single leg function for all legs

        Args:
            change_deg (_type_): _description_
        """        
        for i,leg in enumerate(self.legs):
            self.change_single(index_leg=i, change_deg=change_deg)
            sleep(.1)
    

    def single_turn(self):
        """make a single turn with all legs from 90 degrees - start position
        to 180 degrees, and then reset.
        """        
        self.change_all(change_deg=30)
        sleep(.5)
        self.change_all(change_deg=30)
        sleep(.5)
        self.change_all(change_deg=30)
        sleep(.5)
        self.reset_pos()
        sleep(.2)
    
    def turns(self, N):
        """call turn function N times

        Args:
            N (int): Iterations
        """        
        for i in range(N):
            self.single_turn()
    
    def walk1(self, steps):
        for _ in range(steps):
            
            # self.move_single_leg([self.leg_1[2][0] , self.leg_1[2][1]+ 45, self.leg_1[2][2]], 0)
            sleep(.1)
            self.change_single(0, 45)
            # sleep(.2)
            
            
            # self.move_single_leg([self.leg_3[2][0] , self.leg_3[2][1]+ 45, self.leg_3[2][2]], 2)
            #sleep(.1)
            self.change_single(2, 45)
            # sleep(.2)
            
            
            # self.move_single_leg([self.leg_5[2][0] , self.leg_5[2][1]+ 45, self.leg_5[2][2]], 4)
            #sleep(.1)
            self.change_single(4, -45)
            sleep(.2)


            self.start_position()
            # Move legs 2, 4, and 6
            # self.move_single_leg([self.leg_2[2][0] , self.leg_2[2][1]+ 45, self.leg_2[2][2]], 1)
            sleep(.1)
            self.change_single(1, 45)
            # sleep(.2)
            
            
            # self.move_single_leg([self.leg_4[2][0] , self.leg_4[2][1]+45, self.leg_4[2][2]], 3)
            #sleep(.1)
            self.change_single(3, -45)
            # sleep(.2)
            
            
            # self.move_single_leg([self.leg_6[2][0] , self.leg_6[2][1]+ 45, self.leg_5[2][2]], 5)
            #sleep(.1)
            self.change_single(5, -45)
            sleep(.2)


            self.start_position()
        
    def standup(self):
        self.move_single_leg([self.leg_1[2][0],0,60], 0)
        self.move_single_leg([self.leg_3[2][0],0,60], 2)
        self.move_single_leg([self.leg_4[2][0],0,60], 3)
        self.move_single_leg([self.leg_6[2][0],0,60], 5)
        self.move_single_leg([self.leg_1[2][0],0,60], 1)
        self.move_single_leg([self.leg_3[2][0],0,60], 4)

    def sit_stand_steps(self, N=10, delay=.5):
        if self.leg_1[2][1] >90 and self.leg_1[2][2]>120:
            change = -1
            changing_deg2 = abs(self.deg2 - self.leg_1[2][1])
            changing_deg3 = abs(self.deg3 - self.leg_1[2][2])
            deg_stand_steps_2 = changing_deg2/N*change
            deg_stand_steps_3 = changing_deg3/N*change
        else:
            change=1
            changing_deg2 = abs(175 - self.leg_1[2][1])
            changing_deg3 = abs(162 - self.leg_1[2][2])
            deg_stand_steps_2 = changing_deg2/N*change
            deg_stand_steps_3 = changing_deg3/N*change
        for _ in range(N):
            self.move_single_leg([self.leg_1[2][0],self.leg_1[2][1]+deg_stand_steps_2,self.leg_1[2][2]+deg_stand_steps_3], 0)
            self.move_single_leg([self.leg_2[2][0],self.leg_2[2][1]+deg_stand_steps_2,self.leg_2[2][2]+deg_stand_steps_3], 1)
            self.move_single_leg([self.leg_3[2][0],self.leg_3[2][1]+deg_stand_steps_2,self.leg_3[2][2]+deg_stand_steps_3], 2)
            self.move_single_leg([self.leg_4[2][0],self.leg_4[2][1]+deg_stand_steps_2,self.leg_4[2][2]+deg_stand_steps_3], 3)
            self.move_single_leg([self.leg_5[2][0],self.leg_5[2][1]+deg_stand_steps_2,self.leg_5[2][2]+deg_stand_steps_3], 4)
            self.move_single_leg([self.leg_6[2][0],self.leg_6[2][1]+deg_stand_steps_2,self.leg_6[2][2]+deg_stand_steps_3], 5)
            sleep(delay)
        
                
    def sitdown_steps(self,N =10, delay=.5):
        deg_stand_steps_2 = 110/N
        deg_stand_steps_3 = 90/N
        for _ in range(N-1):
            self.move_single_leg([self.leg_1[2][0],self.leg_1[2][1]+deg_stand_steps_2,self.leg_1[2][2]+deg_stand_steps_3], 0)
            self.move_single_leg([self.leg_2[2][0],self.leg_2[2][1]+deg_stand_steps_2,self.leg_2[2][2]+deg_stand_steps_3], 1)
            self.move_single_leg([self.leg_3[2][0],self.leg_3[2][1]+deg_stand_steps_2,self.leg_3[2][2]+deg_stand_steps_3], 2)
            self.move_single_leg([self.leg_4[2][0],self.leg_4[2][1]+deg_stand_steps_2,self.leg_4[2][2]+deg_stand_steps_3], 3)
            self.move_single_leg([self.leg_5[2][0],self.leg_5[2][1]+deg_stand_steps_2,self.leg_5[2][2]+deg_stand_steps_3], 4)
            self.move_single_leg([self.leg_6[2][0],self.leg_6[2][1]+deg_stand_steps_2,self.leg_6[2][2]+deg_stand_steps_3], 5)
            sleep(delay)
    
    def sitdown(self, delay):
        self.move_single_leg([self.leg_1[2][0],90,90], 0)
        self.move_single_leg([self.leg_3[2][0],90,90], 2)
        self.move_single_leg([self.leg_4[2][0],90,90], 3)
        self.move_single_leg([self.leg_6[2][0],90,90], 5)
        self.move_single_leg([self.leg_1[2][0],90,90], 1)
        self.move_single_leg([self.leg_3[2][0],90,90], 4)

        sleep(delay)

        self.move_single_leg([self.leg_1[2][0],90,60], 0)
        self.move_single_leg([self.leg_3[2][0],90,60], 2)
        self.move_single_leg([self.leg_4[2][0],90,60], 3)
        self.move_single_leg([self.leg_6[2][0],90,60], 5)
        self.move_single_leg([self.leg_1[2][0],90,60], 1)
        self.move_single_leg([self.leg_3[2][0],90,60], 4)

        sleep(delay)

        self.move_single_leg([self.leg_1[2][0],90,30], 0)
        self.move_single_leg([self.leg_3[2][0],90,30], 2)
        self.move_single_leg([self.leg_4[2][0],90,30], 3)
        self.move_single_leg([self.leg_6[2][0],90,30], 5)
        self.move_single_leg([self.leg_1[2][0],90,30], 1)
        self.move_single_leg([self.leg_3[2][0],90,30], 4)



    
    def walk_aida_immanuel(self, steps):
        self.change_single(0, 45)
        self.change_single(2, 45)
        self.change_single(4, -45)
        sleep(.1)
        # self.move_single_leg([self.leg_2[2][0], 0, self.leg_2[2][2]], 1)
        # self.move_single_leg([self.leg_4[2][0], 0, self.leg_4[2][2]], 3)
        # self.move_single_leg([self.leg_6[2][0], 0, self.leg_6[2][2]], 5)


    def turn3_0(self,steps, direction, speed = .5):
        
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True
        else:
            print('what direction is the turn, right or left?')
            go = False
            
        if go:
            for _ in range(steps):
            # Lift and move legs 0,1, 2 3, 4, 5 forward
                for leg_index in [0, 3, 4,2,1, 5]:
                    self.change_single(leg_index, angle)
                    time.sleep(speed)


                # Reset legs to starting position
                self.start_position()

    def walk_forward(self, steps, speed=0.5):
        for _ in range(steps):
            # Lift and move legs 0, 3, 4 forward
            self.change_single(0,30)
            time.sleep(speed)

            self.change_single(4,-30)
            time.sleep(speed)

            self.change_single(3,-30)
            time.sleep(speed)

            # Reset legs to starting position
            self.start_position()
            self.change_single(5,-30)
            time.sleep(speed)

            # Lift and move legs 1, 2, 5 forward
            self.change_single(1,30)
            time.sleep(speed)

            self.change_single(2,30)
            time.sleep(speed)

            # Reset legs to starting position
            self.start_position()

    def walk_forward_diagonal(self, steps, speed=0.5):
        for _ in range(steps):
            # Lift and move legs 0, 4 forward
            self.change_single(0, 30)
            time.sleep(speed)
            self.change_single(4, -30)
            

            # Reset legs to starting position
            # self.start_position()

            # Lift and move legs 1, 5 forward
            self.change_single(1, 30)
            time.sleep(speed)
            self.start_position()
            self.change_single(3, -30)

            # Reset legs to starting position
            # self.start_position()
            time.sleep(speed)

            # Lift and move legs 2, 3 forward
            self.change_single(2, 30)
            self.change_single(5, -30)
            time.sleep(speed)
            # Reset legs to starting position
            self.start_position()

    def tripod_turn(self, steps, direction, speed = 0.5):
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True

        else:
            print('what direction is the turn, right or left?')
            go = False
        if go:
            for _ in range(steps):
            # Lift and move legs 0,1, 2 3, 4, 5 forward
                for leg_index in [[0, 2, 4], [1, 3, 5]]:
                    _, _, current_deg_1 = self.legs[leg_index[0]]
                    _, _, current_deg_2 = self.legs[leg_index[1]]
                    _, _, current_deg_3 = self.legs[leg_index[2]]

                    self.move_single_leg([current_deg_1[0], 150, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0], 150, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0], 150, current_deg_3[2]], leg_index[2])

                    sleep(.1)
                    self.move_single_leg([current_deg_1[0] + angle, 150, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, 150, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, 150, current_deg_3[2]], leg_index[2])

                    sleep(.1)
                    self.move_single_leg([current_deg_1[0] + angle, self.deg2, self.deg3], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, self.deg2, self.deg3], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, self.deg2, self.deg3], leg_index[2])

                    time.sleep(speed)
                    
                    # Reset legs to starting position
                    self.start_position()


arachnokiller = Spider()

a=1
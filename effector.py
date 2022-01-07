import sys
import time
import numpy as np

sys.path.append('/home/pi/mlf/core')
from serial_control import SerialControl

robot_serial = SerialControl()
robot_serial.open_serial()

class Effector:
    def __init__(self, a0 = 90, a1 = 40):
        self.angmin = a0
        self.angmax = a1
        self.ang0 = 90

    def action(self, a=1):
        if a:
            #close
            robot_serial.write_servo(4, self.angmin)
        else:
            #open
            robot_serial.write_servo(4, self.angmax)

    def set_angle(self, ang):
        if ang>90 or ang<40:
            print('ang out of range') 
            #no se como ponerlo como si fuera un error fkjgdg de ahí lo busco
        else:
            dif = self.ang0 - ang
            if dif>0:
                for i in range(dif + 1):
                    ang = self.ang0 - i
                    robot_serial.write_servo(4, ang)
                    time.sleep(0.05)
            else: 
                for i in range(abs(dif) + 1):
                    ang = 10 + i
                    robot_serial.write_servo(4, ang)
                    time.sleep(0.05)
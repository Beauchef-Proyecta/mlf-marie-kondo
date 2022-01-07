import sys
import time
import numpy as np

sys.path.append('/home/pi/mlf/core')
from serial_control import SerialControl

robot_serial = SerialControl()
robot_serial.open_serial()

class Effector:
    def __init__(self, a0 = 90, a1 = 40):
        self.ang = 0
        self.angmin = a0
        self.angmax = a1

    def action(self, a=1):
        if a:
            #open
            robot_serial.run_effector(self.angmin)
        else:
            #close
            robot_serial.run_effector(self.angmax)




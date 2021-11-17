import sys
sys.path.append('/home/pi/mlf-marie-kondo')
from serial_control import SerialControl
from mk2robot import MK2Robot
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc
import time
import numpy as np

robot_serial = SerialControl()
robot_serial.open_serial()

class Effector:
    def __init__(self, a0 = 90, a1 = 40):
        self.ang = 0
        self.angmin = a0
        self.angmax = a1

    def close(self,i=10):#angulo para cerrarse es 90
        robot_serial.run_effector(self.angmin)

    def open(self):
        robot_serial.run_effector(self.angmax)




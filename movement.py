import sys
sys.path.append('/home/pi/mlf-marie-kondo')
from serial_control import SerialControl
from mk2robot import MK2Robot
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc
import time
import numpy as np

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl()
robot_serial.open_serial()

#X_poses = np.array([200, 250, 280, 320])
#Y_poses = np.array([0, 0, 0, 0])
#Z_poses = np.array([140, 150, 160, 170])

#q0, q1, q2 = robot.inverse_kinematics(X_poses[i], Y_poses[i], Z_poses[i])
robot_serial.write_servo(1, 90)

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


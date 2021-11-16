import sys
sys.path.append('/home/pi/mlf/core')
from serial_control import SerialControl
from mk2robot import MK2Robot
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc
import time
import numpy as np

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl()

robot_serial.open_serial()

X_poses = np.array([200, 250, 280, 320])
Y_poses = np.array([0, 0, 0, 0])
Z_poses = np.array([140, 150, 160, 170])

for i in range(len(X_poses)):
    q0, q1, q2 = robot.inverse_kinematics(X_poses[i], Y_poses[i], Z_poses[i])
    robot_serial.write_servo(1, q0 + 45)
    robot_serial.write_servo(2, 90 - q1)
    robot_serial.write_servo(3, q2 + q1)
    time.sleep(1.2)

robot_serial.read_status()
robot_serial.read_sensors()
robot_serial.run_effector()

robot_serial.close_serial()

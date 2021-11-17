import sys
sys.path.append('/home/pi/mlf-marie-kondo')
from serial_control import SerialControl
from mk2robot import MK2Robot
from movement import Effector
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc
import time
import numpy as np

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl()
eff = Effector(80,40)

robot_serial.open_serial()

X_poses = np.array([200, 250, 280, 320])
Y_poses = np.array([0, 0, 0, 0])
Z_poses = np.array([140, 150, 160, 170])

robot_serial.run_effector(40)
time.sleep(1.2)
robot_serial.run_effector(90)
print("voy 2")
time.sleep(1.2)
robot_serial.run_effector(60)
print("voy 3")
time.sleep(1.2)
robot_serial.run_effector(40)

q0, q1, q2 = robot.inverse_kinematics(X_poses[i], Y_poses[i], Z_poses[i])
robot_serial.write_servo(1, q0 + 45)
eff.open()
time.sleep(1.2)
robot_serial.write_servo(2, 90 - q1)
eff.close()
time.sleep(1.2)
robot_serial.write_servo(3, q2 + q1)
eff.open()
time.sleep(1.2)

print("termine")
time.sleep(1.2)

robot_serial.read_status()
robot_serial.read_sensors()
robot_serial.close_serial()

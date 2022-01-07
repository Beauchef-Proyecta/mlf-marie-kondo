#import sys
#sys.path.append('/home/pi/mlf/core')
from effector import Effector
from mlf.core.serial_control import SerialControl
from mlf.core.mk2robot import MK2Robot

import time
import cv2
import matplotlib.pyplot as plt
import numpy as np

robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot_serial = SerialControl()
robot_serial.open_serial()
eff = Effector()

eff.action(1)
robot_serial.write_servo(1, 90)
time.sleep(1.2)
eff.action(0)
robot_serial.write_servo(1, 45)

def main():
    return
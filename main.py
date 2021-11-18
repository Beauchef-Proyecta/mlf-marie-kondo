import sys
sys.path.append('/home/pi/mlf/core')
from serial_control import SerialControl
from mk2robot import MK2Robot
from movement import Effector
#from core.serial_control import SerialControl #for pc
#from core.mk2robot import MK2Robot #for pc
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    return
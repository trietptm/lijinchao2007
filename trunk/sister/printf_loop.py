# coding:gbk
from ctypes import *
import time

msvcrt = cdll.msvcrt
counter = 0

while True:
    msvcrt.printf("ѭ��count: %d \n" % counter)
    time.sleep(2)
    counter += 1

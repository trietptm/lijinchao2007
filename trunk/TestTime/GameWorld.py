#coding:gbk
import sys
import os
BaseDir = os.path.abspath(os.path.curdir)
MongoManagerDir = os.path.join(BaseDir, "MongoManager")
sys.path.append(MongoManagerDir)
import log
Log = log.Log
ErrLog = log.ErrLog

import MongoManager
import MyTimer
  
def RegisterTime(func, count=-1, second=-1, minute=-1, hour=-1):    
    MyTimer.RegisterTime(func, count, second, minute, hour) 
    
def RegisterTimerEx(name, interval, func, count = -1):
    MyTimer.RegisterTimerEx(name, interval, func, count)
    
def GetMongoManager():
    MongoManager.GetMongoManager()
    
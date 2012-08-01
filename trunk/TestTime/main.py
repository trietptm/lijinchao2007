#coding:gbk
import log
import GameWorld
import time
Log = log.Log
ErrLog = log.ErrLog

now = time.localtime(time.time())
year, month, day, hour, minute, second, weekday, yearday, daylight = now

def TestSecond():
    print "second"
    

def TestMinute():
    print "Minute"
    

def TestHour():
    print "hour"
    
GameWorld.RegisterTime(TestSecond, 3, second)
GameWorld.RegisterTime(TestSecond, 3, second+1)
GameWorld.RegisterTime(TestMinute, 3, second, minute)
GameWorld.RegisterTime(TestMinute, 3, second, minute+1)
GameWorld.RegisterTime(TestHour, 3, second, minute, hour)
GameWorld.RegisterTime(TestHour, 3, second+1, minute, hour)
GameWorld.run()
    
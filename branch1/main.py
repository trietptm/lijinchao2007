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
    
#GameWorld.RegisterTime(TestSecond, 2, second, 0, 0)
#GameWorld.RegisterTime(TestSecond, 2, second+1, 0, 0)
#GameWorld.RegisterTime(TestMinute, 2, second, minute, 0)
GameWorld.RegisterTime(TestMinute, 2, second+1, minute, 0)
#GameWorld.RegisterTime(TestHour, 2, second, minute, hour )
GameWorld.RegisterTime(TestHour, 2, second+1, minute, hour )
GameWorld.RegisterTime(TestHour, 2, second+3, minute, hour )
GameWorld.RegisterTime(TestHour, 2, second+4, minute, hour )
GameWorld.run()
    
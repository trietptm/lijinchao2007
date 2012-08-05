#coding:gbk
import log
import GameWorld
import time
import profile
import pstats
Log = log.Log
ErrLog = log.ErrLog

now = time.localtime(time.time())
year, month, day, hour, minute, second, weekday, yearday, daylight = now

def TestSecond():
    #print "second"
    pass

def TestMinute():
    #print "Minute"
    pass

def TestHour():
    #print "hour"
    pass

for i in range(1000):
    funcCode = '''def fun%s():
    for i in xrange(10000):
        pass'''%i
    exec funcCode
    func = locals()["fun%s"%i]
    GameWorld.RegisterTime(func, -1, second+1)
    GameWorld.RegisterTime(func, -1, second+1, minute)

p = profile.Profile()
p.run("GameWorld.run()")
s = pstats.Stats(p)
s.sort_stats("time", "name").print_stats()

   
#GameWorld.RegisterTime(TestSecond, 3, second)
#GameWorld.RegisterTime(TestSecond, 3, second+1)
#GameWorld.RegisterTime(TestMinute, 3, second, minute)
#GameWorld.RegisterTime(TestMinute, 3, second+1, minute)
#GameWorld.RegisterTime(TestHour, 3, second, minute, hour)
#GameWorld.RegisterTime(TestHour, 3, second+1, minute, hour)
#GameWorld.run()

    
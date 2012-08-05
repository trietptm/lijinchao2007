#coding:gbk
#分析函数运行时间

#@verson=1.0

#------------------------------------------------
import profile
import pstats
#------------------------------------------------
# 全局变量
#------------------------------------------------
def func1():
    for i in xrange(10000):
        pass
def func2():
    for i in xrange(10000):
        func1()
p = profile.Profile()
p.run("func2()")

s = pstats.Stats(p)
s.sort_stats("time", "name").print_stats()
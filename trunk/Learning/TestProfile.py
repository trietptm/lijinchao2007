#coding:gbk
#������������ʱ��

#@verson=1.0

#------------------------------------------------
import profile
import pstats
#------------------------------------------------
# ȫ�ֱ���
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
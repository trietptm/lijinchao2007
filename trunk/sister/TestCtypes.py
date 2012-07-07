# -*- coding: cp936 -*-
from ctypes import *
m = cdll.msvcrt
mm = "djfi"
m.printf("tt")
intA = c_int(23)
m.printf("intA:%d", intA)


#libc = CDLL("Non_MFC_DLL.dll")
#print libc.Max(22,3)
print "是分"

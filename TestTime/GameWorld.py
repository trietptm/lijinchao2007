#coding:gbk
import sys
import os
BaseDir = os.path.abspath(os.path.curdir)
MongoManagerDir = os.path.join(BaseDir, "MongoManager")
sys.path.append(MongoManagerDir)

import MongoManager
import log
import time
import copy
Log = log.Log
ErrLog = log.ErrLog

# 全局
SecondFuncList = []
MinuteFuncList = []
HourFuncList = []

g_second = -1
g_minute = -1
g_hourt = -1

def RegisterTime(func, count=-1, second=-1, minute=-1, hour=-1):
    if count == 0:
        ErrLog("次数不可为0")
        return
    
    funcDict = {"func":func, "second":second, "minute":minute, "hour":hour, "count":count, "passed":False}
    if hour != -1:
        if funcDict in HourFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了小时函数", funcDict)
        HourFuncList.append(funcDict)
        return
    
    if minute != -1:
        if funcDict in MinuteFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了分钟函数", funcDict)
        MinuteFuncList.append(funcDict)
        return
    
    if second != -1:
        if funcDict in SecondFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了秒函数", funcDict)
        SecondFuncList.append(funcDict)
        return

def OnHour(hour):
    Log("HourFuncList", HourFuncList)
    # 小时计时器
    for funcDict in copy.copy(HourFuncList):
        if hour == funcDict["hour"]:
            copyDict = copy.copy(funcDict)
            copyDict["count"] = 1
            MinuteFuncList.append(copyDict)
                
            if funcDict["count"] != -1:
                funcDict["count"] -= 1
            
            if funcDict["count"] == 0:
                HourFuncList.remove(funcDict)
    Log("HourFuncList", HourFuncList)
    
def OnMinute(minute):
    Log("MinuteFuncList", MinuteFuncList)
    # 分钟计时器
    for funcDict in copy.copy(MinuteFuncList):
        if minute == funcDict["minute"]:
            copyDict = copy.copy(funcDict)
            copyDict["count"] = 1
            # 加入秒计时
            SecondFuncList.append(copyDict)
            
            if funcDict["count"] != -1:
                funcDict["count"] -= 1
            if funcDict["count"] == 0:
                MinuteFuncList.remove(funcDict)
            # 此轮已经运行过
            funcDict["passed"] = True
    Log("MinuteFuncList", MinuteFuncList)
    
def OnSecond(second):
    #Log("SecondFuncList", SecondFuncList)               
    # 秒计时器
    copySecondFuncList = copy.copy(SecondFuncList)
    for funcDict in copySecondFuncList:
        if second == funcDict["second"]:
            if funcDict["count"] != -1:
                funcDict["count"] -= 1
                
            func = funcDict["func"]
            
            if funcDict["count"] == 0:
                SecondFuncList.remove(funcDict)
            func()

RunTimes = 10
Start = 0     
def run():    
    global g_hourt
    global g_minute
    global g_second
    global Start
    while True:
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        print time.strftime("%c", now)
        
        # 首次
        if g_hourt == -1:
            OnHour(hour)
            g_hourt = hour
        else:
            # 小时跳变
            if minute == 0 and second ==0:
                OnHour(hour)
        # 首次
        if g_minute == -1:
            OnMinute(minute)
            g_minute = minute
        else:
            # 分钟跳变
            if second ==0:
                OnMinute(minute)
                
        OnSecond(second)
        if Start == RunTimes:
            break
        Start += 1
        time.sleep(1)  #每30秒执行一次   



a()
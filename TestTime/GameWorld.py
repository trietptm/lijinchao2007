#coding:gbk
import log
import time
import copy
Log = log.Log
ErrLog = log.ErrLog

# 全局
SecondFuncList = []
MinuteFuncList = []
HourFuncList = []

g_second = 0
g_minute = 0
g_hourt = 0

def RegisterTime(func, count=-1, second=0, minute=0, hour=0):
    if count == 0:
        ErrLog("次数不可为0")
        return
    
    funcDict = {"func":func, "second":second, "minute":minute, "hour":hour, "count":count, "passed":False}
    if hour:
        if funcDict in HourFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了小时函数", funcDict)
        HourFuncList.append(funcDict)
        return
    
    if minute:
        if funcDict in MinuteFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了分钟函数", funcDict)
        MinuteFuncList.append(funcDict)
        return
    
    if second:
        if funcDict in SecondFuncList:
            ErrLog("已经注册了", funcDict)
            return
 
        Log("注册了秒函数", funcDict)
        SecondFuncList.append(funcDict)
        return
    

    
def run():    
    print "run"
    while True:
    #    s=time.ctime()
    #    length=len(s)
    #    Log(length, s)
    #    ErrLog(length, s)
        now = time.localtime(time.time())
        year, month, day, hour, minute, second, weekday, yearday, daylight = now
        #print time.strftime("%c", now)
        
        Log("HourFuncList", HourFuncList)
        # 小时计时器
        for funcDict in copy.copy(HourFuncList):
            # 已经运行过,并且不再可运行的条件之中
            if funcDict["passed"] and hour != funcDict["hour"]:
                funcDict["passed"] = False
                continue
            
            if hour == funcDict["hour"]:
                # 已经运行过就不再运行
                if funcDict["passed"]:
                    continue
                copyDict = copy.copy(funcDict)
                copyDict["count"] = 1
                MinuteFuncList.append(copyDict)
                    
                if funcDict["count"] != -1:
                    funcDict["count"] -= 1
                
                if funcDict["count"] == 0:
                    HourFuncList.remove(funcDict)
                # 此轮已经运行过
                funcDict["passed"] = True 
                
        Log("MinuteFuncList", MinuteFuncList)
        # 分钟计时器
        for funcDict in copy.copy(MinuteFuncList):
            # 已经运行过,并且不再可运行的条件之中
            if funcDict["passed"] and minute != funcDict["minute"]:
                funcDict["passed"] = False
                continue
            
            if minute == funcDict["minute"]:
                if funcDict["passed"]:
                    continue
                
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
        
        Log("SecondFuncList", SecondFuncList)               
        # 秒计时器
        copySecondFuncList = copy.copy(SecondFuncList)
        for funcDict in copySecondFuncList:
            #Log("funcDict", funcDict)  
            if second == funcDict["second"]:
                if funcDict["count"] != -1:
                    funcDict["count"] -= 1
                    
                func = funcDict["func"]
                
                if funcDict["count"] == 0:
                    SecondFuncList.remove(funcDict)
                
                func()
                print time.strftime("%c", now)
        time.sleep(1)  #每30秒执行一次   



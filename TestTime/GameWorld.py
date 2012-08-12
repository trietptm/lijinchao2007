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

# ȫ��
SecondFuncList = []
MinuteFuncList = []
HourFuncList = []

g_second = -1
g_minute = -1
g_hourt = -1

def RegisterTime(func, count=-1, second=-1, minute=-1, hour=-1):
    if count == 0:
        ErrLog("��������Ϊ0")
        return
    
    funcDict = {"func":func, "second":second, "minute":minute, "hour":hour, "count":count, "passed":False}
    if hour != -1:
        if funcDict in HourFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע����Сʱ����", funcDict)
        HourFuncList.append(funcDict)
        return
    
    if minute != -1:
        if funcDict in MinuteFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע���˷��Ӻ���", funcDict)
        MinuteFuncList.append(funcDict)
        return
    
    if second != -1:
        if funcDict in SecondFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע�����뺯��", funcDict)
        SecondFuncList.append(funcDict)
        return

def OnHour(hour):
    Log("HourFuncList", HourFuncList)
    # Сʱ��ʱ��
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
    # ���Ӽ�ʱ��
    for funcDict in copy.copy(MinuteFuncList):
        if minute == funcDict["minute"]:
            copyDict = copy.copy(funcDict)
            copyDict["count"] = 1
            # �������ʱ
            SecondFuncList.append(copyDict)
            
            if funcDict["count"] != -1:
                funcDict["count"] -= 1
            if funcDict["count"] == 0:
                MinuteFuncList.remove(funcDict)
            # �����Ѿ����й�
            funcDict["passed"] = True
    Log("MinuteFuncList", MinuteFuncList)
    
def OnSecond(second):
    #Log("SecondFuncList", SecondFuncList)               
    # ���ʱ��
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
        
        # �״�
        if g_hourt == -1:
            OnHour(hour)
            g_hourt = hour
        else:
            # Сʱ����
            if minute == 0 and second ==0:
                OnHour(hour)
        # �״�
        if g_minute == -1:
            OnMinute(minute)
            g_minute = minute
        else:
            # ��������
            if second ==0:
                OnMinute(minute)
                
        OnSecond(second)
        if Start == RunTimes:
            break
        Start += 1
        time.sleep(1)  #ÿ30��ִ��һ��   



a()
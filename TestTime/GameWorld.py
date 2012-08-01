#coding:gbk
import log
import time
import copy
Log = log.Log
ErrLog = log.ErrLog

# ȫ��
SecondFuncList = []
MinuteFuncList = []
HourFuncList = []

g_second = 0
g_minute = 0
g_hourt = 0

def RegisterTime(func, count=-1, second=0, minute=0, hour=0):
    if count == 0:
        ErrLog("��������Ϊ0")
        return
    
    funcDict = {"func":func, "second":second, "minute":minute, "hour":hour, "count":count, "passed":False}
    if hour:
        if funcDict in HourFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע����Сʱ����", funcDict)
        HourFuncList.append(funcDict)
        return
    
    if minute:
        if funcDict in MinuteFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע���˷��Ӻ���", funcDict)
        MinuteFuncList.append(funcDict)
        return
    
    if second:
        if funcDict in SecondFuncList:
            ErrLog("�Ѿ�ע����", funcDict)
            return
 
        Log("ע�����뺯��", funcDict)
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
        # Сʱ��ʱ��
        for funcDict in copy.copy(HourFuncList):
            # �Ѿ����й�,���Ҳ��ٿ����е�����֮��
            if funcDict["passed"] and hour != funcDict["hour"]:
                funcDict["passed"] = False
                continue
            
            if hour == funcDict["hour"]:
                # �Ѿ����й��Ͳ�������
                if funcDict["passed"]:
                    continue
                copyDict = copy.copy(funcDict)
                copyDict["count"] = 1
                MinuteFuncList.append(copyDict)
                    
                if funcDict["count"] != -1:
                    funcDict["count"] -= 1
                
                if funcDict["count"] == 0:
                    HourFuncList.remove(funcDict)
                # �����Ѿ����й�
                funcDict["passed"] = True 
                
        Log("MinuteFuncList", MinuteFuncList)
        # ���Ӽ�ʱ��
        for funcDict in copy.copy(MinuteFuncList):
            # �Ѿ����й�,���Ҳ��ٿ����е�����֮��
            if funcDict["passed"] and minute != funcDict["minute"]:
                funcDict["passed"] = False
                continue
            
            if minute == funcDict["minute"]:
                if funcDict["passed"]:
                    continue
                
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
        
        Log("SecondFuncList", SecondFuncList)               
        # ���ʱ��
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
        time.sleep(1)  #ÿ30��ִ��һ��   



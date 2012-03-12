#!/usr/bin/python
# -*- coding: GBK -*-
#author:李金潮
#version:子弹_集中到中间(带预判位置注释掉)

import GameWorld 
import GameComm
import math
import time

AI_NAME = "lijinchaoex"
# 调试信息输出
def log(argv, flag=True):
    if flag:
        output = AI_NAME
        output += "####" + str(type(argv)) + ": " + str(argv) 
        GameWorld.IPY_GameWorld().OutputDebugInfo(output)
#aitick
Def_Max_AI_Tick = 110
#使用buff的时间       
BuffTick = 0
#记录上次生物的位置
posDict = {} # handle:(x,y)
INFINITE = 9999999999
LastTick = INFINITE
temTick = 0
idd = 0
# 本ai把所有的位置和方向都换算成了以屏幕左上为原点的坐标系
def ProcessAI(UnitHandle):
    global temTick
    global idd
    #武器起始位置
    firestart = 5
    fireend = 6
    
    #子弹速度
    boomSpeed = 3
    bulletSpeed = 3
    
    #处理距离,若超出此距离则要向目标或者屏幕中央移动
    MinDis = 550
    MaxDis = 250
    #使用眼睛的时间间隔
    interval = 12000   
    global BuffTick
    global LastTick
    
    #屏幕中央的位置
    width = 400 #GW.GetSceneWidth() / 2
    height = 300 #GW.GetSceneHeight() / 2
    
    UH = UnitHandle
    GW = GameWorld.IPY_GameWorld()
    selfInfo = GW.GetUnitInfo(UH)    
    log("%d---------------------------------------------------------" % idd)
    log(GW.GetCpuTick() - temTick)
    temTick = GW.GetCpuTick()   
    idd = idd + 1
    #移动或者转动的最大值
    MoveSpeed, RollValue = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    
    #遍历周围生物
    clist = []  # 存储creatur
    danger = []   # 存储有威胁的对象
    for i in range(0, GW.GetNearUnitCount(UH)):
        h = GW.GetNearUnitHandleByIndex(UH, i)
        info = GW.GetUnitInfo(h)
        dis, dir = GetDisAndDir(selfInfo, info)  #得到与目标的距离和在绝对坐标系中的方向(此处为修订后的结果)
        
        if info.Type == 'creature' and h != GW:
                       
            MinDir = GetFireDegress(info, dis)  # 开火能够命中的最大偏差角度
            clist.append([dis, dir, MinDir, info]) # 距离, 角度, 命中的最大偏差, 敌人信息
   
        if info.Type in ['bullet', 'missile', 'bombbullet'] and info.MasterId != selfInfo.ID:

            if dis * info.MoveSpeed > 360: # 伤害超出200ms的范围,则暂不考虑
                continue
#            if math.cos(math.radians(dir - info.Dir)) > 0: # 说明子弹已经躲过去了
#                log("####过去的子弹,dis:" + str(dis))
#                continue
            log('#####加入danger,dis:' + str(dis))
            danger.append([dis, info])
 
    # 按距离排序
    clist.sort(key=lambda x:x[0])   
    danger.sort(key=lambda x:x[0])   

    # 闪避
    MinTime = 10000
    for i in danger:

        return ShanBi(selfInfo, i[1])
    
    #存储最小的角度 及相应的距离
    temMinDir = 180
    temDis = 1000   
    
    selfdir = GetDegress(selfInfo.Dir) # 嘴的方向就是本身的方向
    for l in clist:
        dirCos = math.cos(math.radians(selfdir - l[1])) # 前者是嘴的方向,后者是本体指向敌人的方向        
        if dirCos > math.cos(math.radians(temMinDir)):
            temMinDir = selfdir - l[1] #角度差
            temDis = l[0]

    # 使用flipper
    if GW.CheckUnitBuff(UH, 'Fast') == 0:
        log('启用flipper')
        return "4 4"
                       
    # 遍历完成未能 咬人
    # 距离要在mindis以内,且角度要大于能够加速的角度
    if temDis <= MinDis and (temDis >= MaxDis) and (dirCos < math.cos(math.radians(l[2]))) :
        log("偏转角度: " + str(temMinDir))
        result = math.fabs(temMinDir) 
        if result > 180:
            result = 360 - result
        
        if result > 90:  # 角度太大,前进
            log("$$$$前进")
            return MoveSpeed[3] 
        
        if math.sin(math.radians(temMinDir)) > 0:
            log("$$$$左转", 1)
            return "1 %d" % min(RollValue, int(result))
        else:
            log("$$$$右转", 1)
            return "2 %d" % min(RollValue, int(result))
        
    # 若是太远,则移动到最近的敌人旁边 但在40-570间          

    if len(clist) > 0:
        near = clist[0]
        nearInfo = clist[0][3]
        if near[0] > MinDis:
            log("####走进")
            return Move(selfInfo, nearInfo.PosX, nearInfo.PosY)
        if near[0] < MaxDis:
            log("####远离")
            x1, y1 = [selfInfo.PosX, selfInfo.PosY]
            x2, y2 = [nearInfo.PosX, nearInfo.PosY]
            x = x2 + (x1 - x2) * MaxDis / near[0]
            y = y2 + (y1 - y2) * MaxDis / near[0]
            return Move(selfInfo, x, y)   
    else:
        # 找不到生物则,启动眼睛
        if (GW.GetCpuTick() - BuffTick > interval) : 
            for i in range(0, 3): #遍历眼睛,冷却则使用
                eye = GW.GetUnitPartInfoByIndex(UH, i)
                if eye.IsDuringCD == 0:
                    BuffTick = GW.GetCpuTick()  #记录时间
                    log("#### 启动眼睛")
                    return "4 %d" % i
        #若以上均未操作,则向中间移动   
        log("向中间移动")
        return Move(selfInfo, width, height)         

#移动到某点
# 小于25度移动
# 大于25小于45 转动
def Move(selfinfo, x, y):
    sx = selfinfo.PosX
    sy = selfinfo.PosY
    
    degress = GetDegressByXY(x - sx, y - sy) # 本体指向目标的矢量方向
    dir = (GetDegress(selfinfo.Dir) - degress + 180) % 360
    
    MoveValue, tt = GetBestMoveAndDir(selfinfo, Def_Max_AI_Tick)
    log("#########移动距离:" + str(MoveValue))
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        return MoveValue[7]  # 后退
    if dir > 45 and dir < 135:
        return MoveValue[5]   # 左移    
    if dir >= 135 and dir < 225:
        return MoveValue[3]  # 前进
    if dir >= 225 and dir < 315:
        return MoveValue[6]   # 右移动
                    
#param:自己实例 目标实例
#return 距离 和  面向偏差角度            
def GetDisAndDir(selfInfo, info):
    x1 = selfInfo.PosX
    y1 = selfInfo.PosY
    x2 = info.PosX
    y2 = info.PosY
    
    dis = math.hypot(x1 - x2, y1 - y2)  #本体与目标距离
    degress = GetDegressByXY(x2 - x1, y2 - y1) # 本体指向目标的矢量方向
    dir = degress   
    return dis, dir

# 得到多少度可以开火(mindir)
def GetFireDegress(target, dis):
    panduan = math.fabs(target.BodyHeight - target.BodyWidth) 
    if dis != 0:
        tanValue = (5) * 2 / (2 * dis)
    else:
        tanValue = 999
    degrees = math.degrees(math.atan(tanValue))             
    return degrees

#根据x y 得到在坐标系中的度数
def GetDegressByXY(x, y):
    radian = math.atan2(y, x) 
    degress = (360 + math.degrees(radian)) % 360
    return degress
       
# 坐标系为y轴反了 dir少了一个象限
def GetDegress(dir):
    return (dir + 270) % 360    

def GetBestMoveAndDir(selfInfo, AiTick):
    moveSpeed = selfInfo.MoveSpeed
    upMoveDis = int(AiTick / (moveSpeed * 1.1))
    downMoveDis = int((AiTick) / (moveSpeed * 1.5))
    sideMoveDis = int((AiTick) / (moveSpeed * 1.3))
    cmdDict = {}
    cmdDict[3] = "3 %d" % upMoveDis
    cmdDict[7] = "7 %d" % downMoveDis
    cmdDict[5] = "5 %d" % sideMoveDis
    cmdDict[6] = "6 %d" % sideMoveDis

   
    Dir = int(AiTick / selfInfo.RollSpeed)
    return cmdDict, Dir

def ShanBi(selfInfo, Info):
    selfDir = selfInfo.Dir
    dd, enemyDir = GetDisAndDir(Info, selfInfo) #敌人朝向我的方向
    infoDir = Info.Dir  #敌人自己的方向
    MoveValue, tt = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    log("####return闪避距离:" + str(MoveValue))
    dir = (selfDir - enemyDir) % 360 
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        log("##########后,dir: " + str(dir))
        return MoveValue[7]  # 后退
    if dir > 45 and dir < 135:
        log("##########左,dir: " + str(dir))
        return MoveValue[5]   # 左移    
    if dir >= 135 and dir < 225:
        log("##########前,dir: " + str(dir))
        return MoveValue[3]  # 前进
    if dir >= 225 and dir < 315:
        log("##########右,dir: " + str(dir))
        return  MoveValue[6]   # 右移动

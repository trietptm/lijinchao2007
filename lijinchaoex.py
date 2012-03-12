#!/usr/bin/python
# -*- coding: GBK -*-
#author:���
#version:�ӵ�_���е��м�(��Ԥ��λ��ע�͵�)

import GameWorld 
import GameComm
import math
import time

AI_NAME = "lijinchaoex"
# ������Ϣ���
def log(argv, flag=True):
    if flag:
        output = AI_NAME
        output += "####" + str(type(argv)) + ": " + str(argv) 
        GameWorld.IPY_GameWorld().OutputDebugInfo(output)
#aitick
Def_Max_AI_Tick = 110
#ʹ��buff��ʱ��       
BuffTick = 0
#��¼�ϴ������λ��
posDict = {} # handle:(x,y)
INFINITE = 9999999999
LastTick = INFINITE
temTick = 0
idd = 0
# ��ai�����е�λ�úͷ��򶼻����������Ļ����Ϊԭ�������ϵ
def ProcessAI(UnitHandle):
    global temTick
    global idd
    #������ʼλ��
    firestart = 5
    fireend = 6
    
    #�ӵ��ٶ�
    boomSpeed = 3
    bulletSpeed = 3
    
    #�������,�������˾�����Ҫ��Ŀ�������Ļ�����ƶ�
    MinDis = 550
    MaxDis = 250
    #ʹ���۾���ʱ����
    interval = 12000   
    global BuffTick
    global LastTick
    
    #��Ļ�����λ��
    width = 400 #GW.GetSceneWidth() / 2
    height = 300 #GW.GetSceneHeight() / 2
    
    UH = UnitHandle
    GW = GameWorld.IPY_GameWorld()
    selfInfo = GW.GetUnitInfo(UH)    
    log("%d---------------------------------------------------------" % idd)
    log(GW.GetCpuTick() - temTick)
    temTick = GW.GetCpuTick()   
    idd = idd + 1
    #�ƶ�����ת�������ֵ
    MoveSpeed, RollValue = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    
    #������Χ����
    clist = []  # �洢creatur
    danger = []   # �洢����в�Ķ���
    for i in range(0, GW.GetNearUnitCount(UH)):
        h = GW.GetNearUnitHandleByIndex(UH, i)
        info = GW.GetUnitInfo(h)
        dis, dir = GetDisAndDir(selfInfo, info)  #�õ���Ŀ��ľ�����ھ�������ϵ�еķ���(�˴�Ϊ�޶���Ľ��)
        
        if info.Type == 'creature' and h != GW:
                       
            MinDir = GetFireDegress(info, dis)  # �����ܹ����е����ƫ��Ƕ�
            clist.append([dis, dir, MinDir, info]) # ����, �Ƕ�, ���е����ƫ��, ������Ϣ
   
        if info.Type in ['bullet', 'missile', 'bombbullet'] and info.MasterId != selfInfo.ID:

            if dis * info.MoveSpeed > 360: # �˺�����200ms�ķ�Χ,���ݲ�����
                continue
#            if math.cos(math.radians(dir - info.Dir)) > 0: # ˵���ӵ��Ѿ����ȥ��
#                log("####��ȥ���ӵ�,dis:" + str(dis))
#                continue
            log('#####����danger,dis:' + str(dis))
            danger.append([dis, info])
 
    # ����������
    clist.sort(key=lambda x:x[0])   
    danger.sort(key=lambda x:x[0])   

    # ����
    MinTime = 10000
    for i in danger:

        return ShanBi(selfInfo, i[1])
    
    #�洢��С�ĽǶ� ����Ӧ�ľ���
    temMinDir = 180
    temDis = 1000   
    
    selfdir = GetDegress(selfInfo.Dir) # ��ķ�����Ǳ���ķ���
    for l in clist:
        dirCos = math.cos(math.radians(selfdir - l[1])) # ǰ������ķ���,�����Ǳ���ָ����˵ķ���        
        if dirCos > math.cos(math.radians(temMinDir)):
            temMinDir = selfdir - l[1] #�ǶȲ�
            temDis = l[0]

    # ʹ��flipper
    if GW.CheckUnitBuff(UH, 'Fast') == 0:
        log('����flipper')
        return "4 4"
                       
    # �������δ�� ҧ��
    # ����Ҫ��mindis����,�ҽǶ�Ҫ�����ܹ����ٵĽǶ�
    if temDis <= MinDis and (temDis >= MaxDis) and (dirCos < math.cos(math.radians(l[2]))) :
        log("ƫת�Ƕ�: " + str(temMinDir))
        result = math.fabs(temMinDir) 
        if result > 180:
            result = 360 - result
        
        if result > 90:  # �Ƕ�̫��,ǰ��
            log("$$$$ǰ��")
            return MoveSpeed[3] 
        
        if math.sin(math.radians(temMinDir)) > 0:
            log("$$$$��ת", 1)
            return "1 %d" % min(RollValue, int(result))
        else:
            log("$$$$��ת", 1)
            return "2 %d" % min(RollValue, int(result))
        
    # ����̫Զ,���ƶ�������ĵ����Ա� ����40-570��          

    if len(clist) > 0:
        near = clist[0]
        nearInfo = clist[0][3]
        if near[0] > MinDis:
            log("####�߽�")
            return Move(selfInfo, nearInfo.PosX, nearInfo.PosY)
        if near[0] < MaxDis:
            log("####Զ��")
            x1, y1 = [selfInfo.PosX, selfInfo.PosY]
            x2, y2 = [nearInfo.PosX, nearInfo.PosY]
            x = x2 + (x1 - x2) * MaxDis / near[0]
            y = y2 + (y1 - y2) * MaxDis / near[0]
            return Move(selfInfo, x, y)   
    else:
        # �Ҳ���������,�����۾�
        if (GW.GetCpuTick() - BuffTick > interval) : 
            for i in range(0, 3): #�����۾�,��ȴ��ʹ��
                eye = GW.GetUnitPartInfoByIndex(UH, i)
                if eye.IsDuringCD == 0:
                    BuffTick = GW.GetCpuTick()  #��¼ʱ��
                    log("#### �����۾�")
                    return "4 %d" % i
        #�����Ͼ�δ����,�����м��ƶ�   
        log("���м��ƶ�")
        return Move(selfInfo, width, height)         

#�ƶ���ĳ��
# С��25���ƶ�
# ����25С��45 ת��
def Move(selfinfo, x, y):
    sx = selfinfo.PosX
    sy = selfinfo.PosY
    
    degress = GetDegressByXY(x - sx, y - sy) # ����ָ��Ŀ���ʸ������
    dir = (GetDegress(selfinfo.Dir) - degress + 180) % 360
    
    MoveValue, tt = GetBestMoveAndDir(selfinfo, Def_Max_AI_Tick)
    log("#########�ƶ�����:" + str(MoveValue))
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        return MoveValue[7]  # ����
    if dir > 45 and dir < 135:
        return MoveValue[5]   # ����    
    if dir >= 135 and dir < 225:
        return MoveValue[3]  # ǰ��
    if dir >= 225 and dir < 315:
        return MoveValue[6]   # ���ƶ�
                    
#param:�Լ�ʵ�� Ŀ��ʵ��
#return ���� ��  ����ƫ��Ƕ�            
def GetDisAndDir(selfInfo, info):
    x1 = selfInfo.PosX
    y1 = selfInfo.PosY
    x2 = info.PosX
    y2 = info.PosY
    
    dis = math.hypot(x1 - x2, y1 - y2)  #������Ŀ�����
    degress = GetDegressByXY(x2 - x1, y2 - y1) # ����ָ��Ŀ���ʸ������
    dir = degress   
    return dis, dir

# �õ����ٶȿ��Կ���(mindir)
def GetFireDegress(target, dis):
    panduan = math.fabs(target.BodyHeight - target.BodyWidth) 
    if dis != 0:
        tanValue = (5) * 2 / (2 * dis)
    else:
        tanValue = 999
    degrees = math.degrees(math.atan(tanValue))             
    return degrees

#����x y �õ�������ϵ�еĶ���
def GetDegressByXY(x, y):
    radian = math.atan2(y, x) 
    degress = (360 + math.degrees(radian)) % 360
    return degress
       
# ����ϵΪy�ᷴ�� dir����һ������
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
    dd, enemyDir = GetDisAndDir(Info, selfInfo) #���˳����ҵķ���
    infoDir = Info.Dir  #�����Լ��ķ���
    MoveValue, tt = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    log("####return���ܾ���:" + str(MoveValue))
    dir = (selfDir - enemyDir) % 360 
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        log("##########��,dir: " + str(dir))
        return MoveValue[7]  # ����
    if dir > 45 and dir < 135:
        log("##########��,dir: " + str(dir))
        return MoveValue[5]   # ����    
    if dir >= 135 and dir < 225:
        log("##########ǰ,dir: " + str(dir))
        return MoveValue[3]  # ǰ��
    if dir >= 225 and dir < 315:
        log("##########��,dir: " + str(dir))
        return  MoveValue[6]   # ���ƶ�

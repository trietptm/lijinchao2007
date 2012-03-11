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
def log(argv, flag=False):
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
# ��ai�����е�λ�úͷ��򶼻����������Ļ����Ϊԭ�������ϵ
def ProcessAI(UnitHandle):
    #������ʼλ��
    firestart = 5
    fireend = 6
    
    #�ӵ��ٶ�
    boomSpeed = 3
    bulletSpeed = 3
    
    #�������,�������˾�����Ҫ��Ŀ�������Ļ�����ƶ�
    MinDis = 550
    MaxDis = 100
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
    #�ƶ�����ת�������ֵ
    tt, RollValue = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    
    #������Χ����
    clist = []  # �洢creatur
    danger = []   # �洢����в�Ķ���
    for i in range(0, GW.GetNearUnitCount(UH)):
        h = GW.GetNearUnitHandleByIndex(UH, i)
        info = GW.GetUnitInfo(h)
        dis, dir = GetDisAndDir(selfInfo, info)  #�õ���Ŀ��ľ�����ھ�������ϵ�еķ���(�˴�Ϊ�޶���Ľ��)
        if info.Type == 'food':
                # ʹ��flipper
            if GW.CheckUnitBuff(UH, 'Fast') == 0:
                return "4 4"
            log('food')
            return Move(selfInfo, info.PosX, info.PosY)
        
        if info.Type == 'creature' and h != GW:
            #dis, dir = GetDisAndDir(selfInfo, info)  #�õ���Ŀ��ľ�����ھ�������ϵ�еķ���
            #bulletTime = bulletSpeed * dis # �ӵ���������ʱ��
            SetFuturePox(info, 100)  # �޶�Ŀ��200ms���λ��

            
            MinDir = GetFireDegress(info, dis)  # �����ܹ����е����ƫ��Ƕ�
            clist.append([dis, dir, MinDir, info]) # ����, �Ƕ�, ���е����ƫ��, ������Ϣ
   
        if info.Type in ['bullet', 'missile', 'bombbullet'] and info.MasterId != selfInfo.ID:
            #log("###�ӵ��ٶ� :" + str(info.Type) + ":" + str(info.MoveSpeed))

            if dis * info.MoveSpeed > 330: # �˺�����200ms�ķ�Χ,���ݲ�����
                continue
            if math.cos(math.radians(dir - info.Dir)) > 0: # ˵���ӵ��Ѿ����ȥ��
                log("####��ȥ���ӵ�")
                continue
            log('#####����danger')
            danger.append([dis, info])
            
        if info.Type == 'creature':
            ds, dr = GetDisAndDir(selfInfo, info)
    
            if ds < MaxDis + 60: # ��׷��һ��ʱ���thruster
                log("lasttick: " + str(LastTick))
                if LastTick == INFINITE:
                    LastTick = LastTick = GW.GetCpuTick()
                if GW.GetCpuTick() - LastTick > 1200: #����׷��3��
                    if GW.GetUnitPartInfoByIndex(UH, 11).IsDuringCD == 0:
                        log('####��׷�˺ܾ�...')
                        return "4 11"
            else:
                LastTick = INFINITE
            
            if GW.CheckUnitBuff(info.Handle, 'PowerShield') and ds < 100:  # �Է��ö� ��
                if GW.GetUnitPartInfoByIndex(UH, 11).IsDuringCD == 0:
                        return "4 11"
                
    # ����������
    clist.sort(key=lambda x:x[0])   
    danger.sort(key=lambda x:x[0])   

    # ����
    MinTime = 10000
    for i in danger:
        log("##########����")
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

        
        if (dirCos > math.cos(math.radians(l[2]))) or dirCos > 0.9994:
            for i in [6, 12]:
                if GW.GetUnitPartInfoByIndex(UH, i).IsDuringCD == 0:
                    log("###����6")
                    return "4 %d" % i
            
#        if (dirCos > math.cos(math.radians(l[2]))) and l[0] < 280 and l[0] < 220 : #����
#            for i in range(3, 4):
#                if  GW.GetUnitPartInfoByIndex(UH, i).IsDuringCD == 0:
#                    log("###����:")
#                    return "4 %d" % i
        #����
    #�غϺ���    
    if temDis == 0:
        log('###�˺�')
        return "7 %d" % GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)[0]
    
    # ʹ��flipper
    if GW.CheckUnitBuff(UH, 'Fast') == 0:
        return "4 4"
                       
    # �������δ�� ҧ��
    # ����Ҫ��mindis����,�ҽǶ�Ҫ�����ܹ����ٵĽǶ�
    if temDis <= MinDis and (temDis >= MaxDis) and (dirCos < math.cos(math.radians(l[2]))) :
        log(temMinDir)
        result = math.fabs(temMinDir) 
        if result > 180:
            result = 360 - result
            
        if math.sin(math.radians(temMinDir)) > 0:
            log("$$$$��ת", 1)
            return "1 %d" % min(RollValue, int(result))
        else:
            log("$$$$��ת", 1)
            return "2 %d" % min(RollValue, int(result))
        
    # ����̫Զ,���ƶ�������ĵ����Ա� ����40-570��          
    log("##########move to ���������") 
    if len(clist) > 0:
        near = clist[0]
        nearInfo = clist[0][3]
        if near[0] > MinDis:
            return Move(selfInfo, nearInfo.PosX, nearInfo.PosY)
        if near[0] < MaxDis:
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
                    return "4 %d" % i
        #�����Ͼ�δ����,�����м��ƶ�   
        return Move(selfInfo, width, height)         
  
# boomTime��,�޶�info��λ��
# ��һ�������������ڸ���ת��תȥ,��һ��
def SetFuturePox(info, boomTime):
    global posDict
    #��һ�γ���
    if not posDict.has_key(info.Handle):
        posDict.update({info.Handle:(info.PosX, info.PosY)})
        return
    
    
    (lx, ly) = posDict[info.Handle]

    dir = info.MoveSpeed
    x = info.PosX
    y = info.PosY
    
    # δ����λ��
    #info.PosX = max(0, int(boomTime * (x - lx) / 100 + x))
    #info.PosY = max(0, int(boomTime * (y - ly) / 100 + y))
    # ���浱ǰλ��
    posDict.update({info.Handle:(x, y)})
         
#�ƶ���ĳ��
# С��25���ƶ�
# ����25С��45 ת��
def Move(selfinfo, x, y):
    sx = selfinfo.PosX
    sy = selfinfo.PosY
    
    degress = GetDegressByXY(x - sx, y - sy) # ����ָ��Ŀ���ʸ������
    dir = (GetDegress(selfinfo.Dir) - degress + 180) % 360
    
    MoveValue, tt = GetBestMoveAndDir(selfinfo, Def_Max_AI_Tick)
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        return "7 %d" % MoveValue  # ����
    if dir > 45 and dir < 135:
        return "5 %d" % MoveValue   # ����    
    if dir >= 135 and dir < 225:
        return "3 %d" % MoveValue  # ǰ��
    if dir >= 225 and dir < 315:
        return "6 %d" % MoveValue   # ���ƶ�
                    
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
    # ���˵Ŀ�߱�ԽС,����Ҫ��׼�ĽǶ�ԽҪ��ȷ
#    if panduan < 25: 
#        tanValue = (target.BodyWidth + target.BodyHeight) * 2 / (6 * dis)
#    elif panduan < 40: 
#        tanValue = (target.BodyWidth + target.BodyHeight) * 2 / (5 * dis)
#    elif panduan < 55: 
#        tanValue = (target.BodyWidth + target.BodyHeight) * 2 / (4 * dis)
#    elif panduan < 70: 
#        tanValue = (target.BodyWidth + target.BodyHeight) * 2 / (3 * dis)
#    else:
#        tanValue = (target.BodyWidth + target.BodyHeight) * 2 / (2 * dis)
    if dis != 0:
        tanValue = (5) * 2 / (2 * dis)
    else:
        tanValue = 999
    #log("#######panduan: " + str(panduan))
    degrees = math.degrees(math.atan(tanValue))
    #log('####����ĽǶ�:' + str(degrees))                 
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
    Dis = int(AiTick / selfInfo.MoveSpeed)
    Dir = int(AiTick / selfInfo.RollSpeed)

    return Dis, Dir

def ShanBi(selfInfo, Info):
    selfDir = selfInfo.Dir
    dd, enemyDir = GetDisAndDir(Info, selfInfo) #���˳����ҵķ���
    infoDir = Info.Dir  #�����Լ��ķ���
    MoveValue, tt = GetBestMoveAndDir(selfInfo, Def_Max_AI_Tick)
    
    dir = (selfDir - enemyDir) % 360 
    if (dir >= 0 and dir <= 45) or (dir >= 315 and dir <= 360):
        return "7 %d" % MoveValue  # ����
    if dir > 45 and dir < 135:
        return "5 %d" % MoveValue   # ����    
    if dir >= 135 and dir < 225:
        return "3 %d" % MoveValue  # ǰ��
    if dir >= 225 and dir < 315:
        return "6 %d" % MoveValue   # ���ƶ�

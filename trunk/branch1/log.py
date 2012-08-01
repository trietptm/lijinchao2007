#coding:gbk
import logging

# 1 日志都在AllLog.txt
# 0 日志分开
mode = 1

if mode:   
    hdLog = logging.FileHandler('AllLog.txt')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdLog.setFormatter(formatter)
else:
    ErrLog = logging.FileHandler('ErrLog.txt')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    ErrLog.setFormatter(formatter)
    
    Log = logging.FileHandler('Log.txt')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    Log.setFormatter(formatter)
    
log = logging.getLogger()
log.addHandler(hdLog)
log.setLevel(logging.NOTSET)

def ErrLog(*argv):
    log.error(GetMsg(argv))
    

def Log(*argv):
    log.info(GetMsg(argv))
    
        
def GetMsg(msgs):
    result = ""
    result += " : ("
    for a in msgs:
        result += str(a) + ","
    result += ")"
    return result

  
#coding:gbk
#mongo������

#@verson=1.0

#------------------------------------------------
import log
import time
import copy
import pymongo
#------------------------------------------------
# ȫ�ֱ���
Log = log.Log
ErrLog = log.ErrLog

DBName = "test"
#------------------------------------------------
def DecodeDict(unicodeDict):
    # ת���ֵ�
    result = {}
    for key, value in unicodeDict.items():
        if not isinstance(value, str):
            result[key.encode("gbk")] = value
        else:
            result[key.encode("gbk")] = value.encode("gbk")
    return result

#------------------------------------------------
class MongoManager():
    
    def __init__(self, dbName = DBName):
        self._db = None
        self._TableDict = {}
        try:
            self._conn = pymongo.Connection(host = "127.0.0.1", port=27017)
        except:
            self._conn = None
            ErrLog("�������ݿ�ʧ��")
            return
        
        if self._conn:
            self._db = self._conn["%s" % dbName]
            
        
    def GetTable(self, tableName):
        if not self._db:
            ErrLog("�������ݿ�ʧ��,�޷�����table")
            return
        
        if self._TableDict.has_key(tableName):
            return self._TableDict[tableName]
        
        tableObj = self._db["%s" % tableName]
        self._TableDict[tableName] = tableObj
        return tableObj
    
    def InsertTableValue(self, tableName, **keysValue):
        tableObj = self.GetTable(tableName)
        
        tableObj.insert(keysValue)
        
        
    def SetTableValue(self, tableName, key, keyValue, **keysValue):
        tableObj = self.GetTable(tableName)
        if not isinstance(key, str):
            ErrLog("���õ���key��Ϊstr")
            return
        
        if not tableObj.find({key:keyValue}).count():
            temDict = {key:keyValue}
            self.InsertTableValue(tableName, **temDict)
            
            
    def GetTableValue(self, tableName, key, keyValue):
        tableObj = self.GetTable(tableName)
        if not isinstance(key, str):
            ErrLog("GetTableValue�������key��Ϊstr")
            return
        
        iter = tableObj.find({key:keyValue})
        if not iter.count():
            return {}
        result = iter[0]
        result.pop("_id")
        result = DecodeDict(result)
        return result
    
    # ������Ч,ɾ��ȫ��
    def RemoveTable(self, tableName, **keysValue):
        if self._TableDict.has_key(tableName):
            print str(keysValue)
            self._TableDict[tableName].remove(**keysValue)
            
            
g_mongoManager = None

def GetMongoManager():
    global g_mongoManager
    if g_mongoManager:
        return g_mongoManager
    g_mongoManager = MongoManager()
    return g_mongoManager

GetMongoManager().SetTableValue("test", "dd", 2, c=3)
GetMongoManager().SetTableValue("test", "d", 2, c=3)
print GetMongoManager().GetTableValue("test", 1, 2)

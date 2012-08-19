#coding:gbk
#用户表  set get 默认开启cache

#@verson=1.0


#------------------------------------------------
import log
import MongoManager
#------------------------------------------------
# 全局变量
Log = log.Log
ErrLog = log.ErrLog
#------------------------------------------------

class PlayerTable():
    
    def __init__(self):
        self._dbManager = MongoManager.GetMongoManager()
        self._tableDict = {}
        self._tableName = "tagPlayer"
        self._key = "PlayerID"
        self._columns = ["sex", "age", "name"]
        self._tableObj = None
        self.ReadTable()
        
        
    def ReadTable(self):
        self._tableObj = self._dbManager.ReadTable(self._key, self._tableName)
        
    def InitPlayer(self, playerID,  **valueDict):
        self._dbManager.SetTableValue(self._tableName, self._key, playerID, **valueDict)
        
    def SetSex(self, playerID,  value):
        temDict = {"sex":value}
        self._dbManager.SetTableValue(self._tableName, self._key, playerID, True, **temDict)
    
    def GetSex(self, playerID):
        return self._dbManager.GetTableValue(self._tableName, self._key, playerID, True)
    
    def SetAge(self, playerID, value):
        pass
    
    def GetAge(self, playerID):
        pass
    
    
    def SetName(self, playerID, value):
        pass
    
    def GetName(self, playerID):
        pass
        

g_playerTable = None

def GetPlayerTable():
    global g_playerTable
    if g_playerTable:
        return g_playerTable
    g_playerTable = PlayerTable()
    return g_playerTable


if __name__ == '__main__':
    GetPlayerTable().SetSex(1, "boy111")
    print GetPlayerTable().GetSex(1)
    print GetPlayerTable().GetSex(2)
    print '**********'
    #MongoManager.GetMongoManager().Save()
#    GetPlayerTable().InitPlayer(2, **{"sex":"boy", "age":18})
#    print GetPlayerTable().GetSex(2)
        
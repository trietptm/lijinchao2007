#coding:gbk
#mongo管理器

#@verson=1.0

#------------------------------------------------
import log
import time
import copy
import pymongo
import GameWorld
#------------------------------------------------
# 全局变量
Log = log.Log
ErrLog = log.ErrLog

# set get 是否开启cache
OpenCache = False

DBName = "test"
#------------------------------------------------
def DecodeDict(unicodeDict):
    # 转换字典
    result = {}
    for key, value in unicodeDict.items():
        if isinstance(value, unicode):
            result[key.encode("gbk")] = value.encode("gbk")
        else:
            result[key.encode("gbk")] = value
    return result

#------------------------------------------------
class MongoManager():
    
    def __init__(self, dbName = DBName):
        self._db = None
        self._TableDict = {}
        self._TableKeyDict = {}
        self._CacheDict = {}
        try:
            self._conn = pymongo.Connection(host = "127.0.0.1", port=27017)
        except:
            self._conn = None
            ErrLog("连接数据库失败")
            return
        
        if self._conn:
            self._db = self._conn["%s" % dbName]
        
        GameWorld.RegisterTimerEx("MongoManager", 10.0, self.Save)
        
    def ReadTable(self, key, tableName):
        tableObj = self.GetTable(tableName)
        tableList = []
        for item in tableObj.find():
            item.pop("_id")
            item["isChange"] = False
            item = DecodeDict(item)
            tableList.append(item)
        print "ReadTable" + repr(tableList)
        self._CacheDict[tableName] = tableList
        self._TableKeyDict[tableName] = key
        
        
    def GetTable(self, tableName):
        if not self._db:
            ErrLog("连接数据库失败,无法创建table")
            return
        
        if self._TableDict.has_key(tableName):
            return self._TableDict[tableName]
        
        tableObj = self._db["%s" % tableName]
        self._TableDict[tableName] = tableObj
        return tableObj
    
    def InsertTableValue(self, tableName, **keysValue):
        tableObj = self.GetTable(tableName)
        
        tableObj.insert(keysValue)
        
        
    def SetTableValue(self, tableName, key, keyValue, isCache = OpenCache, **keysValue):
        if isCache:
            # 读取数据库
            if not self._CacheDict.has_key(tableName):
                self.ReadTable(key, tableName)
                
            for item in self._CacheDict[tableName]:
                if not item.has_key(key):
                    #ErrLog("某列%s 居然没有key:%s " %(item, key))
                    # 是个列表,继续寻找,直到找到
                    continue
                if item[key] == keyValue:
                    item.update(keysValue)
                    item["isChange"] = True
                    #print "SetTableValue" + str(item)
                    return True
            # 此条没有创建过
            item = {}
            item["isChange"] = True
            item[key] = keyValue
            item.update(keysValue)
            print "SetTableValue(create):" + str(item)
            self._CacheDict[tableName].append(item)
            return True
        
        tableObj = self.GetTable(tableName)
        if not isinstance(key, str):
            ErrLog("设置的主key必为str")
            return
        
        if not tableObj.find({key:keyValue}).count():
            temDict = {key:keyValue}
            self.InsertTableValue(tableName, **temDict)
        
        if keysValue.has_key("isChange"):
            keysValue.pop("isChange")
        tableObj.update({key:keyValue}, {"$set":keysValue})
        
        
    def GetTableValue(self, tableName, key, keyValue, isCache = True):
        if isCache:
            # 读取数据库
            if not self._CacheDict.has_key(tableName):
                self.ReadTable(key, tableName)
            for item in self._CacheDict[tableName]:
                if not item.has_key(key):
                    ErrLog("某列%s 居然没有key:" %(item, key))
                    return {}
                if item[key] == keyValue:
                    return item
                return {}
                
        tableObj = self.GetTable(tableName)
        if not isinstance(key, str):
            ErrLog("GetTableValue传入的主key必为str")
            return
        
        iter = tableObj.find({key:keyValue})
        if not iter.count():
            return {}
        result = iter[0]
        result.pop("_id")
        result = DecodeDict(result)
        return result
    
    # 传参无效,删除全部
    def RemoveTable(self, tableName, **keysValue):
        if self._TableDict.has_key(tableName):
            print "RemoveTable" + str(keysValue)
            self._TableDict[tableName].remove(**keysValue)
    
    # 定时保存
    def Save(self):
        print "Save"
        Log("MongoManager.Save")
        for tableName, tableList in self._CacheDict.items():
            keyName = self._TableKeyDict[tableName]
            print "Save" + str(tableList)
            for item in tableList:
                #print "Save" + str(item)
                print keyName
                if item["isChange"]:
                    self.SetTableValue(tableName, \
                                       keyName, item[keyName], False, **item)
            
g_mongoManager = None

def GetMongoManager():
    global g_mongoManager
    if g_mongoManager:
        return g_mongoManager
    g_mongoManager = MongoManager()
    return g_mongoManager

if __name__ == '__main__':
    GetMongoManager().SetTableValue("test", "dd", 2, c="22")
    GetMongoManager().SetTableValue("test", "dd", 3, c=33)
    print GetMongoManager().GetTableValue("test", "dd", 2)

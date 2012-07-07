# coding: gbk
from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    
    def load(self, path_to_exe):
        
        #create_flags = DEBUG_PROCESS
        create_flags = CREATE_NEW_CONSOLE
        
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        startupinfo.cb = sizeof(startupinfo)
        print repr(startupinfo.cb)
        
        command = pointer(c_char(' '))
        for i, value in enumerate(path_to_exe):
            command[i] = value
        command[i + 1] = " "
        #command = None
        if kernel32.CreateProcessA(None,
                                   command,
                                   None,
                                   None,
                                   False,
                                   create_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)
                                   ):
            print " 成功启动id: %d " % process_information.dwProcessId
            
        else:
            print " 失败: 0x%08x " % kernel32.GetLastError()
            
        

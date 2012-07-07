# coding: gbk
from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False
        
        
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
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
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
            # 获取handle
            self.h_process = self.open_process(process_information.dwProcessId)
            
        else:
            print " 失败: 0x%08x " % kernel32.GetLastError()
            
            
    def open_process(self, pid):
        
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return h_process
    
    
    def attach(self, pid):
        
        self.h_process = self.open_process(pid)
        
        # 启动附加
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            self.run()
        else:
            print " 无法附加 "
            
    
    def run(self):
        
        while self.debugger_active:
            self.get_debug_event()
            
    
    def get_debug_event(self):
        
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
#            raw_input("点击继续...")
            print "get_debug_event"
            self.debugger_active = False
            kernel32.ContinueDebugEvent(\
                                        debug_event.dwProcessId, \
                                        debug_event.dwThreadId, \
                                        continue_status)
           
            
    def detach(self):
        
        if kernel32.DebugActiveProcessStop(self.pid):
            print "完成调试.."
            return True
        else:
            print "结束调试错误!"
            return False
      
        
    # 枚举线程
    def enumerate_thread(self):
        
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        
        if snapshot:
            
            # 便利句柄中的线程
            thread_entry.dwSize = sizeof(thread_entry)
            sucess = kernel32.Thread32First(snapshot, byref(thread_entry))
            
            while sucess:
                if thread_entry.th32OwnerProcessID == self.pid:
                    thread_list.append(thread_entry.th32ThreadID)
                sucess = kernel32.Thread32Next(snapshot, byref(thread_entry))
            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            return False
        
    # 获取寄存器信息
    def get_thread_context(self, thread_id=None, h_thread=None):
        
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        
        # 获取线程句柄
        h_thread = self.open_thread(thread_id)
        print "获取的句柄：0x%08x" % h_thread
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            return False
            
            
    
    # 获取线程句柄
    def open_thread(self, thread_id):
        
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        
        if h_thread:
            return h_thread
        else:
            print " 无法获取句柄：threadid： 0x%08x" % thread_id
            return False
            
        

















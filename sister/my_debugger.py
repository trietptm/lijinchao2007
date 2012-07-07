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
            print " �ɹ�����id: %d " % process_information.dwProcessId
            # ��ȡhandle
            self.h_process = self.open_process(process_information.dwProcessId)
            
        else:
            print " ʧ��: 0x%08x " % kernel32.GetLastError()
            
            
    def open_process(self, pid):
        
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return h_process
    
    
    def attach(self, pid):
        
        self.h_process = self.open_process(pid)
        
        # ��������
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            self.run()
        else:
            print " �޷����� "
            
    
    def run(self):
        
        while self.debugger_active:
            self.get_debug_event()
            
    
    def get_debug_event(self):
        
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
#            raw_input("�������...")
            print "get_debug_event"
            self.debugger_active = False
            kernel32.ContinueDebugEvent(\
                                        debug_event.dwProcessId, \
                                        debug_event.dwThreadId, \
                                        continue_status)
           
            
    def detach(self):
        
        if kernel32.DebugActiveProcessStop(self.pid):
            print "��ɵ���.."
            return True
        else:
            print "�������Դ���!"
            return False
      
        
    # ö���߳�
    def enumerate_thread(self):
        
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        
        if snapshot:
            
            # ��������е��߳�
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
        
    # ��ȡ�Ĵ�����Ϣ
    def get_thread_context(self, thread_id=None, h_thread=None):
        
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        
        # ��ȡ�߳̾��
        h_thread = self.open_thread(thread_id)
        print "��ȡ�ľ����0x%08x" % h_thread
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            return False
            
            
    
    # ��ȡ�߳̾��
    def open_thread(self, thread_id):
        
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        
        if h_thread:
            return h_thread
        else:
            print " �޷���ȡ�����threadid�� 0x%08x" % thread_id
            return False
            
        

















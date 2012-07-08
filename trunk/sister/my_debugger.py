# coding: gbk
from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False
        self.debug_event = None
        self.h_thread = None
        self.context = None
        self.exception = None
        
        self.breakpoints = {}
        self.first_breakpoint = True
        self.hardware_breakpoints = {}
        
        
        
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
            #self.run()
        else:
            print " 无法附加 "
            
    
    def run(self):
        
        while self.debugger_active:
            self.get_debug_event()
            
    
    def get_debug_event(self):
        print 
        print "get_debug_event"
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
#            raw_input("点击继续...")
            
            self.h_thread = self.open_thread(debug_event.dwThreadId)
            self.context = self.get_thread_context(h_thread=self.h_thread)
            self.debug_event = debug_event
            print "事件码：%s， 线程id：%s， 进程id：%s" % (debug_event.dwDebugEventCode, debug_event.dwThreadId, debug_event.dwProcessId)
            
            if debug_event.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
                self.exception = debug_event.u.Exception.ExceptionRecord.ExceptionCode
                self.exception_address = debug_event.u.Exception.ExceptionRecord.ExceptionAddress
                
                # call the internal handler for the exception event that just occured.
                if self.exception == EXCEPTION_ACCESS_VIOLATION:
                    print "Access Violation Detected."
                elif self.exception == EXCEPTION_BREAKPOINT:
                    continue_status = self.exception_handler_breakpoint()
                elif self.exception == EXCEPTION_GUARD_PAGE:
                    print "Guard Page Access Detected."
                elif self.exception == EXCEPTION_SINGLE_STEP:
                    self.exception_handler_single_step()
            print "continue thread: %s " % debug_event.dwThreadId
            kernel32.ContinueDebugEvent(\
                                        debug_event.dwProcessId, \
                                        debug_event.dwThreadId, \
                                        continue_status)
        else:
            print "get_debug_event 失败 "
    
    # 处理断点
    def exception_handler_breakpoint(self):
        print "[*] Exception address: 0x%08x" % self.exception_address
        continue_status = DBG_CONTINUE
        # check if the breakpoint is one that we set
        if not self.breakpoints.has_key(self.exception_address):
           
            # if it is the first Windows driven breakpoint
            # then let's just continue on
            if self.first_breakpoint:
                self.first_breakpoint = False
                print "[*] Hit the first breakpoint."
                return DBG_CONTINUE
               
        else:
            print "[*] Hit user defined breakpoint."
            # this is where we handle the breakpoints we set 
            # first put the original byte back
            self.write_process_memory(self.exception_address, self.breakpoints[self.exception_address])

            # obtain a fresh context record, reset EIP back to the 
            # original byte and then set the thread's context record
            # with the new EIP value
            self.context = self.get_thread_context(h_thread=self.h_thread)
            self.context.Eip -= 1
            
            kernel32.SetThreadContext(self.h_thread, byref(self.context))
            
            continue_status = DBG_CONTINUE


        return continue_status
    
     
     
    # 单步断点
    def exception_handler_single_step(self):
        print "[*] Exception address: 0x%08x" % self.exception_address
        # Comment from PyDbg:
        # determine if this single step event occured in reaction to a hardware breakpoint and grab the hit breakpoint.
        # according to the Intel docs, we should be able to check for the BS flag in Dr6. but it appears that windows
        # isn't properly propogating that flag down to us.
        slot = 0
        if self.context.Dr6 & 0x1 and self.hardware_breakpoints.has_key(0):
            slot = 0

        elif self.context.Dr6 & 0x2 and self.hardware_breakpoints.has_key(1):
            slot = 0
        elif self.context.Dr6 & 0x4 and self.hardware_breakpoints.has_key(2):
            slot = 0
        elif self.context.Dr6 & 0x8 and self.hardware_breakpoints.has_key(3):
            slot = 0
        else:
            # This wasn't an INT1 generated by a hw breakpoint
            continue_status = DBG_CONTINUE #DBG_EXCEPTION_NOT_HANDLED

        # Now let's remove the breakpoint from the list
        if self.bp_del_hw(slot):
            continue_status = DBG_CONTINUE

        print "[*] Hardware breakpoint removed."
        return continue_status
    
    
    def bp_del_hw(self, slot):
        
        # Disable the breakpoint for all active threads
        for thread_id in self.enumerate_threads():

            context = self.get_thread_context(thread_id=thread_id)
            
            # Reset the flags to remove the breakpoint
            context.Dr7 &= ~(1 << (slot * 2))

            # Zero out the address
            if   slot == 0: 
                context.Dr0 = 0x00000000
            elif slot == 1: 
                context.Dr1 = 0x00000000
            elif slot == 2: 
                context.Dr2 = 0x00000000
            elif slot == 3: 
                context.Dr3 = 0x00000000

            # Remove the condition flag
            context.Dr7 &= ~(3 << ((slot * 4) + 16))

            # Remove the length flag
            context.Dr7 &= ~(3 << ((slot * 4) + 18))

            # Reset the thread's context with the breakpoint removed
            h_thread = self.open_thread(thread_id)
            kernel32.SetThreadContext(h_thread, byref(context))
            
        # remove the breakpoint from the internal list.
        del self.hardware_breakpoints[slot]

        return True
          
            
    def detach(self):
        
        if kernel32.DebugActiveProcessStop(self.pid):
            print "完成调试.."
            return True
        else:
            print "结束调试错误!"
            return False
      
        
    # 枚举线程
    def enumerate_threads(self):
        
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
        if not h_thread:
            h_thread = self.open_thread(thread_id)
        if h_thread and thread_id:   
            print "thread: %s, 获取的句柄：0x%08x" % (thread_id, h_thread)
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
            
    
    # 读取内存地址
    def read_process_memory(self, address, length):
        
        data = ""
        read_buf = create_string_buffer(length)
        count = c_ulong(0)
        
        
        kernel32.ReadProcessMemory(self.h_process, address, read_buf, 5, byref(count))
        data = read_buf.raw
        
        return data
        
    
    # 写入内存
    def write_process_memory(self, address, data):
        
        count = c_ulong(0)
        length = len(data)
        
        c_data = c_char_p(data[count.value:])

        if not kernel32.WriteProcessMemory(self.h_process, address, c_data, length, byref(count)):
            return False
        else:
            return True
        
    
    # 设置断点
    def bp_set(self, address):
        print "[*] Setting breakpoint at: 0x%08x" % address
        if not self.breakpoints.has_key(address):

            # store the original byte
            old_protect = c_ulong(0)
            kernel32.VirtualProtectEx(self.h_process, address, 1, PAGE_EXECUTE_READWRITE, byref(old_protect))
            
            original_byte = self.read_process_memory(address, 1)
            print "[*] Setting content: %s" % original_byte
            if original_byte != False:
                
                # write the INT3 opcode
                if self.write_process_memory(address, "\xCC"):
                    
                    # register the breakpoint in our internal list
                    self.breakpoints[address] = (original_byte)
                    original_byte1 = self.read_process_memory(address, 1)
                    print "[*] after Setting content at: %s" % repr(original_byte1)
                    return True
            else:
                return False
    
    
    # 解析函数地址
    def func_resolve(self, dll, function):
        
        handle = kernel32.GetModuleHandleA(dll)
        print " msvcrt.handle: 0x%08x" % handle
        address = kernel32.GetProcAddress(handle, function)
        
        kernel32.CloseHandle(handle)
        return address
    

    def bp_set_hw(self, address, length, condition):
        
        # Check for a valid length value
        if length not in (1, 2, 4):
            return False
        else:
            length -= 1
            
        # Check for a valid condition
        if condition not in (HW_ACCESS, HW_EXECUTE, HW_WRITE):
            return False
        
        # Check for available slots
        if not self.hardware_breakpoints.has_key(0):
            available = 0
        elif not self.hardware_breakpoints.has_key(1):
            available = 1
        elif not self.hardware_breakpoints.has_key(2):
            available = 2
        elif not self.hardware_breakpoints.has_key(3):
            available = 3
        else:
            return False

        # We want to set the debug register in every thread
        for thread_id in self.enumerate_threads():
            context = self.get_thread_context(thread_id=thread_id)

            # Enable the appropriate flag in the DR7
            # register to set the breakpoint
            context.Dr7 |= 1 << (available * 2)

            # Save the address of the breakpoint in the
            # free register that we found
            if   available == 0: context.Dr0 = address
            elif available == 1: context.Dr1 = address
            elif available == 2: context.Dr2 = address
            elif available == 3: context.Dr3 = address

            # Set the breakpoint condition
            context.Dr7 |= condition << ((available * 4) + 16)

            # Set the length
            context.Dr7 |= length << ((available * 4) + 18)

            # Set this threads context with the debug registers
            # set
            h_thread = self.open_thread(thread_id)
            kernel32.SetThreadContext(h_thread, byref(context))

        # update the internal hardware breakpoint array at the used slot index.
        self.hardware_breakpoints[available] = (address, length, condition)

        return True














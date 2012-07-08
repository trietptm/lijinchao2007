# coding:gbk
import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
#debugger.load("NOTEPAD")

pid = raw_input("输入pid: ")
debugger.attach(int(pid))

printf_address = debugger.func_resolve("msvcrt.dll", "printf")

print "[*] printf的地址是: 0x%08x" % printf_address

#debugger.bp_set(printf_address)
#debugger.bp_set_hw(printf_address, 1, HW_EXECUTE)

debugger.run()




#threadList = debugger.enumerate_thread()
#
#for thread in threadList:
#    
#    thread_context = debugger.get_thread_context(thread)
#    if thread_context:
#        print "[*] 线程id： 0x%08x " % thread
#        print "[**] EIP:  0x%08x " % thread_context.Eip
#        print "[**] ESP:  0x%08x " % thread_context.Esp
#        print "[**] EBP:  0x%08x " % thread_context.Ebp
#        print "[**] EAX:  0x%08x " % thread_context.Eax
#        print "[**] EBX:  0x%08x " % thread_context.Ebx
#        print "[**] ECX:  0x%08x " % thread_context.Ecx
#        print "[**] EDX:  0x%08x " % thread_context.Edx
#        print 
#    
#debugger.detach()

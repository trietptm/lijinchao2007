# coding:gbk
import my_debugger

debugger = my_debugger.debugger()

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
#debugger.load("NOTEPAD")

pid = raw_input("输入pid: ")
debugger.attach(int(pid))

threadList = debugger.enumerate_thread()

for thread in threadList:
    
    thread_context = debugger.get_thread_context(thread)
    if thread_context:
        print "[*] 线程id： 0x%08x " % thread
        print "[**] EIP:  0x%08x " % thread_context.Eip
        print "[**] ESP:  0x%08x " % thread_context.Esp
        print "[**] EBP:  0x%08x " % thread_context.Ebp
        print "[**] EAX:  0x%08x " % thread_context.Eax
        print "[**] EBX:  0x%08x " % thread_context.Ebx
        print "[**] ECX:  0x%08x " % thread_context.Ecx
        print "[**] EDX:  0x%08x " % thread_context.Edx
        print 
    
debugger.detach()

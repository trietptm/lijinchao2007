# coding:gbk
import my_debugger

debugger = my_debugger.debugger()

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")
#debugger.load("NOTEPAD")

pid = raw_input("����pid: ")
debugger.attach(int(pid))

debugger.detach()

#coding:gbk
#��֤������ʱ��

#@verson=1.0

#------------------------------------------------
import socket, struct, time
#------------------------------------------------
# ȫ�ֱ���
Host = "time.windows.com"
Port = 37
TIME1970 = 2208988800L # 1970-01-01 00:00:00
#------------------------------------------------
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((Host, Port))

t=c.recv(4)
print t
t=struct.unpack("!I", t)
print t

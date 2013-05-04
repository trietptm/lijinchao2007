import socket
import struct, time

HOST="127.0.0.1"
PORT=8888

TIME1970=2208988800L

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

text = s.recv(4)
t = struct.unpack("!I", text)[0]
t = int(t - TIME1970)
print t
s.close()
print "time %s " % time.ctime(t)


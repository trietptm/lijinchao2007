import socket
import struct, time

HOST="127.0.0.1"
PORT=8888

TIME1970=2208988800L

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    print "start accept"
    c, info = s.accept()
    print c, info
    
    t = int(time.time()) + TIME1970
    t = struct.pack("!I", t)
    c.send(t)
    c.close()

s.close()


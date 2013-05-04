import asyncore
import socket
import time, struct

TIME1970=2208988800L

class TimeChanel(asyncore.dispatcher):
    
    def handle_write(self):
        t =  int(time.time()) + TIME1970
        print "send t %s " % t
        t = struct.pack("!I", t)
        self.send(t)
        self.close()
        
        
class TimeServer(asyncore.dispatcher):
    
    def __init__(self, port=8888):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(("", port))
        self.listen(1)
        print "listen port %s " % port
        
    def handle_accept(self):
        channel, info = self.accept()
        TimeChanel(channel)
        
server=TimeServer()
asyncore.loop()

        
        
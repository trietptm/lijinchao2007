import asyncore
import socket, time

TIME1970=2208988800L

class Client(asyncore.dispatcher):
    
    def __init__(self, host, port=8888):
        print "init"
        asyncore.dispatcher.__init__(self)
        print "create_socket"
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        print "connect"
        self.connect((host, port))
        print "end init"
#        
#    def writable(self):
#        print "writable"
#        return 0
#    
#    def handle_connect(self):
#        print "handle_connect"
#        pass
#    
#    def handle_close(self):
#        print "handle_close"
#        self.close()
#        
#    def handle_expt(self):
#        print "handle_expt"
#        print "error1"
#        
    def handle_read(self):
        print "handle_read"
        s = self.recv(4)
        deltatime = ord(s[3]) + (ord(s[2])<<8) + (ord(s[1])<<16) + (ord(s[0])<<24)
        self.DelaWith(deltatime)
        
    def DelaWith(self, deltatime):
        print deltatime
        print time.ctime(deltatime - TIME1970)


clientInstance = Client("127.0.0.1")
asyncore.loop()
raw_input()

import asyncore
import socket
import traceback

class EchoHandler(asyncore.dispatcher):
    
    def handle_read(self):
        data = self.recv(4096)
        if self.connected:
            print " from %s data : %s " % (self.addr, data)
            self.send(data)
        
        
    def handle_close(self):
        print "close 2"
        self.close()
        

        
class EchoServer(asyncore.dispatcher):
    
    def __init__(self, host, port=8888):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(11)
        
        
    def handle_accept(self):
        pair = self.accept()
        if pair == None:
            pass
        else:
            print " connect form %s " % repr(pair[1])
            EchoHandler(pair[0])
            

        
        
server = EchoServer("localhost")
asyncore.loop()


        
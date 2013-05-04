import asyncore
import socket

class Client(asyncore.dispatcher):
    
    def __init__(self, host="localhost", port=8888):
        self.buff = ""
        
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        print asyncore.socket_map
        
    def handle_read(self):
        data = self.recv(4096)
        print data
        self.buff = ""
    
    def handle_write(self):
        self.buff = raw_input()
        if self.buff:
            self.send(self.buff)

    def writable(self):
        if self.buff:
            return False
        else:
            return True

        
         
client= Client()
asyncore.loop()

        

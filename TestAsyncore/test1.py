import asyncore, socket
class http_client(asyncore.dispatcher):
    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 80) )
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self):
        print "handle_connect"
        pass

    def handle_close(self):
        print "handle_close"
        self.close()

    def handle_read(self):
        print "handle_read"
        print self.recv(8192)
    
    def reable(self):
        print "reable"
        return (len(self.buffer) > 0)
    
    def writable(self):
        print "writable"
        return (len(self.buffer) > 0)

    def handle_write(self):
        print "handle_write"
        sent = self.send(self.buffer)

        self.buffer = self.buffer[sent:]

c = http_client('www.python.org', '/')

asyncore.loop()

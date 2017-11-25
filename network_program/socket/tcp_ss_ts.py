#!usr/bin/env python3

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from {}".format(self.client_address))
        self.wfile.write("[{}] {}".format(ctime(), self.rfile.readline()).encode("utf-8"))


tcpsersock = TCP(ADDR, MyRequestHandler)
print("waiting for connection.....")
tcpsersock.serve_forever()

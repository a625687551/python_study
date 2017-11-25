#!usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(ADDR)
tcpsersock.listen(5)

while True:
    print("waiting for connection....")
    tcpclisock, addr = tcpsersock.accept()
    print("...connected from {}".format(addr))

    while True:
        data = tcpclisock.recv(BUFSIZ)
        if not data:
            break
        tcpclisock.send("[{}] {}".format(ctime(), data).encode("utf-8"))
    tcpclisock.close()

tcpsersock.close()  # that is important

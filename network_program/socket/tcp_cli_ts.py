#!usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpclisock = socket(AF_INET, SOCK_STREAM)
    tcpclisock.connect(ADDR)
    data = input("> ")
    if not data:
        break
    tcpclisock.send("{} \n".format(data).encode("utf-8"))
    rec = tcpclisock.recv(BUFSIZ)
    if not rec:
        break
    print(rec.decode("utf-8"))
    tcpclisock.close()

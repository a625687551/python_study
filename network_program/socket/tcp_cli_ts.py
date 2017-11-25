#!usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpclisock = socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(ADDR)

while True:
    data = input("> ")
    if not data:
        break
    tcpclisock.send(data.encode("utf-8"))
    rec = tcpclisock.recv(BUFSIZ)
    if not rec:
        break
    print(rec.decode("utf-8"))
tcpclisock.close()

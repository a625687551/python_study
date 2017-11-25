#!usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpclisock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udpclisock.sendto(data.encode(), ADDR)
    data, addr = udpclisock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)
udpclisock.close()
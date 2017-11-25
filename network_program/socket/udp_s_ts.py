#!usr/bin/env python3

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpsersock = socket(AF_INET, SOCK_DGRAM)
udpsersock.bind(ADDR)

while True:
    print("waiting for message....")
    data, addr = udpsersock.recvfrom(BUFSIZ)
    udpsersock.sendto("[{}] {}".format(ctime(), data).encode(), addr)
    print(".....received from and return to : {}".format(addr))

udpsersock.close()

#!usr/bin/env python3

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TcpserProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print(clnt)
        print("....connected from {}".format(clnt))

    def dataReceived(self, data):
        self.transport.write("[{}] {}".format(ctime(), data).encode())


factory = protocol.Factory()
factory.protocol = TcpserProtocol
print("....waiting for connection ....")
reactor.listenTCP(PORT, factory)
reactor.run()

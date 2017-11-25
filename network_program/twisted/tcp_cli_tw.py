#!usr/bin/env python3

from twisted.internet import protocol, reactor

HOST = "127.0.0.1"
PORT = 21567


class TcpcliProtocol(protocol.Protocol):
    def sendata(self):
        data = input("> ")
        if data:
            print("sending .....{}".format(data))
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendata()

    def dataReceived(self, data):
        print(data)
        self.sendata()


class TcpcliFactory(protocol.ClientFactory):
    protocol = TcpcliProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TcpcliFactory())
reactor.run()
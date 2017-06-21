import socket
import os
import sys
import pickle
import threading
from threading import Thread


class Connection:
    def __init__(self, port, host, name):
        self.name = name
        self.host = host
        self.port = port
        self.messages = []
        self.clients = []


def send():
    while True:
        os.system('clear')
        for message in Conn.messages:
            print message
        print "\ntype \'--exit\' to quit or \'--r\' to refresh"
        print "Type message here: "
        message = raw_input(" ")
        if message == "--exit":
            sys.exit()
        if message == "--r":
            pass
        else:
            send = "%s:  %s" % (Conn.name, message)
            Conn.s.sendto(pickle.dumps(send), (Conn.host, Conn.port))

def main():
    print "Username: "
    option = raw_input('>>> ')
    global Conn
    Conn = Connection(7890, '10.183.1.16', option)
    Conn.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send()


if __name__ == "__main__":
    main()

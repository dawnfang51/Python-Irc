import socket
from client import Connection
import pickle
import errno
import threading
from threading import Thread



def clisten():
    i = 0
    while True:
        s1.listen(1)
        exec("c%i, addr%i = s1.accept()" % (i, i))
        exec("Conn.clients.append(c%i)" % i)
        i+=1

def mlisten():
    while True:
        message = s2.recvfrom(1024)
        send(message[0])


def send(message):
    for client in Conn.clients:
        #Checks to see if client exists
        #If not reader is removed from client list
        try:
            client.send(message)
        except IOError as e:
            if e.errno == errno.EPIPE:
                print "%r is offline" % client



def main():
    global Conn
    Conn = Connection(7890, "10.183.1.16", "main_server")
    #Socket S1 is socket for client prompt (tcp)
    #Message recieving socket
    global s1
    s1 = socket.socket()
    s1.bind((Conn.host, Conn.port))
    print s1
    #Socket S2 is socket for client reader (udp)
    #Message Sending socket
    global s2
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s2.bind((Conn.host, Conn.port))
    Thread(target = mlisten).start()
    Thread(target = clisten).start()



if __name__ == "__main__":
    main()

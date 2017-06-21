import socket
import os
from client import Connection
import time
import threading
from threading import Thread
import pickle

def listen():
    while True:
        messg = Conn.s.recv(1024)
        messg = pickle.loads(messg)
        Conn.messages.append(messg)

def printMessage():
    while True:
        os.system('clear')
        for message in Conn.messages:
            print message
        time.sleep(1)

def main():
    global Conn
    Conn = Connection(7890, '10.183.1.16', "reader")
    Conn.s = socket.socket()
    Conn.s.connect((Conn.host, Conn.port))
    Thread(target = listen).start()
    Thread(target = printMessage).start()

if __name__ == "__main__":
    main()

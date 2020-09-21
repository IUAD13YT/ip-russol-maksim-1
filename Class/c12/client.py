import socket

import threading
import time

shutdown = False
join = False

def receving (name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode ("utF-8"))
                time.sleep (0.2)
        except:
            pass

server = ("localhost", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))

name = input("Name: ")

rt = threading.Thread(target = receving, args=("RecvThread", s))
rt.start()

while not shutdown:
    if not join:
        s.sendto(("([" + name + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input("[You] :: ")
            if message != "":
                s.sendto(("(" + name + "] :: " + message).encode("utf-8"), server)
            time.sleep (0.2)
        except:
            s.sendto(("({" + name + "] <= left chat ") .encode("utf-8"), server)
            shutdown = True

rt.join()
s.close()

s.close()
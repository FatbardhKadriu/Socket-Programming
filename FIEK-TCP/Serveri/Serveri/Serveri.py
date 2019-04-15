from socket import *
from _thread import *
import math 
import random 

serverName = 'localhost'
serverPort = 12000 
serverAddress = (serverName, serverPort)
serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind(serverAddress)
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()

serverSocket.listen(5)

print("**********************************************************************")
print("Projekti i parë në lëndën Rrjeta Kompjuterike\n")
print("\t\t\tPROGRAMIMI ME SOCKET-A")
print("\t\tFIEK - TCP Serveri\n\tFatbardh Kadriu")
print("\nServeri është në pritje të lidhjeve")
print("\n**********************************************************************")


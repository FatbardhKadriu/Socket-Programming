import socket
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

def BASHKETINGELLORE(text):
    bashketingelloret=['b','B','c','C','Ç','ç','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','x','X','z','Z']
    noOfCons = 0 
    for char in k:
        if(char in bashketingelloret):
            noOfCons = noOfCons + 1
    return noOfCons

def PRINTIMI(text):
    text = (str(text)).strip()
    return text

def EMRIIKOMPJUTERIT():
    return socket.gethostname()

def LOJA():
    RandomNumbers = ""
    for x in range(1,8):
        randomNo = random.randint(1,49)
        RandomNumbers += str(randomNo) + " "
    return RandomNumbers

def FIBONACCI(no):
    a = 1 
    b = 1
    for i in range(2, no):
        f = a + b
        a = b
        b = f 
    return f

def KONVERTIMI(choice, value):
    if(choice == 'KilowattToHorsepower'):
        results = value / 0.745699872
    elif(choice == 'HorsepowerToKilowatt'):
        results = value * 0.745699872
    elif(choice == 'DegreesToRadians'):
        results = value * (math.pi / 180)
    elif(choice == 'RadiansToDegrees'):
        results = value * (180 / math.pi)
    elif(choice == 'GallonsToLiters'):
        results = 3.785 * value
    elif(choice == 'LitersToGallons'):
        results = 0.264 * value
    else:
        results = "Gabim!\n\t\tJepni nje nga opsionet e mundshme"
    return results




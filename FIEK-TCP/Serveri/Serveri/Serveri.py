import socket 
from _thread import *
import math 
import random 
import os 
import sys 

serverName = 'localhost'
serverPort = 12000 
serverAddress = (serverName, serverPort)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

def IPADRESA():
    return socket.gethostbyname(EMRIIKOMPJUTERIT())

def BASHKETINGELLORE(text):
    bashketingelloret=['b','B','c','C','Ç','ç','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','x','X','z','Z']
    noOfCons = 0 
    for character in text:
        if(character in bashketingelloret):
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

def ThreadFunction(connection):
    while True:
        try:
            data = connection.recv(128).decode()
        except socket.error:
            print("E dhena nuk eshte pranuar!")
            break

        list = str(data).rsplit(" ")
        line = ""
        lengthOfList = len(list)
        for words in range(1, i):
            line += list[words]
            if(words != lengthOfList):
                line = line + " "
        if not data:
            break
        elif((list[0] == "IPADRESA") or (list[0] == "ipadresa")):
            data = "IP Adresa e klientit është "+IPADRESA()
        elif((list[0] == "BASHKETINGELLORE") or (list[0] == "bashketingellore")):
            data = "Teksti i pranuar përmban " + str(BASHKETINGELLORE(line))+" bashketingellore"
        elif((list[0] == "PRINTIMI") or (list[0] == "printimi")):
            data = "Fjalia që keni shtypur -> " + str(PRINTIMI(line))
        elif((list[0] == "EMRIIKOMPJUTERIT") or (list[0] == "emriikompjuterit")):
            try:
                data = "Emri i klientit është " + EMRIIKOMPJUTERIT()
            except socket.error:
                data = "Emri i klientit nuk mund të gjendet!"
        elif((list[0] == "LOJA") or (list[0] == "loja")):
            data = "7 numrat e gjeneruar rastësisht nga [1-49] janë : " + LOJA()
        elif((list[0] == "FIBONACCI") or (list[0] == "fibonacci")):
            try:
                line = int(get[1])
            except Exception:
                break
            data = "FIBONACCI : " + str(FIBONACCI(line))
        elif((list[0] == "KONVERTIMI") or (list[0] == "konvertimi")):
            nr = float(list[2])
            data = "Vlera e fituar është : "+str(KONVERTIMI(list[1],nr))
        else:
            data = "Serveri nuk ka përgjigje për këtë kërkesë!"
        connection.send(data.encode())
    connection.close()

i = 1 
while(i == 1):
    connection, address = serverSocket.accept()
    print("Serveri është lidhur me klientin me IP Adresë %s, në portin %s" % address)
    start_new_thread(ThreadFunction,(connection,))

serverSocket.close()


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
        for ch in text:
            if(ch in bashketingelloret):
                noOfCons = noOfCons + 1
        return noOfCons

def PRINTIMI(text):
    text=(str(text)).strip()
    return text

def EMRIIKOMPJUTERIT():
    return socket.gethostname()

def KOHA():
    from time import gmtime, strftime
    ActualTime = strftime("%d.%m.%Y %I:%M:%S %p")
    return ActualTime

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
        f = a + b;
        a = b 
        b = f;
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
            print("Të dhënat nuk janë dërguar në server!")
            break
        
        listOfWords = str(data).rsplit(" ")
        line = ""
        lengthOfList = len(listOfWords)
        for words in range(1, lengthOfList):
            line += listOfWords[words]
            if(words!=lengthOfList):
                line += " "
        if not data:
            break
        elif((listOfWords[0] == "IPADRESA") or (listOfWords[0] == "ipadresa")):
            data="IP Adresa e klientit eshte : " + IPADRESA()
        elif((listOfWords[0] == "NUMRIIPORTIT") or (listOfWords[0] == "numriiportit")):
            data="Klienti eshte duke perdorur portin " + str(address[1])
        elif((listOfWords[0] == "BASHKETINGELLORE") or (listOfWords[0] == "bashketingellore")):
            data="Teksti i pranuar permban " + str(BASHKETINGELLORE(line)) +" bashketingellore"
        elif((listOfWords[0] == "PRINTIMI") or (listOfWords[0] == "printimi")):
            data="Fjalia qe keni shtypur -> " + str(PRINTIMI(line))
        elif((listOfWords[0] == "KOHA") or (listOfWords[0] == "koha")):
            data = "\t" + KOHA()
        elif((listOfWords[0]=="EMRIIKOMPJUTERIT") or (listOfWords[0]=="emriikompjuterit")):
            try:
                data="Emri i klientit eshte " + EMRIIKOMPJUTERIT()
            except socket.error:
                data="Emri i kompjuterit nuk mund te gjendet!"
        elif((listOfWords[0] == "LOJA") or (listOfWords[0] == "loja")):
            data="7 numrat e gjeneruar rastesisht prej [1-49] jane : " + LOJA()
        elif((listOfWords[0] == "FIBONACCI") or (listOfWords[0] == "fibonacci")):
                line = int(listOfWords[1])
                data="FIBONACCI : " + str(FIBONACCI(line))
        elif((listOfWords[0] == "KONVERTIMI") or (listOfWords[0] == "konvertimi")):
            try:
                number = float(listOfWords[2])
            except socket.error:
                break
            data="Vlera e fituar eshte : " + str(KONVERTIMI(listOfWords[1], number))

        else:
            data="Serveri nuk mund t'i pergjigjet kesaj kerkese!"
        connection.send(data.encode())
   connection.close()

i = 1 
while(i == 1):
    connection, address = serverSocket.accept()
    print("Serveri është lidhur me klientin me IP Adresë %s, në portin %s" % address)
    start_new_thread(ThreadFunction,(connection,))

serverSocket.close()


import socket 
from _thread import *
import math 
import random 
import sys


serverName = 'localhost'
serverPort = 12000 
serverAddress = (serverName, serverPort)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    serverSocket.bind(serverAddress)
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()


print("**********************************************************************")
print("Projekti i parë në lëndën Rrjeta Kompjuterike\n")
print("\t\t\tPROGRAMIMI ME SOCKET-A")
print("\t\tFIEK - UDP Serveri\n\tFatbardh Kadriu")
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


def FAKTORIELI(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def SHPERNDARJA(k,n,p):
    if(p>1):
        return "Nuk mund te jete probabiliteti me i madh se 1"
    elif(p<0):
        return "Probabiliteti nuk mund te jete negativ"
    elif(k>n):
        return "n duhet te jete me i madh se k"
    else:
        return (FAKTORIELI(n)/(FAKTORIELI(k)*FAKTORIELI(n-k)))*math.pow(p,k)*math.pow(1-p,n-k)

def ASCII(s):
    l1 = [c for c in s]
    l2 = [ord(c) for c in s]
    return "\t\t\t" + str(l1) + "\n\t\t\t" + str(l2)

def ThreadFunction(input, address):
        try:
            data  = input.decode() 
        except socket.error:
            print("Të dhënat nuk janë dërguar në server!")
        
        getData = str(data)
        listOfWords = getData.rsplit(" ")
        line = ""
        lengthOfList = len(listOfWords)
        for words in range(1, lengthOfList):
            line += listOfWords[words]
            if(words!=lengthOfList):
                line += " "
        if not data:
            return
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
                data = "FIBONACCI : " + str(FIBONACCI(line))
        elif((listOfWords[0] == "KONVERTIMI") or (listOfWords[0] == "konvertimi")):
            try:
                number = float(listOfWords[2])
            except socket.error:
                return
            data="Vlera e fituar eshte : " + str(KONVERTIMI(listOfWords[1], number))
        elif((listOfWords[0] == "SHPERNDARJA") or listOfWords[0] == "shperndarja"):
            k = int(listOfWords[1])
            n = int(listOfWords[2])
            p = float(listOfWords[3])
            data = "Shperndarja binomiale : " + str(SHPERNDARJA(k, n, p))
        elif((getData[0:6] == ("ascii"+" ")) or (getData[0:6] == ("ASCII"+" "))):
            l1 = getData[6:]
            data = "ASCCI List ->\n" + ASCII(l1)
        else:
            data = "Serveri nuk mund t'i pergjigjet kesaj kerkese!"
        serverSocket.sendto(data.encode(), address)

while True:
    data, address = serverSocket.recvfrom(128)
    print("Klienti me IP Adresë %s, i cili po përdor portin %s," % address)
    print("ka bërë kërkesën",data.decode())
    start_new_thread(ThreadFunction,(data, address,))

serverSocket.close()


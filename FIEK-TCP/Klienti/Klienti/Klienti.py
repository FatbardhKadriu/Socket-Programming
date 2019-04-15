from socket import *

serverName = 'localhost'
port = 12000
addr = (serverName, port)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(addr)

print("**********************************************************************")
print("Projekti i parë në lëndën Rrjeta Kompjuterike\n")
print("\t\t\tPROGRAMIMI ME SOCKET-A")
print("\t\tFIEK - TCP Klienti\n\tFatbardh Kadriu")
print("\n**********************************************************************")
print("Më poshtë janë paraqitur opsionet e mundshme\n")
print("IPADRESA")
print("NUMRIIPORTIT")
print("BASHKETINGELLORE{hapesire}tekst")
print("PRINTIMI{hapesire}tekst")
print("EMRIIKOMPJUTERIT")
print("KOHA")
print("LOJA")
print("FIBONACCI")
print("KONVERTIMI{hapësirë}Opsioni{hapësirë}Numër")
print("Opsionet jane:\n\t\tKilowattToHorsepower\n\t\tHorsepowerToKilowatt\n\t\tDegreesToRadians\n\t\tRadiansToDegrees\n\t\tGallonsToLiters\n")
print("\n**********************************************************************")
print("Shtyp 'shkyqu' apo ENTER nëse dëshironi të shkyçeni nga serveri\n")
print("**********************************************************************")


request = input("Jepni kerkesen tuaj : ")
i = 1 
while(i == 1):
    clientSocket.send(request.encode())
    data = clientSocket.recv(128).decode()
    print(data)
    if (request == "SHKYQU"):
        i = 2 
    request = input("Jepni kerkesen tuaj : ")


clientSocket.close()



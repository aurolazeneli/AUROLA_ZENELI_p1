import socket

serverName = input('Ndryshoni emrin e serverit ose do te nenkuptohet(localhost): ')
serverPort = input('Ndryshoni portin e serverit ose do te nenkuptohet(13000): ')

if(serverName == ''):
    serverName = 'localhost'
if(serverPort == ''):
    serverPort = 13000
else:
    try:
        serverPort = int(serverPort)
    except:
        print("Porti duhet te jete numer i plote")

ClientSocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ClientSocket.connect((serverName,serverPort))
while True:
    req = input('Jeni lidhur me serverin, shkruani kerkesen tuaj: ')
    if(len(req)>128):
        print('Keni kaluar kufirin e 128 byte-ve')
        continue
    elif(req == ""):
        continue
    ClientSocket.sendall(str.encode(req))

    res=ClientSocket.recv(128).decode()

    print('Te dhenat nga serveri: ',str(res))



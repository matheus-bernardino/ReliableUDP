import socket, pickle, time, random

class Payload:
    data = ''
    tcpSyn = 1
    seqNumber = 0
    ackNumber = 0

serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", serverPort))
initialTime = time.time()
while 1:
    if(time.time() - initialTime > 0.1):
        initialTime = time.time()
        time.sleep(random.uniform(0, 1))
    message, clientAdr = serverSocket.recvfrom(4096)
    packet = pickle.loads(message)
    #mdfMessage = pickle.loads(message)
    payload = Payload()
    if payload.tcpSyn == 1:
        payload.tcpSyn = 1
        payload.ackNumber = packet.seqNumber + 1
        payload.seqNumber = 5
    #print(mdfMessage.data)
    #mdfMessage.data = mdfMessage.data.upper():
    serverSocket.sendto(pickle.dumps(payload), clientAdr)
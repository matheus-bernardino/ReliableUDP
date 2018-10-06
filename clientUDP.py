import socket, pickle, time

class Payload:
    data = ''
    tcpSyn = 1
    seqNumber = 0
    ackNumber = 0

class Connection:
    def establishConnection(self, serverName, serverPort):
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = Payload()
            payload.tcpSyn = 1
            payload = pickle.dumps(payload)
            rtt = 0.001
            initialTime = time.time()
            while 1 and (time.time() - initialTime < 5):
                start = time.time()
                clientSocket.sendto(payload, (serverName, serverPort))
                clientSocket.settimeout(rtt)
                try:
                    mdfMessage, serverAdr = clientSocket.recvfrom(4096)
                except:
                    mdfMessage = None

                if mdfMessage is not None:
                    return True, pickle.loads(mdfMessage).ackNumber, pickle.loads(mdfMessage).seqNumber + 1
                    #print (pickle.loads(mdfMessage).data)
                else:
                    print ('Timeout')
                rtt = time.time() - start
                print (rtt)
            return False

serverName = 'localhost'
serverPort = 12000
connection = Connection()
tryConnection = connection.establishConnection(serverName, serverPort)
print('Conexão estabelecida' if tryConnection != False else 'Conexão falhou')
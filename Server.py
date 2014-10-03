#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

print 'The server is ready to received'
#Prepare a sever socket
#Fill in start
#Fill in end
host = 'localhost'
port = 8000
serverSocket.bind((host, port))
serverSocket.listen(1)
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    print 'connected from',addr
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    try:
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end
        print 'IOError'
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 NOT FOUND \r\n\r\n')
        connectionSocket.send('file not found')
        #Close Client socket
        connectionSocket.close()
serverSocket.close()
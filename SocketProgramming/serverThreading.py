#import socket module
from thread import *
from socket import *



#Prepare a sever socket
#Fill in start
#Fill in end
host = 'localhost'
#port = 8008
def serv(port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(1)
    print 'The server is ready to receive'
    while True:
        #Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
        #print 'connected from',addr
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        try:
            #start_new_thread(serv, port + 1)
            message = connectionSocket.recv(1024)#Fill in start #Fill in end
            start_new_thread(serv, (port + 1,))
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
start_new_thread(serv, (8000,))



while True:
    pass

#while True:
    #wait to accept a connection - blocking call
    #conn, addr = serverSocket.accept()
    #print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    #start_new_thread(serv ,(conn, port))

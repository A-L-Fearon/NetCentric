from socket import *
import sys
import thread

#create a server
def check_sever(new_port, port):
    if new_port:
        thread.start_new_thread(new_server, (port + 1, True))
    else:
        return False

def new_server(port, new_server):
    serversocket = socket(AF_INET, SOCK_STREAM)

    print 'The server is ready to received'
    #Prepare a sever socket
    #Fill in start
    #Fill in end
    host = 'localhost'
    port = 8000
    serversocket.bind((host, port))
    serversocket.listen(1)
    while True:
        #Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serversocket.accept() #Fill in start #Fill in end
        print 'connected from',addr
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        try:
            message = connectionSocket.recv(1024)#Fill in start #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()#Fill in start #Fill in end
            #Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
            #Fill in start
            #Fill in end
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
            new_server(port, check_sever())
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
    serversocket.close()





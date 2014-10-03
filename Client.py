from socket import *
serverName = 'localhost'#'172.16.189.122'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#sentence = raw_input('Input lowercase sentence:')
test = 'GET /hello.html ' + 'HTTP/1.1' #+ sentence
print test
clientSocket.send(test)
response = clientSocket.recv(1024)
print response
if response.split()[1] == '200':
    while not '</html>' in response:
        response = clientSocket.recv(1024)
        print response
        #if '</html>' in response:
        #    break

    #print 'From Server: \n' + response
    clientSocket.close()
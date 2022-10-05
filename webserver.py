#Joseph Kahale
#CS3800.01
#4 October 2022


#import socket module 
from socket import * 
import sys # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket 

serverPort = 6789

serverSocket.bind((''.encode(), serverPort))
serverSocket.listen(1)
print('The server is ready to recieve')
#Fill in end 
while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()           
    try: 
        message = connectionSocket.recv(1024).decode()            
        filename = message.split()[1]                  
        f = open(filename[1:])
        outputdata = f.read()            
        #Send one HTTP header line into socket 
        connectionSocket.send('HTTP/1.1 200 OK'.encode())
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError: 
        #Send response message for file not found 
        #Fill in start       
        connectionSocket.send('HTTP/1.1 404 Not Found'.encode())

        #Fill in end 
        #Close client socket 
        #Fill in start 
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        #Fill in end             
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data    
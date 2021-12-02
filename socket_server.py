#Import socket library for socket programming capabilities
import socket
#Creating a socket
serverSocket = socket.socket()
print("Socket created successfully")
#reserve a port 
port =12345
#bind socket to IP address & port number
serverSocket.bind(('localhost', port))
# change status to listening to wait for client connection
# 5 --> number of clients that can connect to server
serverSocket.listen(5)
print("Socket server listening !!")

while True:
   #accept connection from client , save IP address of client
   connection , addr = serverSocket.accept()
   print("Connected to ", addr)
   # send message to client
   connection.send("Thank you !!".encode())
   # terminate communication
   connection.close()
   # break while loop
   break 

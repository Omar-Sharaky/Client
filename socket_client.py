import socket
clientSocket = socket.socket()
port =12345
select=int(input(" 1:connect to Local Host, 2 connect tp anotehr custom Ip"))
if select==1:
    clientSocket.connect(('localhost', port))
if select==2:
    IP=input("enter Ip:")
    clientSocket.connect((IP, port))
print(clientSocket.recv(1024).decode())
clientSocket.close()
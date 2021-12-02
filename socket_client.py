import socket
clientSocket = socket.socket()
port =12345
clientSocket.connect(('localhost', port))
print(clientSocket.recv(1024).decode())
clientSocket.close()
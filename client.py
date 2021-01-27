import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.connect((host,port))
sock.send(bytes('mesage from the client','utf-8'))

print(sock.recv(2048))
sock.close()

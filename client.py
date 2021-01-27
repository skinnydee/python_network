import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.connect((host,port))

print(sock.recv(2048))
sock.close()

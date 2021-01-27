import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.bind((host,port))

print("waiting for connection")
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("Got connection from ", addr)
    conn.send(bytes("this is the server",'utf-8'))
    conn.close()

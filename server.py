import socket

sock = socket.socket()
host = socket.gethostname()
port = 9999

sock.bind((host,port))
sock.listen(5)
print("waiting for connection")
conn, addr = sock.accept()
print("Got connection from ", addr)


while True:
    data = conn.recv(2048)
    print(data)
    if not data: break
    conn.send(bytes(data))
    conn.send(bytes("this is a server",'utf-8'))
    #conn.send(bytes('unable to recieve data','utf-8'))
conn.close()

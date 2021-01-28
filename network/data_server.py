import socket

host = socket.gethostname()
port = 6000

sock = socket.socket()
sock.bind((host,port))
sock.listen(5)

conn, addr = sock.accept()

print('connected to ', addr)

while True:
    data = conn.recv(1024)
    print(data)
    data1 = str(data)
    result = int(data1[2]) + int(data1[4])
    conn.send(bytes(str(result),'utf-8'))
conn.close()



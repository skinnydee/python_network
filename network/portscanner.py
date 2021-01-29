import socket

host = socket.gethostbyname('www.tutorialspoint.com')
print(host)
ip = host

sock = socket.socket()

while 1:
    try:
        port = input("Enter the port")
        sock = socket.socket()
        sock.connect((host,port))
        print("Port {}: open " .format(port))            
        sock.close()
    except:     
        print("ort {}: closed " .format(port))
print("Port scanning complete")

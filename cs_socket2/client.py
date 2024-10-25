import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 8898))
sk.send(b'hello!')
ret = sk.recv(1024)
print(1024)
sk.close()
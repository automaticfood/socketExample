import socket
import time

COD = 'utf-8'
HOST = socket.gethostname()
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)
SIZE = 10

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(SIZE)

while True:
    print("服务器启动，监听客户端链接")
    conn, addr = serversocket.accept()
    print("链接的客户端", addr)
    while True:
        try:
            data = conn.recv(BUFSIZ)
            if not data:
                break
        except Exception:
            print("断开的客户端", addr)
            break
        else:
            print("客户端发送的内容", data.decode(COD))
        msg = time.strftime("%Y-%m-%d %X")
        msg_send = '[{}]:{}'.format(msg, data.decode(COD))
        conn.send(msg_send.encode(COD))
    conn.close()
serversocket.close()

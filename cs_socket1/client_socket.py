import socket

# HOST = socket.gethostname()
HOST = "113.219.237.106"
PORT = 64482
BUFSIZ = 1024
ADDR = (HOST, PORT)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(ADDR)

while True:
    print("连接成功")
    data_send = input("请输入：").strip()
    if not data_send:
        break
    else:
        clientsocket.send(data_send.encode("utf-8"))
    
    data_recive = clientsocket.recv(BUFSIZ)
    if not data_recive:
        break
    else:
        print(data_recive.decode("utf-8"))
clientsocket.close()
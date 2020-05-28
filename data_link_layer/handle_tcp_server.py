import socket

server = socket.socket(type=socket.SOCK_STREAM)
address = "127.0.0.1"
port = 1234
server.bind((address, port))
print("Tcp服务器已经启动")
server.listen(128) #最大连接数
new_client, client_address = server.accept() #就收客户端连接
print(client_address[0],client_address[1])
data = new_client.recv(1024)
print(data.decode())
new_client.send("hhhh".encode())
new_client.close()
server.close()
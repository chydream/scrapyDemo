import socket

client = socket.socket(type=socket.SOCK_STREAM)
client.connect(("127.0.0.1", 1234))
client.send("你好".encode('utf-8'))
recv_data = client.recv(1024)
print(recv_data.decode())
client.close()
import socket

# 创建socket 指定类型UDP
server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 1234))
data, address = server.recvfrom(1024) #返回客户端信息
print(address[0], address[1], data.decode('utf-8'))
server.sendto("好好学习，天天向上".encode(), address)
server.close()
import socket

client = socket.socket(type=socket.SOCK_DGRAM)
send_data = input("请输入需要发送的数据：")
client.sendto(send_data.encode(), ('127.0.0.1', 1234))
client_data, address = client.recvfrom(1024)
print('服务器回复的数据{}'.format(client_data.decode('utf-8')))
client.close()
import socket

client = socket.socket(type=socket.SOCK_DGRAM)
nickname = input("请输入你的网名：")
while True:
    send_data = input("请输入需要发送的数据：")
    if send_data == 'quit':
        send_data = "已下线"
        client.sendto((nickname+"#"+send_data).encode(), ('127.0.0.1', 1234))
        break
    else:
        client.sendto((nickname+"#"+send_data).encode(), ('127.0.0.1', 1234))
        client_data, address = client.recvfrom(1024)
        data = client_data.decode().split("#")
        print(data[0]+"说："+data[1])
client.close()
import socket
import multiprocessing

def handle_client(client):
    #接收客户端数据
    client_request_data = client.recv(1024)
    print("客户端的请求数据为：{}".format(client_request_data))
    # 响应客户端数据，根据规范
    # 状态行： 包含 HTTP 协议版本、状态码和状态描述，以空格分隔
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = 'Server:My server\r\n'
    response_body = "Hello World"
    response = response_start_line + response_headers + '\r\n' + response_body
    client.send(response.encode("utf-8"))  # 一定要回复二进制数据
    client.close()


if __name__ == '__main__':
    # 创建一个tcp类型的http器
    server = socket.socket(type=socket.SOCK_STREAM)
    server.bind(("", 8080))
    server.listen(128)
    print("WEB服务器已经启动......")
    # 不停的接收客户端的请求
    while True:
        client, address = server.accept() # 接收客户端请求
        print("%s,%s连接上了web服务器"%(address[0], address[1]))
        # 引入多进程，处理客户端的请求
        client_process = multiprocessing.Process(target=handle_client, args=(client,))
        client_process.start() #开启进程
import socket

HOST = '127.0.0.1'  # 服务器的IP地址
PORT = 1881  # 端口号
BUFFER_SIZE = 1024
def Client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
    try:
        client_socket.connect((HOST, PORT))  # 连接到服务器
        print("连接成功")

        # 接收服务器的欢迎消息
        welcome_msg = client_socket.recv(BUFFER_SIZE).decode()
        print("Received:", welcome_msg)

        while True:
            message = input("Enter message (or 'close' to quit): ")
            client_socket.send(message.encode())  # 发送消息给服务器

            if message == "close":
                print("Closing connection...")
                break

            response = client_socket.recv(BUFFER_SIZE).decode()  # 接收服务器的响应
            print("Server response:", response)

    except ConnectionRefusedError:
        print("连接被拒绝")
    except Exception as e:
        print("发生错误:", str(e))
    finally:
        client_socket.close()  # 关闭套接字

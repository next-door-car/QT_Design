from PyQt5.QtCore import pyqtSignal, QObject
import socket


BUFFER_SIZE=1024
class TCPClient(QObject):
    responseReceived = pyqtSignal(str)  # 信号，用于通知UI收到了服务器响应
    def __init__(self, host, port, parent=None):
        super().__init__(parent)
        self.host = host
        self.port = port
        self.client_socket = None

    def connectToServer(self):
        print(1)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        try:
            self.client_socket.connect((self.host, self.port))  # 连接到服务器
            print("connect success")

            # 接收服务器的欢迎消息
            # welcome_msg = self.client_socket.recv(BUFFER_SIZE).decode()
            # print("Received:", welcome_msg)
            
            while response := self.client_socket.recv(BUFFER_SIZE).decode():
                print("Server response:", response)
                self.responseReceived.emit(response)

                if response == "00000000":
                    break
                elif response == "00000001":
                    break
                elif response == "00000002":
                    break
                elif response == "00000003":
                    break
                elif response == "00000004":
                    break
                elif response == "00000005":
                    break
                elif response == "00000006":
                    break
                elif response == "close":
                    break


        except ConnectionRefusedError:
            print("refused")
        except Exception as e:
            print("error:", str(e))
        finally:
            self.client_socket.close()  # 关闭套接字
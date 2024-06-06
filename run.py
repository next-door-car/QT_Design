import sys
from QTUI import QT2
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from Cilect import TCPClient

def xue(self):
    self.ui.textEdit_2.setStyleSheet("background-color:  black;")
    self.ui.textEdit_8.setStyleSheet("background-color:  black;")
    self.ui.textEdit_9.setStyleSheet("background-color:  black;")
    self.ui.textEdit_15.setStyleSheet("background-color: black;")
    self.ui.textEdit_16.setStyleSheet("background-color: black;")



HOST = "127.0.0.1"  # 服务器的IP地址或主机名
PORT = 1881  # 服务器监听的端口号
connect_flag=0
class MyUI(QMainWindow, QT2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QT2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.tcpClient = TCPClient(HOST, PORT,connect_flag, self)
        self.tcpClient.responseReceived.connect(self.handleResponse)
        self.isTCPClientActive = True  # 新增一个标志位，用于判断是否继续接收响应

    def handleResponse(self, response):
        xue(self)
        if response == "00000001":
            print("change color")
            self.ui.textEdit_2.setStyleSheet("background-color: red;")
        elif response == "00000010":
            print("change color")
            self.ui.textEdit_8.setStyleSheet("background-color: red;")
        elif response == "00000100":
            print("change color")
            self.ui.textEdit_9.setStyleSheet("background-color: red;")
        elif response == "00001000":
            print("change color")
            self.ui.textEdit_15.setStyleSheet("background-color: red;")
        elif response == "00010000":
            print("change color")
            self.ui.textEdit_16.setStyleSheet("background-color: red;")
        elif response == "close":
            print("Closing TCP client")
            self.isTCPClientActive = False  # 设置标志位为False，停止接收响应
            self.tcpClient.client_socket.close()  # 关闭TCP连接

if __name__ == '__main__':
    reseve_array = []
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    mainWindow = MyUI()
    mainWindow.show()
    # 建立与服务器的连接
    while(1):
         mainWindow.tcpClient.connectToServer()
        #  while mainWindow.isTCPClientActive:
         app.processEvents()  # 处理Qt事件循环
         if(connect_flag==1):
             break
         
    sys.exit(app.exec_())

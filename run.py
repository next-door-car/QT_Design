import sys
from QTUI import QT2
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from Cilect import Client

if __name__ == '__main__':
    # 添加如下代码
    # Client()
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = QT2.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
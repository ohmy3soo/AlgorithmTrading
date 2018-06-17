import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.textEdit = QTextEdit()
        self.pushButton = QPushButton('저장')
        '''
        #layout = QVBoxLayout()
        layout = QHBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)
        '''
        # QGridLayout
        layout = QGridLayout()

        self.label1 = QLabel("ID: ")
        self.lineEdit1 = QLineEdit()
        self.pushButton1 = QPushButton("Sign In")
        # 행X열
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
# from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ola mundo")
        butao = QPushButton("Click me")

        self.setFixedSize(QSize(500, 500))
        self.setCentralWidget(butao)

app = QApplication(sys.argv)
janela = Main()
janela.show()


app.exec()

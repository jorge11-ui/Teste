# from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 500))
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)

        # butao = QPushButton("Click me")
        #
        # self.setCentralWidget(butao)
        #
app = QApplication(sys.argv)
janela = Main()
janela.show()
app.exec()

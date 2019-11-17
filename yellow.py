import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):

    def __init__(self):
        self.food = []
        self.initUI()

    def initUI(self):

        self.btn = QPushButton()
        self.btn.move(50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

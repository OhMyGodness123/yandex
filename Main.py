import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_Form


class Example(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.flag = 1

    def initUI(self):
        self.btn.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.runi(qp)
        qp.end()

    def runi(self, qp):
        if self.flag == 1:
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            dia = randint(1, 100)
            qp.drawEllipse(100, 100, dia, dia)
            self.flag = 0

    def run(self):
        self.flag = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

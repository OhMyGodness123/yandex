import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem
import sqlite3
from PyQt5 import uic


class Example(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        self.result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tab.setRowCount(len(self.result))
        self.tab.setColumnCount(len(self.result[0]))
        self.tab.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "молотый/в зернах",
                                            "Вкус", "Цена", "Размер"])
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tab.setItem(i, j, QTableWidgetItem(str(val)))
        self.red.clicked.connect(self.run)
        con.close()

    def run(self):
        self.sec = Second()
        self.close()
        self.sec.show()


class Second(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        self.result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tab.setRowCount(len(self.result))
        self.tab.setColumnCount(len(self.result[0]))
        self.tab.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "молотый/в зернах",
                                            "Вкус", "Цена", "Размер"])
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tab.setItem(i, j, QTableWidgetItem(str(val)))
        self.upd.clicked.connect(self.up)
        print(1)
        self.chan.clicked.connect(self.change)
        print(1)

    def up(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        self.rsult = cur.execute("SELECT * FROM coffee").fetchall()
        self.tab.setRowCount(len(self.rsult))
        self.tab.setColumnCount(len(self.rsult[0]))
        self.tab.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "молотый/в зернах",
                                            "Вкус", "Цена", "Размер"])
        titles = [description[0] for description in cur.description]
        for i, elem in enumerate(self.rsult):
            for j, val in enumerate(elem):
                self.tab.setItem(i, j, QTableWidgetItem(str(val)))

    def adder(self):
        pass

    def change(self):
        for i, elem in enumerate(self.rsult):
            for j, val in enumerate(elem):
                print(j, val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

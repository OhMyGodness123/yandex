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
                if j == 2:
                    print(val)
                    self.tab.setItem(i, j, QTableWidgetItem(
                        cur.execute("SELECT OBJARKA FROM OBJARKA WHERE id = ?", (val,)).fetchone()[0]))
                else:
                    self.tab.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

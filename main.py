from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5 import uic
import sys

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Espresso(QMainWindow):
    def __init__(self):
        super(Espresso, self).__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(561, 447)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.project_model = QSqlTableModel(self)
        self.project_model.select()
        self.tableView.setModel(self.project_model)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        sql = QSqlQuery('''select coffee.ID, sorts.sort as "Сорт", roasting.roasting as "Степень обжарки",
        types.type as "Тип", coffee.volume as "Объём", coffee.cost as "Стоимость", coffee.description as "Описание"
        from coffee
        join sorts on sorts.id = coffee.sorts
        join roasting on roasting.ID = coffee.roasting
        join types on types.ID = coffee.type''', self.db)
        self.project_model.setQuery(sql)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
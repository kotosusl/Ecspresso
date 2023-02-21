from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import sys
import sqlite3
from addEditCoffeeForm import Ui_addEditCoffeeForm
from main_from import Ui_MainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Espresso(Ui_MainWindow):
    def __init__(self):
        super(Espresso, self).setupUi(self)
        self.setFixedSize(561, 490)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../data/coffee.sqlite')
        self.project_model = QSqlTableModel(self)
        self.project_model.select()
        self.tableView.setModel(self.project_model)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.update_table()
        self.add.clicked.connect(self.adding)
        self.refactor.clicked.connect(self.reset)
        self.update_button.clicked.connect(self.update_table)

    def adding(self):
        global IN_FORM
        if not IN_FORM:
            IN_FORM = True
            self.form = AddForm()
            self.form.show()

    def reset(self):
        global IN_FORM
        if not IN_FORM:
            if str(self.tableView.currentIndex().siblingAtColumn(0).data()):
                IN_FORM = True
                self.form = ResetForm(self.tableView.currentIndex().siblingAtColumn(0).data())
                self.form.show()

    def update_table(self):
        sql = QSqlQuery('''select coffee.ID, sorts.sort as "Сорт", roasting.roasting as "Степень обжарки",
                types.type as "Тип", coffee.volume as "Объём", coffee.cost as "Стоимость", 
                coffee.description as "Описание"
                from coffee
                join sorts on sorts.id = coffee.sorts
                join roasting on roasting.ID = coffee.roasting
                join types on types.ID = coffee.type''', self.db)
        self.project_model.setQuery(sql)


class ResetForm(Ui_addEditCoffeeForm):
    def __init__(self, coffee_id):
        super(ResetForm, self).setupUi(self)
        self.setFixedSize(390, 321)
        con = sqlite3.connect('../data/coffee.sqlite')
        self.cur = con.cursor()
        self.coffee_id = coffee_id
        self.sort.addItems([str(p[0]) for p in self.cur.execute('''select sort from sorts''').fetchall()])
        self.roasting.addItems([str(p[0]) for p in self.cur.execute('''select roasting from roasting''').fetchall()])
        self.type.addItems([str(p[0]) for p in self.cur.execute('''select type from types''').fetchall()])
        self.sort.setCurrentText(str(self.cur.execute(f'''select sorts.sort from sorts where sorts.id = 
        (select coffee.sorts from coffee where coffee.id = {coffee_id})''').fetchone()[0]))
        self.roasting.setCurrentText(str(self.cur.execute(f'''select roasting from roasting where roasting.id = 
        (select coffee.roasting from coffee where coffee.id = {coffee_id})''').fetchone()[0]))
        self.type.setCurrentText(str(self.cur.execute(f'''select type from types where types.id = 
        (select coffee.type from coffee where coffee.id = {coffee_id})''').fetchone()[0]))
        self.cost.setValue(self.cur.execute(f'''select coffee.cost from coffee 
                where coffee.id = {coffee_id}''').fetchone()[0])
        self.volume.setValue(self.cur.execute(f'''select coffee.volume from coffee 
                where coffee.id = {coffee_id}''').fetchone()[0])
        self.description.setText(self.cur.execute(f'''select description from coffee 
                where coffee.id = {coffee_id}''').fetchone()[0])
        self.add_button.clicked.connect(self.new_row)

    def new_row(self):
        if (self.sort.currentText(), self.roasting.currentText(), self.type.currentText(), self.volume.value(),
            self.cost.value()) in self.cur.execute('''select sorts.sort, roasting.roasting, types.type,
             coffee.volume, coffee.cost from coffee
                join sorts on sorts.id = coffee.sorts
                join roasting on roasting.ID = coffee.roasting
                join types on types.ID = coffee.type''').fetchall():
            self.statusbar.showMessage('Запись уже существует')
        else:
            self.statusbar.showMessage('')
            sql = f'''update coffee
            set sorts = (select id from sorts where sort = '{self.sort.currentText()}'), 
            roasting = (select id from roasting where roasting = '{self.roasting.currentText()}'),
            type = (select id from types where type = '{self.type.currentText()}'),
            volume = {self.volume.value()}, cost = {self.cost.value()},
            description = '{self.description.toPlainText()}'
            where coffee.id = {self.coffee_id}'''
            self.sqlquery = QSqlQuery()
            self.sqlquery.exec(sql)
            self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        global IN_FORM
        IN_FORM = False


class AddForm(Ui_addEditCoffeeForm):
    def __init__(self):
        super(AddForm, self).setupUi(self)
        self.setFixedSize(390, 321)
        con = sqlite3.connect('../data/coffee.sqlite')
        self.cur = con.cursor()
        self.sort.addItems([str(p[0]) for p in self.cur.execute('''select sort from sorts''').fetchall()])
        self.roasting.addItems([str(p[0]) for p in self.cur.execute('''select roasting from roasting''').fetchall()])
        self.type.addItems([str(p[0]) for p in self.cur.execute('''select type from types''').fetchall()])
        self.add_button.clicked.connect(self.new_row)

    def new_row(self):
        if (self.sort.currentText(), self.roasting.currentText(), self.type.currentText(), self.volume.value(),
            self.cost.value()) in self.cur.execute('''select sorts.sort, roasting.roasting, types.type,
             coffee.volume, coffee.cost from coffee
                join sorts on sorts.id = coffee.sorts
                join roasting on roasting.ID = coffee.roasting
                join types on types.ID = coffee.type''').fetchall():
            self.statusbar.showMessage('Запись уже существует')
        else:
            self.statusbar.showMessage('')
            sql = f'''INSERT INTO coffee(sorts, roasting, type, volume, cost, description) 
            VALUES((select id from sorts where sort = '{self.sort.currentText()}'), 
            (select id from roasting where roasting = '{self.roasting.currentText()}'),
            (select id from types where type = '{self.type.currentText()}'),
            {self.volume.value()}, {self.cost.value()}, '{self.description.toPlainText()}')'''
            self.sqlquery = QSqlQuery()
            self.sqlquery.exec(sql)
            self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        global IN_FORM
        IN_FORM = False


IN_FORM = False
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
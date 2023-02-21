from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 541, 411))
        self.tableView.setObjectName("tableView")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(30, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.refactor = QtWidgets.QPushButton(self.centralwidget)
        self.refactor.setGeometry(QtCore.QRect(220, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.refactor.setFont(font)
        self.refactor.setObjectName("refactor")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(410, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.refactor.setText(_translate("MainWindow", "Изменить"))
        self.update_button.setText(_translate("MainWindow", "Обновить"))

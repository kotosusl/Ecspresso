from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_addEditCoffeeForm(QMainWindow):
    def setupUi(self, MainWindow):
        super(Ui_addEditCoffeeForm, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(240, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.sort = QtWidgets.QComboBox(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(240, 20, 131, 22))
        self.sort.setObjectName("sort")
        self.sort_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sort_label.setFont(font)
        self.sort_label.setObjectName("sort_label")
        self.roasting_label = QtWidgets.QLabel(self.centralwidget)
        self.roasting_label.setGeometry(QtCore.QRect(20, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.roasting_label.setFont(font)
        self.roasting_label.setObjectName("roasting_label")
        self.roasting = QtWidgets.QComboBox(self.centralwidget)
        self.roasting.setGeometry(QtCore.QRect(240, 50, 131, 22))
        self.roasting.setObjectName("roasting")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(240, 80, 131, 22))
        self.type.setObjectName("type")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(20, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.volume = QtWidgets.QSpinBox(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(240, 110, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.volume.setFont(font)
        self.volume.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.volume.setMaximum(1000)
        self.volume.setProperty("value", 100)
        self.volume.setObjectName("volume")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(20, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.volume_label.setFont(font)
        self.volume_label.setObjectName("volume_label")
        self.cost_label = QtWidgets.QLabel(self.centralwidget)
        self.cost_label.setGeometry(QtCore.QRect(20, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cost_label.setFont(font)
        self.cost_label.setObjectName("cost_label")
        self.cost = QtWidgets.QSpinBox(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(240, 140, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cost.setFont(font)
        self.cost.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.cost.setMaximum(10000)
        self.cost.setProperty("value", 100)
        self.cost.setObjectName("cost")
        self.ru_label = QtWidgets.QLabel(self.centralwidget)
        self.ru_label.setGeometry(QtCore.QRect(350, 140, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ru_label.setFont(font)
        self.ru_label.setObjectName("ru_label")
        self.discription_label = QtWidgets.QLabel(self.centralwidget)
        self.discription_label.setGeometry(QtCore.QRect(20, 170, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.discription_label.setFont(font)
        self.discription_label.setObjectName("discription_label")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(240, 170, 131, 81))
        self.description.setObjectName("description")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление кофе"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.sort_label.setText(_translate("MainWindow", "Сорт"))
        self.roasting_label.setText(_translate("MainWindow", "Степень обжарки"))
        self.type_label.setText(_translate("MainWindow", "Тип"))
        self.volume_label.setText(_translate("MainWindow", "Объём"))
        self.cost_label.setText(_translate("MainWindow", "Цена"))
        self.ru_label.setText(_translate("MainWindow", "руб."))
        self.discription_label.setText(_translate("MainWindow", "Описание"))
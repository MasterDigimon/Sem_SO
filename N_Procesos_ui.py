# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Numero de Procesos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(274, 121)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Procesos_GB = QGroupBox(self.centralwidget)
        self.Procesos_GB.setObjectName(u"Procesos_GB")
        self.Procesos_GB.setGeometry(QRect(10, 10, 251, 71))
        self.Capturar_Boton = QPushButton(self.Procesos_GB)
        self.Capturar_Boton.setObjectName(u"Capturar_Boton")
        self.Capturar_Boton.setGeometry(QRect(150, 20, 91, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Capturar_Boton.setFont(font)
        self.Procesos_SB = QSpinBox(self.Procesos_GB)
        self.Procesos_SB.setObjectName(u"Procesos_SB")
        self.Procesos_SB.setGeometry(QRect(80, 20, 51, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.Procesos_SB.setFont(font1)
        self.Procesos_SB.setMaximum(999)
        self.label = QLabel(self.Procesos_GB)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 274, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Numero de Procesos", None))
        self.Procesos_GB.setTitle("")
        self.Capturar_Boton.setText(QCoreApplication.translate("MainWindow", u"Capturar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Procesos:", None))
    # retranslateUi


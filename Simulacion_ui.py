# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulacion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 587)
        self.Nuevo_Boton = QPushButton(Form)
        self.Nuevo_Boton.setObjectName(u"Nuevo_Boton")
        self.Nuevo_Boton.setGeometry(QRect(720, 540, 161, 31))
        font = QFont()
        font.setPointSize(10)
        self.Nuevo_Boton.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 543, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.Tiempo_TB = QTextBrowser(Form)
        self.Tiempo_TB.setObjectName(u"Tiempo_TB")
        self.Tiempo_TB.setGeometry(QRect(90, 540, 171, 31))
        self.Simulacion_TW = QTableWidget(Form)
        self.Simulacion_TW.setObjectName(u"Simulacion_TW")
        self.Simulacion_TW.setGeometry(QRect(10, 10, 661, 231))
        self.Lotes_TW = QTableWidget(Form)
        self.Lotes_TW.setObjectName(u"Lotes_TW")
        self.Lotes_TW.setGeometry(QRect(680, 50, 221, 481))
        self.Resultados_TW = QTableWidget(Form)
        self.Resultados_TW.setObjectName(u"Resultados_TW")
        self.Resultados_TW.setGeometry(QRect(10, 250, 661, 281))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 10, 121, 31))
        self.label_2.setFont(font1)
        self.Lotes_Restantes_TB = QTextBrowser(Form)
        self.Lotes_Restantes_TB.setObjectName(u"Lotes_Restantes_TB")
        self.Lotes_Restantes_TB.setGeometry(QRect(810, 10, 81, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simulaci\u00f3n", None))
        self.Nuevo_Boton.setText(QCoreApplication.translate("Form", u"Nueva Simulaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tiempo: ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Lotes Restantes:", None))
    # retranslateUi


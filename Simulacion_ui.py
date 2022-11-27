# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Simulacion.ui'
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
        Form.resize(556, 411)
        self.Nuevo_Boton = QPushButton(Form)
        self.Nuevo_Boton.setObjectName(u"Nuevo_Boton")
        self.Nuevo_Boton.setGeometry(QRect(390, 370, 161, 31))
        font = QFont()
        font.setPointSize(10)
        self.Nuevo_Boton.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 373, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.Tiempo_TB = QTextBrowser(Form)
        self.Tiempo_TB.setObjectName(u"Tiempo_TB")
        self.Tiempo_TB.setGeometry(QRect(90, 370, 171, 31))
        self.Simulacion_TB = QTextBrowser(Form)
        self.Simulacion_TB.setObjectName(u"Simulacion_TB")
        self.Simulacion_TB.setGeometry(QRect(10, 10, 341, 171))
        self.Resultados_TB = QTextBrowser(Form)
        self.Resultados_TB.setObjectName(u"Resultados_TB")
        self.Resultados_TB.setGeometry(QRect(10, 190, 341, 171))
        self.Lotes_TB = QTextBrowser(Form)
        self.Lotes_TB.setObjectName(u"Lotes_TB")
        self.Lotes_TB.setGeometry(QRect(360, 10, 191, 351))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simulaci\u00f3n", None))
        self.Nuevo_Boton.setText(QCoreApplication.translate("Form", u"Nueva Simulaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tiempo: ", None))
    # retranslateUi


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
        Form.resize(1124, 639)
        self.Nuevo_Boton = QPushButton(Form)
        self.Nuevo_Boton.setObjectName(u"Nuevo_Boton")
        self.Nuevo_Boton.setGeometry(QRect(880, 10, 161, 31))
        font = QFont()
        font.setPointSize(10)
        self.Nuevo_Boton.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 13, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.Tiempo_TB = QTextBrowser(Form)
        self.Tiempo_TB.setObjectName(u"Tiempo_TB")
        self.Tiempo_TB.setGeometry(QRect(490, 10, 171, 31))
        self.Listos_TW = QTableWidget(Form)
        self.Listos_TW.setObjectName(u"Listos_TW")
        self.Listos_TW.setGeometry(QRect(10, 80, 691, 171))
        self.Listos_TW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Listos_TW.setRowCount(0)
        self.Listos_TW.setColumnCount(0)
        self.Listos_TW.horizontalHeader().setCascadingSectionResizes(True)
        self.Listos_TW.horizontalHeader().setDefaultSectionSize(175)
        self.Listos_TW.verticalHeader().setVisible(False)
        self.Terminados_TW = QTableWidget(Form)
        self.Terminados_TW.setObjectName(u"Terminados_TW")
        self.Terminados_TW.setGeometry(QRect(710, 80, 401, 541))
        self.Terminados_TW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Terminados_TW.horizontalHeader().setCascadingSectionResizes(True)
        self.Terminados_TW.verticalHeader().setVisible(False)
        self.Bloqueados_TW = QTableWidget(Form)
        self.Bloqueados_TW.setObjectName(u"Bloqueados_TW")
        self.Bloqueados_TW.setGeometry(QRect(10, 430, 691, 191))
        self.Bloqueados_TW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Bloqueados_TW.horizontalHeader().setCascadingSectionResizes(True)
        self.Bloqueados_TW.horizontalHeader().setDefaultSectionSize(160)
        self.Bloqueados_TW.verticalHeader().setVisible(False)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 151, 31))
        self.label_2.setFont(font1)
        self.Nuevos_TB = QTextBrowser(Form)
        self.Nuevos_TB.setObjectName(u"Nuevos_TB")
        self.Nuevos_TB.setGeometry(QRect(160, 10, 191, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(710, 50, 401, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 691, 31))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 250, 691, 31))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.Ejecucion_TW = QTableWidget(Form)
        self.Ejecucion_TW.setObjectName(u"Ejecucion_TW")
        self.Ejecucion_TW.setGeometry(QRect(10, 280, 691, 121))
        self.Ejecucion_TW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Ejecucion_TW.setColumnCount(0)
        self.Ejecucion_TW.horizontalHeader().setCascadingSectionResizes(True)
        self.Ejecucion_TW.horizontalHeader().setDefaultSectionSize(120)
        self.Ejecucion_TW.verticalHeader().setVisible(False)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 400, 691, 31))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simulaci\u00f3n", None))
        self.Nuevo_Boton.setText(QCoreApplication.translate("Form", u"Nueva Simulaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tiempo: ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Procesos en Nuevos:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Procesos Terminados", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Procesos en Listos", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Proceso en Ejecucion", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Proceso en Bloqueados", None))
    # retranslateUi


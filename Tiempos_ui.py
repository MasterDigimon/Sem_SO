# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tiempos.ui'
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
        Form.resize(1547, 509)
        self.Tiempo_TW = QTableWidget(Form)
        self.Tiempo_TW.setObjectName(u"Tiempo_TW")
        self.Tiempo_TW.setGeometry(QRect(10, 10, 1531, 491))
        self.Tiempo_TW.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Tiempo_TW.horizontalHeader().setCascadingSectionResizes(True)
        self.Tiempo_TW.horizontalHeader().setDefaultSectionSize(140)
        self.Tiempo_TW.verticalHeader().setVisible(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


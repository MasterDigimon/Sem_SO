# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Captura de Procesos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Captura_Form(object):
    def setupUi(self, Captura_Form):
        if not Captura_Form.objectName():
            Captura_Form.setObjectName(u"Captura_Form")
        Captura_Form.resize(412, 337)
        self.groupBox = QGroupBox(Captura_Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 391, 251))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 20))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.Nombre_TE = QTextEdit(self.groupBox)
        self.Nombre_TE.setObjectName(u"Nombre_TE")
        self.Nombre_TE.setGeometry(QRect(10, 30, 371, 31))
        self.Suma_CB = QCheckBox(self.groupBox)
        self.Suma_CB.setObjectName(u"Suma_CB")
        self.Suma_CB.setGeometry(QRect(10, 150, 70, 21))
        self.Suma_CB.setFont(font)
        self.Resta_CB = QCheckBox(self.groupBox)
        self.Resta_CB.setObjectName(u"Resta_CB")
        self.Resta_CB.setGeometry(QRect(160, 150, 70, 21))
        self.Resta_CB.setFont(font)
        self.Multiplicacion_CB = QCheckBox(self.groupBox)
        self.Multiplicacion_CB.setObjectName(u"Multiplicacion_CB")
        self.Multiplicacion_CB.setGeometry(QRect(310, 150, 70, 21))
        self.Multiplicacion_CB.setFont(font)
        self.Potencia_CB = QCheckBox(self.groupBox)
        self.Potencia_CB.setObjectName(u"Potencia_CB")
        self.Potencia_CB.setGeometry(QRect(310, 180, 70, 21))
        self.Potencia_CB.setFont(font)
        self.Modulo_CB = QCheckBox(self.groupBox)
        self.Modulo_CB.setObjectName(u"Modulo_CB")
        self.Modulo_CB.setGeometry(QRect(160, 180, 70, 21))
        self.Modulo_CB.setFont(font)
        self.Division_CB = QCheckBox(self.groupBox)
        self.Division_CB.setObjectName(u"Division_CB")
        self.Division_CB.setGeometry(QRect(10, 180, 70, 21))
        self.Division_CB.setFont(font)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 201, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 209, 71, 31))
        self.label_3.setFont(font)
        self.Tiempo_SB = QDoubleSpinBox(self.groupBox)
        self.Tiempo_SB.setObjectName(u"Tiempo_SB")
        self.Tiempo_SB.setGeometry(QRect(80, 210, 62, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.Tiempo_SB.setFont(font1)
        self.Tiempo_SB.setDecimals(1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 210, 111, 31))
        self.label_4.setFont(font)
        self.ID_SB = QSpinBox(self.groupBox)
        self.ID_SB.setObjectName(u"ID_SB")
        self.ID_SB.setGeometry(QRect(330, 210, 51, 31))
        self.ID_SB.setFont(font1)
        self.ID_SB.setMaximum(999)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 60, 81, 20))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 90, 71, 31))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 90, 71, 31))
        self.label_8.setFont(font)
        self.ValorA_SB = QDoubleSpinBox(self.groupBox)
        self.ValorA_SB.setObjectName(u"ValorA_SB")
        self.ValorA_SB.setGeometry(QRect(40, 90, 62, 31))
        self.ValorA_SB.setFont(font1)
        self.ValorB_SB = QDoubleSpinBox(self.groupBox)
        self.ValorB_SB.setObjectName(u"ValorB_SB")
        self.ValorB_SB.setGeometry(QRect(220, 90, 62, 31))
        self.ValorB_SB.setFont(font1)
        self.label_5 = QLabel(Captura_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 371, 21))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.CapturarP_Boton = QPushButton(Captura_Form)
        self.CapturarP_Boton.setObjectName(u"CapturarP_Boton")
        self.CapturarP_Boton.setGeometry(QRect(160, 300, 91, 31))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.CapturarP_Boton.setFont(font3)

        self.retranslateUi(Captura_Form)

        QMetaObject.connectSlotsByName(Captura_Form)
    # setupUi

    def retranslateUi(self, Captura_Form):
        Captura_Form.setWindowTitle(QCoreApplication.translate("Captura_Form", u"Captura de Procesos", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Captura_Form", u"Nombre del Programador:", None))
        self.Suma_CB.setText(QCoreApplication.translate("Captura_Form", u"A + B", None))
        self.Resta_CB.setText(QCoreApplication.translate("Captura_Form", u"A - B", None))
        self.Multiplicacion_CB.setText(QCoreApplication.translate("Captura_Form", u"A x B", None))
        self.Potencia_CB.setText(QCoreApplication.translate("Captura_Form", u"A ^ B", None))
        self.Modulo_CB.setText(QCoreApplication.translate("Captura_Form", u"A % B", None))
        self.Division_CB.setText(QCoreApplication.translate("Captura_Form", u"A / B", None))
        self.label_2.setText(QCoreApplication.translate("Captura_Form", u"Operaci\u00f3n:", None))
        self.label_3.setText(QCoreApplication.translate("Captura_Form", u"Tiempo: ", None))
        self.label_4.setText(QCoreApplication.translate("Captura_Form", u"ID de Proceso:", None))
        self.label_6.setText(QCoreApplication.translate("Captura_Form", u"Valores:", None))
        self.label_7.setText(QCoreApplication.translate("Captura_Form", u"A: ", None))
        self.label_8.setText(QCoreApplication.translate("Captura_Form", u"B: ", None))
        self.label_5.setText(QCoreApplication.translate("Captura_Form", u"N\u00famero de Proceso:", None))
        self.CapturarP_Boton.setText(QCoreApplication.translate("Captura_Form", u"Capturar", None))
    # retranslateUi


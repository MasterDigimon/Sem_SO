from PySide2.QtWidgets import QMainWindow, QMessageBox, QWidget
from N_Procesos_ui import Ui_MainWindow
from C_Procesos import *
from clases import Proceso
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.procesos = []
        self.ui.Capturar_Boton.clicked.connect(self.def_numero)

        self.operacion = [None, None, None]
        return


        
    def def_numero(self):
        if(self.ui.Procesos_SB.value() == 0):
            QMessageBox.warning(self, "Error", "No se pueden asignar 0 procesos")
        elif(self.ui.Quantum_SB.value() == 0):
            QMessageBox.warning(self, "Error", "No se puede asignar 0 de Quantum")
        else:
            self.asignar_valores()
            self.hide()
            self.ventana = Simulacion(self.procesos, self.ui.Quantum_SB.value())
            self.ventana.show()
            pass
        pass

    def asignar_valores(self):
        
        for i in range(0, self.ui.Procesos_SB.value()):
            proceso = Proceso(i)
            self.procesos.append(proceso)

    

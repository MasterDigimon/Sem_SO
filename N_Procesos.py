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
        else:
            self.asignar_valores()
            self.hide()
            self.ventana = Simulacion(self.procesos)
            self.ventana.show()
            pass
        pass

    def asignar_valores(self):
        
        for i in range(0, self.ui.Procesos_SB.value()):
            self.genOperacion()
            proceso = Proceso(i, self.operacion[1], self.operacion[2], self.operacion[0], random.randint(6, 16))
            self.procesos.append(proceso)

    def genOperacion(self):
        self.operacion[0] = random.randint(0, 5)
        #Suma - 0, Resta - 1, Multiplicacion - 2, Division - 3, Modulo - 4, Potencia - 5

        if(self.operacion[0] == 0):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(0, 100)

        elif(self.operacion[0] == 1):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(0, 100)

        elif(self.operacion[0] == 2):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(0, 100)

        elif(self.operacion[0] == 3):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(1, self.operacion[1])

        elif(self.operacion[0] == 4):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(0, self.operacion[1])

        elif(self.operacion[0] == 5):
            self.operacion[1] = random.randint(0, 100)
            self.operacion[2] = random.randint(0, 5)

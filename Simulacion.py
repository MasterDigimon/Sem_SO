from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget
from clases import Proceso
import time


class Simulacion(QWidget):
    def __init__(self, _ids, _operaciones):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.contpros = 0
        self.contlote = 0
        self.ejecucion = True
        self.ids = _ids
        self.operaciones = _operaciones

        self.ui.Nuevo_Boton.clicked.connect(self.sim)

        pass

    def sim(self):
        cont_tiempo = 0
        
        for i in self.ids:
            proceso = self.operaciones[i]
            self.imprimir_lotes(i)
            self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")
            for x in range(0, int(proceso.tiempo * 10)):
                time.sleep(.1)
                cont_tiempo += .1
                self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")
        pass

    def imprimir_lotes(self, i):
        self.ui.Lotes_TB.clear()
        texto = ""
        actual = self.ids.index(i)
        restantes = len(self.ids) - actual - 1
        texto += ("Lotes Restantes " + str(restantes))
        texto += ("---------------------------------------------\n")
        for f in range(0, actual):
            texto += ("Lote " + str(f + 1) + " --- Terminado\n")
            print("Lote " + str(f + 1) + " --- Terminado\n")

        texto += ("Lote " + str(actual + 1) + " --- En ejecucion\n")
        print("Lote " + str(actual + 1) + " --- En ejecucion\n")
        if(actual == 0):
            for f in range(actual + 1, restantes + 1):
                texto += ("Lote " + str(f + 1) + " --- En espera\n")
                print("Lote " + str(f + 1) + " --- En espera\n")
        else:
            for f in range(actual + 1, restantes + 2):
                texto += ("Lote " + str(f + 1) + " --- En espera\n")
                print("Lote " + str(f + 1) + " --- En espera\n")
        
        self.ui.Lotes_TB.setText(texto)
        

        return
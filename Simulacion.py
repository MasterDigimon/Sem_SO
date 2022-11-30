from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from clases import Proceso
import time


class Simulacion(QWidget):
    def __init__(self, _ids, _operaciones):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        
        self.contlotes = 0
        self.ejecucion = True
        self.ids = _ids

        self.estado_lotes = []
        self.lotes = {}
        for x in range(0, len(self.ids)):
            if(x % 3 == 0):
                self.contlotes += 1
                self.estado_lotes.append("Pendiente")
                self.lotes[self.contlotes] = []
            self.lotes[self.contlotes].append(_operaciones[_ids[x]])
        

        self.ui.Nuevo_Boton.clicked.connect(self.sim)

        pass

    def sim(self):
        for i in self.estado_lotes:
            i = "Pendiente"
        
        cont_tiempo = 0
        lotes_restantes = self.contlotes
        terminados = []
        
        
        for i in range(1, self.contlotes + 1):
            self.estado_lotes[i - 1] = "En Ejecucion"
            lotes_restantes -= 1

            for x in self.lotes[i]:
                x.iniciar_sim()

                self.imprimir_lotes()
                
                
                self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")

                for y in range(0, int(x.tiempo * 10)):
                    time.sleep(.1)
                    cont_tiempo += .1
                    x.tiempoTranscurrido = round(x.tiempoTranscurrido + .1, 2)
                    self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")
                    self.ui.Lotes_Restantes_TB.setText(str(lotes_restantes))

                    self.imprimir_ProcesoEjec(self.lotes[i]);
                    QApplication.processEvents()


                
                terminados.append(x)
                self.imprimir_terminados(terminados)
                self.imprimir_lotes()
                QApplication.processEvents()

            self.estado_lotes[i - 1] = "Terminado"
            self.imprimir_terminados(terminados)
            self.imprimir_lotes()
            QApplication.processEvents()
        
        
        pass

    def imprimir_lotes(self):
        headers = ["Lote", "Estado"]

        self.ui.Lotes_TW.setColumnCount(2)
        self.ui.Lotes_TW.setRowCount(int(self.contlotes))
        self.ui.Lotes_TW.setHorizontalHeaderLabels(headers)


        for f in range(0, self.contlotes):
            lote = QTableWidgetItem("Lote " + str(f + 1))
            estado = QTableWidgetItem(self.estado_lotes[f])
      

            self.ui.Lotes_TW.setItem(f, 0, lote)
            self.ui.Lotes_TW.setItem(f, 1, estado)

            pass
        

        return

    def imprimir_ProcesoEjec(self, lote):
        headers = ["ID", "Nombre", "Operacion", "Tiempo Esperado", "Tiempo Transcurrido"]

        self.ui.Simulacion_TW.setColumnCount(5)
        self.ui.Simulacion_TW.setRowCount(len(lote))
        self.ui.Simulacion_TW.setHorizontalHeaderLabels(headers)

        for i in range(0, len(lote)):
            id = QTableWidgetItem(str(lote[i].id))
            nombre = QTableWidgetItem(str(lote[i].nombre))
            operacion = QTableWidgetItem(str(lote[i].Return_operacion()))
            Tiempo_Esperado = QTableWidgetItem(str(lote[i].tiempo))
            Tiempo_Transcurrido = QTableWidgetItem(str(lote[i].tiempoTranscurrido))

            self.ui.Simulacion_TW.setItem(i, 0, id)
            self.ui.Simulacion_TW.setItem(i, 1, nombre)
            self.ui.Simulacion_TW.setItem(i, 2, operacion)
            self.ui.Simulacion_TW.setItem(i, 3, Tiempo_Esperado)
            self.ui.Simulacion_TW.setItem(i, 4, Tiempo_Transcurrido)

        pass

    def imprimir_terminados(self, terminados):
        headers = ["ID", "Nombre", "Operacion", "Resultado"]

        self.ui.Resultados_TW.setColumnCount(4)
        self.ui.Resultados_TW.setRowCount(len(terminados))
        self.ui.Resultados_TW.setHorizontalHeaderLabels(headers)

        for i in range(0, len(terminados)):
            id = QTableWidgetItem(str(terminados[i].id))
            nombre = QTableWidgetItem(str(terminados[i].nombre))
            operacion = QTableWidgetItem(str(terminados[i].Return_operacion()))
            resultado = QTableWidgetItem(str(terminados[i].calcular_resultado()))

            self.ui.Resultados_TW.setItem(i, 0, id)
            self.ui.Resultados_TW.setItem(i, 1, nombre)
            self.ui.Resultados_TW.setItem(i, 2, operacion)
            self.ui.Resultados_TW.setItem(i, 3, resultado)
        pass

from Tiempos_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from clases import Proceso

class Tiempos(QWidget):
    def __init__(self, _procesos):
        super(Tiempos, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.procesos = _procesos

        self.Imprimir_procesos()

        

    def Imprimir_procesos(self):
        headers = ["ID", "Operacion", "Resultado", "Tiempo de Llegada", "Tiempo de Finalizacion", "Tiempo de Retorno", "Tiempo de Respuesta", "Tiempo de Espera", "Tiempo de Servicio"]

        self.ui.Tiempo_TW.setColumnCount(len(headers))
        self.ui.Tiempo_TW.setRowCount(len(self.procesos))
        self.ui.Tiempo_TW.setHorizontalHeaderLabels(headers)


        i = 0
        for x in self.procesos:
            id = QTableWidgetItem(str(x.id))
            operacion = QTableWidgetItem(x.Return_operacion())
            resultado = QTableWidgetItem(str(x.resultado))

            T_Llegada = QTableWidgetItem(str(x.T_Llegada))
            T_Finalizacion = QTableWidgetItem(str(x.T_Finalizacion))
            T_Retorno = QTableWidgetItem(str(x.T_Retorno))
            T_Respuesta = QTableWidgetItem(str(x.T_Respuesta))
            T_Espera = QTableWidgetItem(str(x.T_Espera))
            T_Servicio = QTableWidgetItem(str(x.T_Servicio))


            self.ui.Tiempo_TW.setItem(i, 0, id)
            self.ui.Tiempo_TW.setItem(i, 1, operacion)
            self.ui.Tiempo_TW.setItem(i, 2, resultado)
            self.ui.Tiempo_TW.setItem(i, 3, T_Llegada)
            self.ui.Tiempo_TW.setItem(i, 4, T_Finalizacion)
            self.ui.Tiempo_TW.setItem(i, 5, T_Retorno)
            self.ui.Tiempo_TW.setItem(i, 6, T_Respuesta)
            self.ui.Tiempo_TW.setItem(i, 7, T_Espera)
            self.ui.Tiempo_TW.setItem(i, 8, T_Servicio)
            i += 1


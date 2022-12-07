from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from clases import Proceso
import time
from pynput import keyboard as kb


pause  = False
accion = None

class Simulacion(QWidget):
    def __init__(self, _ids, _operaciones):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        
        self.contlotes = 0
        self.ejecucion = True
        self.ids = _ids

        self.estado_lotes = []
        self.estado_procesos = []
        self.lotes = {}
        for x in range(0, len(self.ids)):
            self.estado_procesos.append("Pendiente")
            if(x % 3 == 0):
                self.contlotes += 1
                self.estado_lotes.append("Pendiente")
                
                self.lotes[self.contlotes] = []
            self.lotes[self.contlotes].append(_operaciones[_ids[x]])
        

        self.ui.Nuevo_Boton.clicked.connect(self.sim)
        escuchador = kb.Listener(listener)
        escuchador.start()

        pass
    
    def inicializar(self):
        for i in range(0, len(self.estado_procesos)):
            self.estado_procesos[i] = "Pendiente"
        
        for i in range(0, len(self.estado_lotes)):
            self.estado_lotes[i] = "Pendiente"
        
        for i in range(1, self.contlotes + 1):
            for x in self.lotes[i]:
                x.iniciar_sim()

        self.imprimir_terminados([])
        global accion
        accion = None
        pass

    def sim(self):
        self.inicializar()
        for i in self.estado_lotes:
            i = "Pendiente"
        
        cont_tiempo = 0
        lotes_restantes = self.contlotes
        terminados = []
        global pause
        global accion

        cont_proceso = 0
        f = 1
        while(f < self.contlotes + 1):   #----- Lotes -----
            
            self.estado_lotes[f - 1] = "En Ejecucion"

            lotes_restantes = 0
            for pen in self.estado_lotes:
                if(pen == "Pendiente"):
                    lotes_restantes += 1
            
            n = 0
            while(n < len(self.lotes[f])):  #----- Procesos por lote -----
                x:Proceso = self.lotes[f][n]


                self.imprimir_lotes()
                
                
                self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")

                y = x.tiempoTranscurrido * 10
                while(y < int(x.tiempo * 10) and accion != 0 and self.estado_procesos[cont_proceso] == "Pendiente"):  #----- Tiempo de Proceso -----
                    
                    if(accion == 1):
                        x.error = True
                        self.estado_procesos[x.id] = "Terminado"
                        accion = None
                        terminados.append(x)
                        y = int(x.tiempo * 10)

                    elif(accion == 5):
                        QMessageBox.warning(self, "Error", "Pulsa C para continuar")
                        accion = None

                    elif(not pause):
                        


                        time.sleep(.1)
                        cont_tiempo += .1
                        x.tiempoTranscurrido = round(x.tiempoTranscurrido + .1, 2)
                        self.ui.Tiempo_TB.setText(str(round(cont_tiempo, 2)) + " s")
                        self.ui.Lotes_Restantes_TB.setText(str(lotes_restantes))
                        y += 1

                        self.imprimir_ProcesoEjec(self.lotes[f]);
                        QApplication.processEvents()

                    
                
                if(x.tiempo == x.tiempoTranscurrido):
                    self.estado_procesos[x.id] = "Terminado"
                    terminados.append(x)

                elif(accion == 0):
                    accion = None
                

                
                
                self.imprimir_terminados(terminados)
                self.imprimir_lotes()
                QApplication.processEvents()
                n += 1
                accion = None
                cont_proceso += 1

            if(not "Pendiente" in self.estado_procesos[3 * (f-1) : 3 * (f-1) + 3]):
                    self.estado_lotes[f - 1] = "Terminado"
            else:
                self.estado_lotes[f-1] = "Pendiente"

            self.imprimir_terminados(terminados)
            self.imprimir_lotes()
            QApplication.processEvents()
            f += 1
            if(f == self.contlotes + 1 and "Pendiente" in self.estado_procesos):
                f = 1
                cont_proceso = 0
        
        
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
        headers = ["ID", "Operacion", "Tiempo Esperado", "Tiempo Transcurrido"]

        self.ui.Simulacion_TW.setColumnCount(4)
        self.ui.Simulacion_TW.setRowCount(len(lote))
        self.ui.Simulacion_TW.setHorizontalHeaderLabels(headers)

        for i in range(0, len(lote)):
            id = QTableWidgetItem(str(lote[i].id))
            operacion = QTableWidgetItem(str(lote[i].Return_operacion()))
            Tiempo_Esperado = QTableWidgetItem(str(lote[i].tiempo))
            Tiempo_Transcurrido = QTableWidgetItem(str(lote[i].tiempoTranscurrido))

            self.ui.Simulacion_TW.setItem(i, 0, id)
            self.ui.Simulacion_TW.setItem(i, 1, operacion)
            self.ui.Simulacion_TW.setItem(i, 2, Tiempo_Esperado)
            self.ui.Simulacion_TW.setItem(i, 3, Tiempo_Transcurrido)

        pass

    def imprimir_terminados(self, terminados):
        headers = ["ID",  "Operacion", "Resultado"]

        self.ui.Resultados_TW.setColumnCount(3)
        self.ui.Resultados_TW.setRowCount(len(terminados))
        self.ui.Resultados_TW.setHorizontalHeaderLabels(headers)

        for i in range(0, len(terminados)):
            id = QTableWidgetItem(str(terminados[i].id))
            operacion = QTableWidgetItem(str(terminados[i].Return_operacion()))
            resultado = QTableWidgetItem(str(terminados[i].calcular_resultado()))
            if(terminados[i].error):
                resultado = QTableWidgetItem("Error")

            self.ui.Resultados_TW.setItem(i, 0, id)
            self.ui.Resultados_TW.setItem(i, 1, operacion)
            self.ui.Resultados_TW.setItem(i, 2, resultado)
        pass

def listener(tecla):
    global pause
    global accion
    if(pause):
        if(tecla == kb.KeyCode.from_char('c')):
            pause = False
        else:
            accion = 5
    
    else:
        if(tecla == kb.KeyCode.from_char('e')):
            accion = 0
        elif (tecla == kb.KeyCode.from_char('w')):
            accion = 1
        elif (tecla == kb.KeyCode.from_char('p')):
            accion = 2
            pause = True

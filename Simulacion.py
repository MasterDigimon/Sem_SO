from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from clases import Proceso
import time
from pynput import keyboard as kb


accion = None

class Simulacion(QWidget):
    def __init__(self, _procesos):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.procesos_iniciales = _procesos


        self.nuevo:Proceso = _procesos
        self.listo:Proceso = []
        self.bloqueado:Proceso = []
        self.terminado:Proceso = []
        self.ejecucion:Proceso = None

        self.cont_tiempo = 0
        

        self.ui.Nuevo_Boton.clicked.connect(self.sim)
        escuchador = kb.Listener(listener)
        escuchador.start()

        pass
    
    def inicializar(self):
        self.imprimir_terminados([])

        self.cont_tiempo = 0
        self.nuevo = self.procesos_iniciales
        self.listo = []
        self.bloqueado = []
        self.terminado = []
        self.ejecucion = None

        global accion
        accion = None
        pass

    def sim(self):
        self.inicializar()

        terminados = []
        global pause
        global accion
        cont_sistema = 0

        #Carga 3 procesos de Nuevo a Listo si hay suficientes procesos
        for i in range(0, 3):
            if(cont_sistema < 3  and len(self.nuevo) > 0):
                self.nuevo[0].T_Llegada = self.cont_tiempo
                self.listo.append(self.nuevo[0])
                cont_sistema += 1
                self.nuevo.pop(0)
        
        while(len(self.procesos_iniciales) != len(self.terminado)):

            #Carga proceso de Nuevo a Listo
            if(cont_sistema < 3 and len(self.nuevo) > 0):
                self.nuevo[0].T_Llegada = self.cont_tiempo
                self.listo.append(self.nuevo[0])
                cont_sistema += 1
                self.nuevo.pop(0)
                
            #Mueve un proceso de Listo a Terminado
            if(self.ejecucion == None and len(self.listo) > 0):
                self.ejecucion = self.listo[0]
                self.listo.pop(0)

                if(self.ejecucion.T_Respuesta == None):
                    self.ejecucion.T_Respuesta = self.cont_tiempo

            #-------------------------------   Ejecucion del proceso   ----------------------------------------
            while(self.ejecucion.tiempo < self.cont_tiempo and accion == None):
                self.cont_tiempo = round(self.cont_tiempo + .1, 2)
                self.ejecucion.tiempoTranscurrido = round(self.ejecucion.tiempoTranscurrido + .1, 2)
                self.ejecucion.tiempoRestante = round(self.ejecucion.tiempoRestante - .1, 2)

                #Aumento de tiempo de espera en procesos listos
                for listo in self.listo:
                    listo.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                #Aumento de tiempo de espera en procesos bloqueados
                for bloq in self.bloqueado:
                    bloq.T_Bloqueado = round(bloq.T_Bloqueado + .1, 2)
                    bloq.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                    #Mueve proceso de Bloqueado a Listo
                    if(bloq.T_Bloqueado == 7):
                        self.listo.append(bloq)
                        self.bloqueado.remove(bloq)

                

            
            #Termina proceso normalmente
            if(self.ejecucion.tiempoRestante == 0):
                self.ejecucion.resultado.calcular_resultado()
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                cont_sistema -= 1
                
            #Termina proceso por Error
            elif(accion == 1):
                self.ejecucion.resultado = "Error"
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                cont_sistema -= 1

            
            #Mueve proceso de Ejecucion a Bloqueado
            elif(accion == 0):
                self.ejecucion.T_Bloqueado = 0
                self.bloqueado.append(self.ejecucion)
                self.ejecucion = None




#------------------------------- VIEJO PROGRAMA --------------------------------------------
        pass
        f = 0
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
                
                
                self.ui.Tiempo_TB.setText(str(round(self.cont_tiempo, 2)) + " s")

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
                        self.cont_tiempo += .1
                        x.tiempoTranscurrido = round(x.tiempoTranscurrido + .1, 2)
                        x.tiempoRestante = round(x.tiempoRestante - .1, 2)
                        self.ui.Tiempo_TB.setText(str(round(self.cont_tiempo, 2)) + " s")
                        self.ui.Lotes_Restantes_TB.setText(str(lotes_restantes))
                        y += 1

                        self.imprimir_ProcesoEjec(self.lotes[f]);
                        QApplication.processEvents()

                    
                
                if(x.tiempo == x.tiempoTranscurrido and self.estado_procesos[x.id] != "Terminado"):
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
                if(n == len(self.lotes[f]) and "Pendiente" in self.estado_procesos[3 * (f-1) : 3 * (f-1) + 3]):
                    cont_proceso -= n
                    n = 0
                    


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
        headers = ["ID", "Operacion", "Tiempo Esperado", "Tiempo Transcurrido", "Tiempo Restante"]

        self.ui.Simulacion_TW.setColumnCount(5)
        self.ui.Simulacion_TW.setRowCount(len(lote))
        self.ui.Simulacion_TW.setHorizontalHeaderLabels(headers)

        for i in range(0, len(lote)):
            id = QTableWidgetItem(str(lote[i].id))
            operacion = QTableWidgetItem(str(lote[i].Return_operacion()))
            Tiempo_Esperado = QTableWidgetItem(str(lote[i].tiempo))
            Tiempo_Transcurrido = QTableWidgetItem(str(lote[i].tiempoTranscurrido))
            Tiempo_Restante = QTableWidgetItem(str(lote[i].tiempoRestante))

            self.ui.Simulacion_TW.setItem(i, 0, id)
            self.ui.Simulacion_TW.setItem(i, 1, operacion)
            self.ui.Simulacion_TW.setItem(i, 2, Tiempo_Esperado)
            self.ui.Simulacion_TW.setItem(i, 3, Tiempo_Transcurrido)
            self.ui.Simulacion_TW.setItem(i, 4, Tiempo_Restante)

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
    global accion
    if(accion == 2):
        if(tecla == kb.KeyCode.from_char('c')):
            accion = None
        else:
            accion = 5
    
    else:
        if(tecla == kb.KeyCode.from_char('e')):
            accion = 0
        elif (tecla == kb.KeyCode.from_char('w')):
            accion = 1
        elif (tecla == kb.KeyCode.from_char('p')):
            accion = 2

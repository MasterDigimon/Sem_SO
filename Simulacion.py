from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from clases import Proceso
from Tiempos import Tiempos
import time
from pynput import keyboard as kb


accion = None

class Simulacion(QWidget):
    def __init__(self, _procesos):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.procesos_iniciales = _procesos
        self.total_procesos = len(_procesos)


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
        self.imprimir_terminados()

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
        
        while(self.total_procesos != len(self.terminado)):

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

            self.ui.Nuevos_TB.setText(str(len(self.nuevo)))
            QApplication.processEvents()

            #-------------------------------   Ejecucion del proceso   ----------------------------------------
            if(len(self.bloqueado) != 3):
                while(self.ejecucion.tiempo > self.ejecucion.tiempoTranscurrido and accion == None):
                    self.cont_tiempo = round(self.cont_tiempo + .1, 2)
                    self.ejecucion.tiempoTranscurrido = round(self.ejecucion.tiempoTranscurrido + .1, 2)
                    self.ejecucion.tiempoRestante = round(self.ejecucion.tiempoRestante - .1, 2)
                    time.sleep(.1)


                    #Aumento de tiempo de espera en procesos bloqueados
                    for bloq in self.bloqueado:
                        bloq.T_Bloqueado = round(bloq.T_Bloqueado + .1, 2)
                        bloq.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                        #Mueve proceso de Bloqueado a Listo
                        if(bloq.T_Bloqueado == 7):
                            self.listo.append(bloq)

                    #Aumento de tiempo de espera en procesos listos o elimina procesos de bloqueado
                    for listo in self.listo:
                        if(listo in self.bloqueado):
                            self.bloqueado.remove(listo)
                        
                        else:
                            listo.T_Espera = round(listo.T_Espera + .1, 2)

                    self.imprimir_listos()
                    self.imprimir_Ejecucion()
                    self.imprimir_bloqueados()
                    self.ui.Tiempo_TB.setText(str(self.cont_tiempo))
                    QApplication.processEvents()
            else:
                while(len(self.bloqueado) == 3):
                    time.sleep(.1)


                    #Aumento de tiempo de espera en procesos bloqueados
                    for bloq in self.bloqueado:
                        bloq.T_Bloqueado = round(bloq.T_Bloqueado + .1, 2)
                        bloq.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                        #Mueve proceso de Bloqueado a Listo
                        if(bloq.T_Bloqueado == 7):
                            self.listo.append(bloq)

                    #Aumento de tiempo de espera en procesos listos o elimina procesos de bloqueado
                    for listo in self.listo:
                        if(listo in self.bloqueado):
                            self.bloqueado.remove(listo)
                        
                        else:
                            listo.T_Espera = round(listo.T_Espera + .1, 2)

                    self.imprimir_listos()
                    self.imprimir_Ejecucion()
                    self.imprimir_bloqueados()
                    self.ui.Tiempo_TB.setText(str(self.cont_tiempo))
                    QApplication.processEvents()

                

            
            #Termina proceso normalmente
            if(self.ejecucion == None):
                pass
            elif(self.ejecucion.tiempoRestante == 0):
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.ejecucion.calcular_resultado(False)
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                cont_sistema -= 1
                
            #Termina proceso por Error
            elif(accion == 1):
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.ejecucion.calcular_resultado(True)
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                cont_sistema -= 1
                accion = None

            
            #Mueve proceso de Ejecucion a Bloqueado
            elif(accion == 0):
                self.ejecucion.T_Bloqueado = 0
                self.bloqueado.append(self.ejecucion)
                self.ejecucion = None
                accion = None
            
            self.imprimir_listos()
            self.imprimir_Ejecucion()
            self.imprimir_bloqueados()
            self.imprimir_terminados()
            self.ui.Nuevos_TB.setText(str(len(self.nuevo)))
            QApplication.processEvents()
        
        self.Mostrar_Tiempos()

        


    def imprimir_listos(self):
        headers = ["ID", "Tiempo Estimado", "Tiempo Ejecutado", "Tiempo en Espera"]

        self.ui.Listos_TW.setColumnCount(4)
        self.ui.Listos_TW.setRowCount(len(self.listo))
        self.ui.Listos_TW.setHorizontalHeaderLabels(headers)

        cont = 0
        for f in self.listo:
            id = QTableWidgetItem(str(f.id))
            tiempo = QTableWidgetItem(str(f.tiempo))
            tiempoT = QTableWidgetItem(str(f.tiempoTranscurrido))
            tiempoE = QTableWidgetItem(str(f.T_Espera))
      

            self.ui.Listos_TW.setItem(cont, 0, id)
            self.ui.Listos_TW.setItem(cont, 1, tiempo)
            self.ui.Listos_TW.setItem(cont, 2, tiempoT)
            self.ui.Listos_TW.setItem(cont, 3, tiempoE)
            cont += 1



    def imprimir_Ejecucion(self):
        headers = ["ID", "Operacion", "Tiempo Esperado", "Tiempo Transcurrido", "Tiempo Restante"]

        self.ui.Ejecucion_TW.setColumnCount(5)
        self.ui.Ejecucion_TW.setRowCount(1)
        self.ui.Ejecucion_TW.setHorizontalHeaderLabels(headers)

        if(self.ejecucion == None):
            id = QTableWidgetItem("")
            operacion = QTableWidgetItem("")
            Tiempo_Esperado = QTableWidgetItem("")
            Tiempo_Transcurrido = QTableWidgetItem("")
            Tiempo_Restante = QTableWidgetItem("")
        else:
            id = QTableWidgetItem(str(self.ejecucion.id))
            operacion = QTableWidgetItem(str(self.ejecucion.Return_operacion()))
            Tiempo_Esperado = QTableWidgetItem(str(self.ejecucion.tiempo))
            Tiempo_Transcurrido = QTableWidgetItem(str(self.ejecucion.tiempoTranscurrido))
            Tiempo_Restante = QTableWidgetItem(str(self.ejecucion.tiempoRestante))

        self.ui.Ejecucion_TW.setItem(0, 0, id)
        self.ui.Ejecucion_TW.setItem(0, 1, operacion)
        self.ui.Ejecucion_TW.setItem(0, 2, Tiempo_Esperado)
        self.ui.Ejecucion_TW.setItem(0, 3, Tiempo_Transcurrido)
        self.ui.Ejecucion_TW.setItem(0, 4, Tiempo_Restante)

        pass

    def imprimir_bloqueados(self):
        headers = ["ID", "Tiempo en Bloqueados"]

        self.ui.Bloqueados_TW.setColumnCount(2)
        self.ui.Bloqueados_TW.setRowCount(len(self.bloqueado))
        self.ui.Bloqueados_TW.setHorizontalHeaderLabels(headers)

        cont = 0
        for f in self.bloqueado:
            id = QTableWidgetItem(str(f.id))
            tiempo = QTableWidgetItem(str(f.T_Bloqueado))
      

            self.ui.Bloqueados_TW.setItem(cont, 0, id)
            self.ui.Bloqueados_TW.setItem(cont, 1, tiempo)
            cont += 1


    def imprimir_terminados(self):
        headers = ["ID",  "Operacion", "Resultado"]

        self.ui.Terminados_TW.setColumnCount(3)
        self.ui.Terminados_TW.setRowCount(len(self.terminado))
        self.ui.Terminados_TW.setHorizontalHeaderLabels(headers)

        cont = 0
        for i in self.terminado:
            id = QTableWidgetItem(str(i.id))
            operacion = QTableWidgetItem(str(i.Return_operacion()))
            resultado = QTableWidgetItem(str(i.resultado))

            self.ui.Terminados_TW.setItem(cont, 0, id)
            self.ui.Terminados_TW.setItem(cont, 1, operacion)
            self.ui.Terminados_TW.setItem(cont, 2, resultado)
            cont += 1
        pass

    def Mostrar_Tiempos(self):
        procesos = []
        procesos.extend(self.terminado)
        if(self.ejecucion != None):
            procesos.append(self.ejecucion)
        procesos.extend(self.bloqueado)
        procesos.extend(self.listo)

        self.ventana_tiempos = Tiempos(procesos)
        self.ventana_tiempos.show()
        

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

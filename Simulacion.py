from PySide2.QtWidgets import QTextEdit
from Simulacion_ui import Ui_Form
from PySide2.QtWidgets import QMessageBox, QWidget, QTableWidgetItem, QApplication
from PySide2.QtGui import QColor
from clases import Proceso
from Tiempos import Tiempos
import time
from pynput import keyboard as kb


accion = None

class Simulacion(QWidget):
    def __init__(self, _procesos, _quantum):
        super(Simulacion, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.procesos_iniciales = _procesos
        self.total_procesos = len(_procesos)
        self.quantum = _quantum


        self.nuevo:Proceso = _procesos
        self.listo:Proceso = []
        self.bloqueado:Proceso = []
        self.terminado:Proceso = []
        self.ejecucion:Proceso = None


        self.cont_tiempo = 0

        self.marcos = []
        self.id_marcos = []
        self.marcos_libres = 40
        self.cont_sistema = 0
        

        self.ui.Nuevo_Boton.clicked.connect(self.sim)
        self.ui.Detener_Boton.clicked.connect(self.detener)
        escuchador = kb.Listener(listener)
        escuchador.start()

        

        pass
    
    def inicializar(self):

        self.iniciar_memoria()

        self.imprimir_terminados()

        for i in range(0, 40):
            self.marcos.append(None)
            self.id_marcos.append(None)

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
        
        tiempo_limite = 0

        self.ui.Quantum_TB.setText(str(self.quantum))

        #Carga procesos de Nuevo a Listo
        
        self.cargar_proceso()
        
        
        while(self.total_procesos != len(self.terminado) and accion != 10):

            #Carga proceso de Nuevo a Listo
            if(len(self.nuevo) > 0):
                self.cargar_proceso()
                
            #Mueve un proceso de Listo a Ejecucion
            if(self.ejecucion == None and len(self.listo) > 0):
                self.ejecucion = self.listo[0]
                self.ejecucion.estado = "Ejecucion"
                self.listo.pop(0)

                if(self.ejecucion.T_Respuesta == None):
                    self.ejecucion.T_Respuesta = self.cont_tiempo

            self.ui.Nuevos_TB.setText(str(len(self.nuevo)))
            if(len(self.nuevo) > 0):
                self.ui.NextID_TB.setText(str(self.nuevo[0].id))
                self.ui.NextTam_TB.setText(str(self.nuevo[0].memoria))
            else:
                self.ui.NextID_TB.setText("")
                self.ui.NextTam_TB.setText("")
            QApplication.processEvents()

            #-------------------------------   Ejecucion del proceso   ----------------------------------------
            if(self.ejecucion != None):
                tiempo_limite = round(self.cont_tiempo + self.quantum, 2)
                while(self.ejecucion.tiempo > self.ejecucion.T_Servicio and accion == None and self.cont_tiempo < tiempo_limite):
                    self.cont_tiempo = round(self.cont_tiempo + .1, 2)
                    self.ejecucion.T_Servicio = round(self.ejecucion.T_Servicio + .1, 2)
                    self.ejecucion.tiempoRestante = round(self.ejecucion.tiempoRestante - .1, 2)
                    time.sleep(.1)


                    #Aumento de tiempo de espera en procesos bloqueados
                    for bloq in self.bloqueado:
                        bloq.T_Bloqueado = round(bloq.T_Bloqueado + .1, 2)
                        bloq.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                        #Mueve proceso de Bloqueado a Listo
                        if(bloq.T_Bloqueado == 7):
                            bloq.estado = "Listo"
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
                while(len(self.bloqueado) > 0 and self.ejecucion == None):
                    self.cont_tiempo = round(self.cont_tiempo + .1, 2)
                    time.sleep(.1)


                    #Aumento de tiempo de espera en procesos bloqueados
                    for bloq in self.bloqueado:
                        bloq.T_Bloqueado = round(bloq.T_Bloqueado + .1, 2)
                        bloq.T_Espera = round(bloq.T_Bloqueado + .1, 2)

                        #Mueve proceso de Bloqueado a Listo
                        if(bloq.T_Bloqueado == 7):
                            bloq.estado = "Listo"
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

                

            
            
            if(self.ejecucion == None):
                pass

            #Termina proceso normalmente
            elif(self.ejecucion.tiempoRestante == 0):
                self.ejecucion.estado = "Terminado"
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.ejecucion.calcular_resultado(False)
                self.imprimir_memoria(self.ejecucion, "white")
                self.descargar_proceso()
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                
                
            #Termina proceso por Error
            elif(accion == 1):
                self.ejecucion.estado = "Terminado"
                self.ejecucion.T_Finalizacion = self.cont_tiempo
                self.ejecucion.calcular_resultado(True)
                self.imprimir_memoria(self.ejecucion, "white")
                self.descargar_proceso()
                self.terminado.append(self.ejecucion)
                self.ejecucion = None
                accion = None

            
            #Mueve proceso de Ejecucion a Bloqueado
            elif(accion == 0):
                self.ejecucion.estado = "Bloqueado"
                self.ejecucion.T_Bloqueado = 0
                self.bloqueado.append(self.ejecucion)
                self.ejecucion = None
                accion = None

            #Genera Nuevo proceso
            elif(accion == 3):
                self.nuevo.append(Proceso(self.total_procesos))
                self.total_procesos += 1
                accion = None

            #Mostrar Tabla de Procesos
            elif(accion == 4):
                self.Mostrar_Tiempos()
                accion = 2

            #Mover proceso a Listo por tiempo
            elif(self.cont_tiempo == tiempo_limite and len(self.listo) > 0):
                self.ejecucion.estado = "Listo"
                self.listo.append(self.ejecucion)
                self.ejecucion = None
            
            self.imprimir_listos()
            self.imprimir_Ejecucion()
            self.imprimir_bloqueados()
            self.imprimir_terminados()
            self.ui.Nuevos_TB.setText(str(len(self.nuevo)))
            QApplication.processEvents()
        
        self.Mostrar_Tiempos()

    
    def cargar_proceso(self):

        while(self.marcos_libres >= self.nuevo[0].paginas_libres and len(self.nuevo) > 1):
            
            if(self.marcos[self.cont_sistema] == None and self.nuevo[0].paginas_libres > 1):
                self.marcos[self.cont_sistema] = 5
                self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                self.nuevo[0].paginas_libres -= 1
                self.marcos_libres -= 1
                self.nuevo[0].posiciones.append(self.cont_sistema)

            elif(self.marcos[self.cont_sistema] == None and self.nuevo[0].paginas_libres == 1):

                if(self.nuevo[0].pagina_sobrante == None):
                    self.marcos[self.cont_sistema] = 5
                    self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                    self.nuevo[0].paginas_libres -= 1
                    self.marcos_libres -= 1
                    self.nuevo[0].posiciones.append(self.cont_sistema)
                    self.nuevo[0].estado = "Listo"

                    self.nuevo[0].T_Llegada = self.cont_tiempo

                    self.imprimir_memoria(self.nuevo[0], "blue")
                    self.listo.append(self.nuevo[0])
                    self.nuevo.pop(0)
                    


                elif(self.nuevo[0].pagina_sobrante > 0):
                    self.marcos[self.cont_sistema] = self.nuevo[0].pagina_sobrante
                    self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                    self.nuevo[0].paginas_libres -= 1
                    self.marcos_libres -= 1
                    self.nuevo[0].posiciones.append(self.cont_sistema)
                    self.nuevo[0].estado = "Listo"

                    self.nuevo[0].T_Llegada = self.cont_tiempo

                    self.imprimir_memoria(self.nuevo[0], "blue")
                    self.listo.append(self.nuevo[0])
                    self.nuevo.pop(0)

            if(self.cont_sistema < 39):
                self.cont_sistema += 1
            else:
                self.cont_sistema =0
            


        if(self.marcos_libres >= self.nuevo[0].paginas_libres and len(self.nuevo) == 1):

            while(self.nuevo[0].paginas_libres > 0):

                if(self.marcos[self.cont_sistema] == None and self.nuevo[0].paginas_libres > 1):
                    self.marcos[self.cont_sistema] = 5
                    self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                    self.nuevo[0].paginas_libres -= 1
                    self.marcos_libres -= 1
                    self.nuevo[0].posiciones.append(self.cont_sistema)

                elif(self.marcos[self.cont_sistema] == None and self.nuevo[0].paginas_libres == 1):

                    if(self.nuevo[0].pagina_sobrante == None):
                        self.marcos[self.cont_sistema] = 5
                        self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                        self.nuevo[0].paginas_libres -= 1
                        self.marcos_libres -= 1
                        self.nuevo[0].posiciones.append(self.cont_sistema)
                        


                    elif(self.nuevo[0].pagina_sobrante > 0):
                        self.marcos[self.cont_sistema] = self.nuevo[0].pagina_sobrante
                        self.id_marcos[self.cont_sistema] = self.nuevo[0].id
                        self.nuevo[0].paginas_libres -= 1
                        self.marcos_libres -= 1
                        self.nuevo[0].posiciones.append(self.cont_sistema)
                        

                if(self.cont_sistema < 39):
                    self.cont_sistema += 1
                else:
                    self.cont_sistema = 0

            self.nuevo[0].T_Llegada = self.cont_tiempo
            self.nuevo[0].estado = "Listo"

            self.imprimir_memoria(self.nuevo[0], "blue")
            self.listo.append(self.nuevo[0])
            self.nuevo.pop(0)


        pass

    def descargar_proceso(self):
        while(self.ejecucion.paginas_libres < self.ejecucion.paginas):
            
            if(self.id_marcos[self.cont_sistema] == self.ejecucion.id):
                self.marcos[self.cont_sistema] = None
                self.id_marcos[self.cont_sistema] = None
                self.marcos_libres += 1
                self.ejecucion.paginas_libres += 1
            
            if(self.cont_sistema < 39):
                self.cont_sistema += 1
            else:
                self.cont_sistema = 0



    def imprimir_listos(self):
        headers = ["ID", "Tiempo Estimado", "Tiempo Ejecutado", "Tiempo en Espera", "Paginas"]

        self.ui.Listos_TW.setColumnCount(5)
        self.ui.Listos_TW.setRowCount(len(self.listo))
        self.ui.Listos_TW.setHorizontalHeaderLabels(headers)

        


        cont = 0
        for f in self.listo:
            id = QTableWidgetItem(str(f.id))
            tiempo = QTableWidgetItem(str(f.tiempo))
            tiempoT = QTableWidgetItem(str(f.T_Servicio))
            tiempoE = QTableWidgetItem(str(f.T_Espera))
            paginas = QTableWidgetItem(str(f.paginas))
      

            self.ui.Listos_TW.setItem(cont, 0, id)
            self.ui.Listos_TW.setItem(cont, 1, tiempo)
            self.ui.Listos_TW.setItem(cont, 2, tiempoT)
            self.ui.Listos_TW.setItem(cont, 3, tiempoE)
            self.ui.Listos_TW.setItem(cont, 4, paginas)
            cont += 1

            self.imprimir_memoria(f, "blue")

            
                

        




    def imprimir_Ejecucion(self):
        headers = ["ID", "Operacion", "Tiempo Esperado", "Tiempo Transcurrido", "Tiempo Restante", "Paginas"]

        self.ui.Ejecucion_TW.setColumnCount(6)
        self.ui.Ejecucion_TW.setRowCount(1)
        self.ui.Ejecucion_TW.setHorizontalHeaderLabels(headers)

        if(self.ejecucion == None):
            id = QTableWidgetItem("")
            operacion = QTableWidgetItem("")
            Tiempo_Esperado = QTableWidgetItem("")
            Tiempo_Transcurrido = QTableWidgetItem("")
            Tiempo_Restante = QTableWidgetItem("")
            paginas = QTableWidgetItem("")
        else:
            id = QTableWidgetItem(str(self.ejecucion.id))
            operacion = QTableWidgetItem(str(self.ejecucion.Return_operacion()))
            Tiempo_Esperado = QTableWidgetItem(str(self.ejecucion.tiempo))
            Tiempo_Transcurrido = QTableWidgetItem(str(self.ejecucion.T_Servicio))
            Tiempo_Restante = QTableWidgetItem(str(self.ejecucion.tiempoRestante))
            paginas = QTableWidgetItem(str(self.ejecucion.paginas))

            self.imprimir_memoria(self.ejecucion, "green")

        self.ui.Ejecucion_TW.setItem(0, 0, id)
        self.ui.Ejecucion_TW.setItem(0, 1, operacion)
        self.ui.Ejecucion_TW.setItem(0, 2, Tiempo_Esperado)
        self.ui.Ejecucion_TW.setItem(0, 3, Tiempo_Transcurrido)
        self.ui.Ejecucion_TW.setItem(0, 4, Tiempo_Restante)
        self.ui.Ejecucion_TW.setItem(0, 5, paginas)

        

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

            self.imprimir_memoria(f, "red")


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

    def imprimir_memoria(self, proceso,color):
        headers2 = ["Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5"]
        self.ui.Memoria_TW.setColumnCount(28)
        self.ui.Memoria_TW.setRowCount(11)
        self.ui.Memoria_TW.setHorizontalHeaderLabels(headers2)

        for x in proceso.posiciones:
            if(color == "white"):
                id_proceso = QTableWidgetItem("")
            else:
                id_proceso = QTableWidgetItem(str(self.id_marcos[x]))

            self.ui.Memoria_TW.setItem( (x + 4) % 11, (x + 4) // 11 * 7 + 1, id_proceso)

            for y in range(0, 5):
                fondo = QTableWidgetItem("")
                fondo.setBackgroundColor(QColor("white"))
                self.ui.Memoria_TW.setItem( (x + 4) % 11, (x + 4) // 11 * 7 + 2 + y, fondo)

            for y in range(0, self.marcos[x]):
                fondo = QTableWidgetItem("")
                fondo.setBackgroundColor(QColor(color))
                self.ui.Memoria_TW.setItem( (x + 4) % 11, (x + 4) // 11 * 7 + 2 + y, fondo)



    def iniciar_memoria(self):
        headers2 = ["Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5", "Marco", "ID", "1", "2", "3", "4", "5"]
        self.ui.Memoria_TW.setColumnCount(28)
        self.ui.Memoria_TW.setRowCount(11)
        self.ui.Memoria_TW.setHorizontalHeaderLabels(headers2)

        for i in range(0, 4):
            so = QTableWidgetItem("SO")
            self.ui.Memoria_TW.setItem( i , 1, so)

            for x in range(0, 5):
                fondo = QTableWidgetItem("")
                fondo.setBackgroundColor(QColor("gray"))
                self.ui.Memoria_TW.setItem( i, x + 2, fondo)

        

        for i in range(0, 44):
            num_marco = QTableWidgetItem(str(i + 1))

            self.ui.Memoria_TW.setItem( i % 11, i // 11 * 7, num_marco)
            QApplication.processEvents()





    def Mostrar_Tiempos(self):
        procesos = []
        procesos.extend(self.terminado)
        if(self.ejecucion != None):
            procesos.append(self.ejecucion)
        procesos.extend(self.bloqueado)
        procesos.extend(self.listo)
        procesos.extend(self.nuevo)

        self.ventana_tiempos = Tiempos(procesos)
        self.ventana_tiempos.show()
        
    def detener(self):
        global accion
        accion = 10


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
        elif(tecla == kb.KeyCode.from_char('n')):
            accion = 3
        elif(tecla == kb.KeyCode.from_char('b')):
            accion = 4

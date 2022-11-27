from C_Procesos_ui import Ui_Captura_Form
from PySide2.QtWidgets import QMessageBox, QWidget
from clases import Proceso
from Simulacion import Simulacion


class C_Procesos(QWidget):
    def __init__(self, procesos):
        
        super(C_Procesos, self).__init__()
        self.ui = Ui_Captura_Form()
        self.ui.setupUi(self)
        self.procesos = procesos
        self.cont = 1
        self.ids = []
        self.operaciones = {}
        self.ui.label_5.setText("Numero de Proceso: "+ str(self.cont))

        self.ui.CapturarP_Boton.clicked.connect(self.add_proceso)



    
    def add_proceso(self):
        operacion_cont = self.check_cb()
        if(operacion_cont == -1):
            QMessageBox.warning(self, "Error", "Se debe seleccionar 1 operacion")
            return
        elif(operacion_cont == -2):
            QMessageBox.warning(self, "Error", "Se debe seleccionar solo 1 operacion")
            return
        
        if(self.ui.Tiempo_SB.value() == 0):
            QMessageBox.warning(self, "Error", "El tiempo de ejecución debe ser mayor que 0")
            return
        
        if(self.check_div() == False):
            QMessageBox.warning(self, "Error", "No se puede dividir entre 0")
            return

        if(self.check_id() == False):
            QMessageBox.warning(self, "Error", "Este ID ya ha sido registrado")
            return
        
        self.ids.append(self.ui.ID_SB.value())
        proceso = Proceso(self.ui.Nombre_TE.toPlainText(), self.ui.ValorA_SB.value(), self.ui.ValorB_SB.value(), operacion_cont, self.ui.Tiempo_SB.value())
        self.operaciones[self.ui.ID_SB.value()] = proceso

        if(self.procesos == self.cont):
            self.simulacion()
        self.cont += 1
        self.clear()
        return

    def check_cb(self) -> int:
        operacion_cont = 0
        
        if(self.ui.Suma_CB.isChecked()):
            operacion_cont += 1
            operacion = 0
        if(self.ui.Resta_CB.isChecked()):
            operacion_cont += 1
            operacion = 1
        if(self.ui.Multiplicacion_CB.isChecked()):
            operacion_cont += 1
            operacion = 2
        if(self.ui.Division_CB.isChecked()):
            operacion_cont += 1
            operacion = 3
        if(self.ui.Modulo_CB.isChecked()):
            operacion_cont += 1
            operacion = 4
        if(self.ui.Potencia_CB.isChecked()):
            operacion_cont += 1
            operacion = 5
        if(operacion_cont == 0):
            return -1
        elif(operacion_cont > 1):
            return -2
        return operacion

    def check_id(self):
        new_id = self.ui.ID_SB.value()
        if(new_id in self.ids):
            return False
        return True

    def check_div(self):
        if(self.ui.Division_CB.isChecked()):
            if(self.ui.ValorB_SB.value() == 0):
                return False
        return True


    def clear(self):
        self.ui.label_5.setText("Numero de Proceso: "+ str(self.cont))
        self.ui.Nombre_TE.setText("")
        self.ui.ValorB_SB.setValue(0)
        self.ui.ValorA_SB.setValue(0)
        self.ui.Tiempo_SB.setValue(0)
        self.ui.ID_SB.setValue(0)
        return

    def simulacion(self):
        self.hide()
        self.ventana = Simulacion(self.ids, self.operaciones)
        self.ventana.show()
        pass



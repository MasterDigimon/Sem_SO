from PySide2.QtWidgets import QMainWindow, QMessageBox, QWidget
from N_Procesos_ui import Ui_MainWindow
from C_Procesos import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Capturar_Boton.clicked.connect(self.def_numero)
        return


        
    def def_numero(self):
        if(self.ui.Procesos_SB.value() == 0):
            QMessageBox.warning(self, "Error", "No se pueden asignar 0 procesos")
        else:
            self.hide()
            self.ventana = C_Procesos(self.ui.Procesos_SB.value())
            self.ventana.show()
            pass
        pass
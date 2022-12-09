

class Proceso():
    def __init__(self,_id, _A, _B, _operacion, _tiempo):
        self.id = _id
        self.valorA = _A
        self.valorB = _B
        self.operacion = _operacion
        self.tiempo = _tiempo
        self.tiempoRestante = _tiempo
        self.tiempoTranscurrido = 0
        self.resultado = None


        self.T_Bloqueado = 0

        self.T_Llegada = 0
        self.T_Retorno = None
        self.T_Respuesta = None
        self.T_Espera = 0
        self.T_Servicio = None
        self.T_Finalizacion = None
        
        return

    def iniciar_sim(self):
        self.tiempoRestante = self.tiempo
        self.tiempoTranscurrido = 0

        self.T_Bloqueado = 0

        self.T_Espera = 0


    def calcular_resultado(self, error):
        if(error):
            self.resultado = "Error"

        elif(self.operacion == 0):
            self.resultado =  str(self.valorA + self.valorB)
        
        elif(self.operacion == 1):
            self.resultado = str(self.valorA - self.valorB)

        elif(self.operacion == 2):
            self.resultado = str(self.valorA * self.valorB)

        elif(self.operacion == 3):
            self.resultado = str(round(self.valorA / self.valorB, 2))

        elif(self.operacion == 4):
            self.resultado = str(self.valorA % self.valorB)

        elif(self.operacion == 5):
            potencia = 1
            for i in range(0, int(self.valorB)):
                potencia *= self.valorA
            self.resultado = str(potencia)
        
        self.T_Retorno = round(self.T_Finalizacion - self.T_Llegada, 2)
        self.T_Servicio = self.tiempoTranscurrido

    def Return_operacion(self):
        if(self.operacion == 0):
            return str(self.valorA) + " + " + str(self.valorB)
        elif(self.operacion == 1):
            return str(self.valorA) + " - " + str(self.valorB)

        elif(self.operacion == 2):
            return str(self.valorA) + " x " + str(self.valorB)

        elif(self.operacion == 3):
            return str(self.valorA) + " / " + str(self.valorB)

        elif(self.operacion == 4):
            return str(self.valorA) + " % " + str(self.valorB)

        elif(self.operacion == 5):
            return str(self.valorA) + " ^ " + str(self.valorB)



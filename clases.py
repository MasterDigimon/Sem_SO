

class Proceso():
    def __init__(self,_id, _A, _B, _operacion, _tiempo):
        self.id = _id
        self.valorA = _A
        self.valorB = _B
        self.operacion = _operacion
        self.tiempo = _tiempo
        self.tiempoRestante = _tiempo
        self.tiempoTranscurrido = 0
        self.error = None
        return

    def iniciar_sim(self):
        self.tiempoRestante = self.tiempo
        self.tiempoTranscurrido = 0


    def calcular_resultado(self) -> float:
        if(self.operacion == 0):
            return self.valorA + self.valorB
        
        elif(self.operacion == 1):
            return self.valorA - self.valorB

        elif(self.operacion == 2):
            return self.valorA * self.valorB

        elif(self.operacion == 3):
            return round(self.valorA / self.valorB, 2)

        elif(self.operacion == 4):
            return self.valorA % self.valorB

        elif(self.operacion == 5):
            potencia = 1
            for i in range(0, int(self.valorB)):
                potencia *= self.valorA
            return potencia
        pass

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



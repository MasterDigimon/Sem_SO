

class Proceso():
    def __init__(self,_id, _nombre, _A, _B, _operacion, _tiempo):
        self.id = _id
        self.nombre = _nombre
        self.valorA = _A
        self.valorB = _B
        self.operacion = _operacion
        self.tiempo = _tiempo
        self.tiempoRestante = _tiempo
        self.tiempoTranscurrido = 0
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
            return self.valorA / self.valorB

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
            return "Suma"
        elif(self.operacion == 1):
            return "Resta"

        elif(self.operacion == 2):
            return "Multiplicacion"

        elif(self.operacion == 3):
            return "Division"

        elif(self.operacion == 4):
            return "Modulo"

        elif(self.operacion == 5):
            return "Potencia"
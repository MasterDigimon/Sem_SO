import random

class Proceso():
    def __init__(self, _id) -> None:
        self.id = _id
        self.valorA = None
        self.valorB = None
        self.operacion = None
        self.tiempo = random.randint(6, 16)
        self.tiempoRestante = self.tiempo
        self.resultado = None
        self.estado = "Nuevo"


        self.memoria = None
        self.paginas = 0
        self.pagina_sobrante = None
        self.paginas_libres = 0
        self.posiciones = []


        self.T_Bloqueado = 0

        self.T_Llegada = None
        self.T_Retorno = None
        self.T_Respuesta = None
        self.T_Espera = 0
        self.T_Servicio = 0
        self.T_Finalizacion = None

        self.genOperacion()

        return

    def iniciar_sim(self):
        self.tiempoRestante = self.tiempo
        self.T_Servicio = 0

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


    def genOperacion(self):
        self.operacion = random.randint(0, 5)
        self.memoria = random.randint(6, 28)
        #Suma - 0, Resta - 1, Multiplicacion - 2, Division - 3, Modulo - 4, Potencia - 5

        self.paginas += self.memoria // 5
        if(self.memoria % 5 > 0):
            self.pagina_sobrante = self.memoria % 5
            self.paginas += 1

        self.paginas_libres = self.paginas

        if(self.operacion == 0):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(0, 100)

        elif(self.operacion == 1):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(0, 100)

        elif(self.operacion == 2):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(0, 100)

        elif(self.operacion == 3):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(1, self.operacion)

        elif(self.operacion == 4):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(1, self.operacion)

        elif(self.operacion == 5):
            self.valorA = random.randint(0, 100)
            self.valorB = random.randint(0, 5)

    def export(self):
        cadena = str(self.id) + "_" + str(self.valorA) + "_" + str(self.valorB) + "_" + str(self.operacion) + "_" + str(self.tiempo) + "_" + str(self.tiempoRestante) 
        cadena += self.estado + "_" + str(self.memoria) + "_" + str(self.T_Llegada) + "_" + str(self.T_Respuesta) + "_" + str(self.T_Espera) + "_" + str(self.T_Servicio)
        cadena += '\n'
        return cadena

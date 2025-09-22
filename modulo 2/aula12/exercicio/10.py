class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
class Carro:
    def __init__(self, modelo ,potencia_carro):
        self.modelo = modelo
        self.motor = Motor(potencia_carro)
    def exibir(self):
        print(f"O carro {self.modelo} tem motor de {self.motor.potencia} de cavalos de potencia.")


carro = Carro("Fusca", 100)
carro.exibir()
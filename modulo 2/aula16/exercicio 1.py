class Carro:
    def __init__(self, ):
        pass
    def ligar(self):
        print("O motor ligou")

class Motor:
    def __init__(self):
        self.motor = Carro()
    def ligar_carro(self):
        self.motor.ligar()
    
m = Motor()
m.ligar_carro()
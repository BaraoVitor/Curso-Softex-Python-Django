class Carro:
    def __init__(self, modelo:str, combustivel:int):
        self.modelo = modelo
        self.combustivel = combustivel
        self.distancia_percorrida = 0
    def abastecer(self):
        mais = int(input("Quanto vc quer abastecer?\nR:"))
        self.combustivel += mais
    def dirigir(self):
        distancia = int(input("Qual a distacia percorrida?\nR:"))
        consumo = distancia /10
        if consumo <= self.combustivel:
            self.combustivel -= consumo
            print(f"O seu carro {self.modelo} andou {distancia}")
            self.distancia_percorrida += distancia
            
        else:
            print("O combustivel insuficiente!")
        
        if self.distancia_percorrida >= 10000:
            print("Parabens vc chegou no seu destino")
            return True
        return False
    
    def perguntas(self):
        while True:
            per = input("Digite 1-abastecer ou 2-percorrer?\nR:")
            if per == "1":
                self.abastecer()
            elif per == "2":
                self.dirigir()
            else:
                print("Numero Indisponivel")
                break

ca = Carro("Ford", 100)
ca.perguntas()
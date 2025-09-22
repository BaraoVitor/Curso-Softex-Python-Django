

class Banco:
    def __init__(self, titular:str, saldo:int):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor:float):
        
        if valor > 0:
            self.saldo += valor
            print("\033[92m"f"Deposito do {valor} realizado com sucesso!""\033[0m")
        
        else:
            print("\033[91m""Deposito invalido""\033[0m")
        print("\033[94m"f"Seu saldo atual:{self.saldo}""\033[0m")
    
    def sacar(self,valor:float):
        
        if valor <= self.saldo:
            self.saldo -= valor
            print("\033[92m"f"Seu saque foi realizado com sucesso de {valor}""\033[0m")
        
        else:
            print("\033[91m"f"Saldo insuficiente! Seu saldo e de {self.saldo}""\033[0m")
        
    def loop(self):
        while True:
            print("Escolha uma opçao: \n1- Depositar\n2-Sacar\n3-Sair")
            es = input("R:")
            
            if es == "1":
                valor = float(input("\033[94m""Digite o valor do deposito:""\033[0m"))
                self.depositar(valor)
            
            elif es == "2":
                valor = float(input("\033[94m""Digite o valor do saque:""\033[0m"))
                self.sacar(valor)
            
            elif es == "3":
                print("\033[94m""Bye""\033[0m")
                break
            
            else:
                print("\033[91m""Opçao invalida tente novamente""\033[0m")


co = Banco("Vitor", 10000)
co.loop()
        
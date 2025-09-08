class Contador:
    def __init__(self):
        self.lista = [1,5,2,8,5,3,2,2]
    
    def numero(self):
        numeroa = int(input("Digite o numero a ser procurado:"))
        num = self.lista.count(numeroa)
        print(f"Quantidade e {num}")

con = Contador()
ko = con.numero()
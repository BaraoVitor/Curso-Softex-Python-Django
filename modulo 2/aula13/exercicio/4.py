class Produto:
    def __init__(self,item:str, preco:int):
        self.item = item
        self.preco = preco
    def imprimir(self):
        print(f"Seu produto e {self.item} o preço dele e R${self.preco}")

pe = Produto("Caderno", 15.50)
pe2 = Produto("Caneta", 3.00)
pe.imprimir()
print("-"*20)
pe2.imprimir()
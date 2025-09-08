class lanchonete:
    def __init__(self, preco ):
        self.preco = preco
    def calc(self):
        while True:
            cupom = 2211
            lanche = "hambuguer"
            nome = input("Digite o nome do produto:")
            if nome not in lanche:
                print("Digite de novo o produto")
            else:
                tem = input("Voce tem um cupom de desconto?\n")
                if tem == "sim":
                    codigo = int(input("Digite o codigo:"))
                    if  cupom == codigo:
                        desconto = self.preco - 9
                        print(f"Seu valor ficou em {desconto} do seu {lanche}") 
                        break
                else:
                    print(f"O valor do seu {lanche} ficou em {self.preco}")
                    break

produto = lanchonete(50)
produto.calc()

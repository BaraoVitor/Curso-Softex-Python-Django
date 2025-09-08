class Analise:
    def __init__(self):
        self.vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1) ,("Fone", 45,1), ("Webcam", 75.20 , 2)]
    def dados(self):
        venda_filtra = list()
        produto = set()
        for produto, valor, qtd in self.vendas:
            
            preco = list(self.vendas)
            print(f"Seus preços{preco}")

ve = Analise()
ve.dados()
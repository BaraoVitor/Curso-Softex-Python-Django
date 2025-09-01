class CoresIGuais:
    def __init__(self):
        self.lista1 = ["Vermelho", "azul", "verde", "amarelo"]
        self.lista2 = ["verde", "roxo", "azul", "preto"]
        self.lista = []
    def achar(self):
        for i in self.lista1:
            if i in self.lista2:
                self.lista.append(i)
                print(f"Lista:{self.lista}")
            
            
cor = CoresIGuais()
cor.achar()

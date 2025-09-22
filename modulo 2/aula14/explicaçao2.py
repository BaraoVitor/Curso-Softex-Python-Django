class Produto:
    def __init__(self, nome,preco):
        self.__preco = preco
        self.nome = nome
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def _verifica_valor(self, valor):
        if valor >=0:
            self.__preco = valor
        else:
            print("Valor incorreto!")
    def _verifica_valor(self,valor):
        return valor >=0

caneta = Produto('Caneta Azul',10)
print(caneta.preco)
caneta.preco = -10
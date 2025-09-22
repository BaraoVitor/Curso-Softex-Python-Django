class Produto:
    def __init__(self, nome,preco):
        self.__preco = preco
        self.nome = nome
    def get_preco(self):
        return self.__preco
    def set_preco(self, valor):
        if valor >=0:
            self.__preco = valor
        else:
            print("Valor incorreto!")
    def _verifica_valor(self,valor):
        return valor >=0

caneta = Produto('Caneta Azul',2.50)
print(caneta.set_preco(-10))
print(caneta.get_preco())
class MoldePessoa:
    def __init__(self, nome:str, idade: int):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Ola meu nome e {self.nome} e eu tenho {self.idade} anos")


pe = MoldePessoa("Joao", 25)
pe2 = MoldePessoa("Maria", 30)

pe.apresentar()
print("-"*20)
pe2.apresentar()

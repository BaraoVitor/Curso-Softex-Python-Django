class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
    
    def apresentar(self):
        print(f"Seu nome {self.nome}.Sua idade {self.idade}.")
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Seu nome {self.nome}.Sua idade {self.idade}.Seu curso e {self.curso}")


m = Pessoa("Vitor", 23)
a = Estudante("Thiago", 90,"Nao sei")

lista = [a, m]

for i in lista:
    i.apresentar()

    
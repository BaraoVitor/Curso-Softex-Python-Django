class Animal:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
    def som (self):
        print("Metodo da Super")

class Cachorro(Animal):
    def __init__(self, nome , idade , raca):
        super().__init__(nome,idade)
        self.raca = raca

    def som (self):
        print("Metodo da class sub(cachorro)")

class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie


cao = Cachorro("Rex", 4, "Golden")
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.som()


Gato = Gato("Felix", 2, "persa")
print(Gato.nome)
print(Gato.idade)
print(Gato.especie)
Gato.som()
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def validador(self, novo_nome:str):
        if isinstance(novo_nome, str) and not novo_nome:
            self.nome = novo_nome
        else:
            print("Erro! Nao deve estar nulo")
    @property
    def idade(self):
        return self.idade
    @idade.setter
    def validador_idade(self, idade_nova:int):
        if isinstance(idade_nova, int) and idade_nova >0:
            self._idade = idade_nova
        else:
            print("Tera que ser positivo")

nova = Pessoa("Vitor", 34)
print(nova.nome)
nova.idade = 23
print(nova.idade)
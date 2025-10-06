from estudante import Estudante

class Escola:
    def __init__(self):
        self.lista = []
    
    def adicionar_estudante(self, nome, idade, matricula):
        self.nova = Estudante(nome, matricula, idade)
        self.nova_lista = self.lista.append(self.nova)    
    def mostrar_relatorio(self):
        for nome, matri, notas in self.nova_lista:
            print(f"Seu nome e {nome} sua matricula e {matri} sua nota e {notas}.")


m = Escola("Vitor", 12, 1212)
m.mostrar_relatorio()


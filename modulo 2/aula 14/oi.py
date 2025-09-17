import random as rd

class Personagem:
    def __init__(self, nome, vida, ataque, pocoes = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes
        self.defendendo = False
    
    def atacar (self, alvo):
        dano = self.ataque
        if rd.random ()<0.2:
            dano
            
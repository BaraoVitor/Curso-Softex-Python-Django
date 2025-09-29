import math

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class SegmentoDeReta:
    def __init__(self, ponto1, ponto2):
        self.ponto = Ponto(ponto1,ponto2)
    
    def calcular_comprimento(self):
        resul = math.sqrt(self.ponto.x*self.ponto.x + self.ponto.y*self.ponto.y)
        print(f"Seu resultado e {resul}")

m = SegmentoDeReta(2,4)
m.calcular_comprimento()
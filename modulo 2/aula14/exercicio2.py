import math
class Ciculo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self,novo):
        if novo > 0:
            self._raio = novo

        else:
            print("Esse numero nao e positivo")
    def calcular_area(self):
        calc = math.pi * (self._raio ** 2)
        return calc

oi = Ciculo(-10)
oi.raio = -5
print(oi.calcular_area())
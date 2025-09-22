class retangulo:
    def __init__(self,base:int,altura:int):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        calc = self.base * self.altura
        print(f"O calculo deu{calc}")
    def calculo_perimetro(self):
        calc = 2*(self.base + self.altura)
        print(f"O calculo deu {calc}")

re = retangulo(12,12)
es = input("Digite 1- para calcular a Area 2- para calcular a Perimetro:\nR:")
if es == "1":
    re.calcular_area()
elif es == "2":
    re.calculo_perimetro()
else:
    print("Numero digitado incorreto")
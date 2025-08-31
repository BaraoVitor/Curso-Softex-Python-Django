class Validacao:
    def __init__(self, a: str, b: str, c: str):
        self.a = a
        self.b = b
        self.c = c

    def verificador(self):
        while True:
            if self.a.isdigit() and self.b.isdigit() and self.c.isdigit():
                self.a = int(self.a)
                self.b = int(self.b)
                self.c = int(self.c)
                break
            else:
                print("Digite os valores novamente (apenas números inteiros positivos):")
                self.a = input("A: ")
                self.b = input("B: ")
                self.c = input("C: ")

    def soma(self):
        a = self.a
        b = self.b
        c = self.c

        if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
             print("É um triângulo")

        else:
            print("Não é triângulo")

var = Validacao("a", "2", "3")
var.verificador()
var.soma()

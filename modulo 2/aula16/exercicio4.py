class Teclado:
    def __init__(self):
        pass
    def ligar(self):
        print("O teclado foi ativado")
class Mouse:
    def __init__(self):
        pass
    def ligar(self):
        print("O Mouse foi ativado")
class Monitor:
    def __init__(self):
        pass
    def ligar(self):
        print("O Monitor foi ligado")
class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.Monitor = Monitor()
        self.Mouse = Mouse()
    def ligar_computador(self):
        self.teclado.ligar()
        self.Monitor.ligar()
        self.Mouse.ligar()

m = Computador()
m.ligar_computador()

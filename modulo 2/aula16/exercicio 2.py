class GraoDeCafe:
    def __init__(self):
        pass
    def moer(self):
        print("os graos de cafe forma moidos")
class Agua:
    def __init__(self):
        pass
    def aquecer(self):
        print("A agua esta aquecida")
class Cafeteira:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()
    def preparar_cafe(self):
        self.grao.moer()
        self.agua.aquecer()
        print("Preparando cafe")

m = Cafeteira()
m.preparar_cafe()
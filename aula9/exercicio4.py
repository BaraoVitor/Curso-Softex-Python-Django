class Coletor:
    def __init__(self):
        self.stop = "-1"
        self.lista = []
    def verifi(self):
        while True:
            numero = input("Digite o numero:")
            if numero.isdigit():
                self.lista.append(numero)
                print("E um digito")
            elif numero == "-1":
                break

co = Coletor()
co.verifi()
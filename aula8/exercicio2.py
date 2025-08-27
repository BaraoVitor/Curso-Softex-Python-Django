class criptografia:
    def __init__(self, frase):
        self.frase = frase.lower()
    def codificar(self):
        codi = self.frase
        cripto = codi.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
        print(f"Seu codigo e {cripto}")
        codigo = codi.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")
        print(f"Seu codigo voltou a o normal {codigo}")
a = criptografia("Arara")
a.codificar()

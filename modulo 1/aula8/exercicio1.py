
class verificar:
    def __init__(self, numero):
        self.numero = numero
    def numero_telefone(self):
            cont = len(self.numero)
            if self.numero.isdigit() and cont == 11:
                print("Seu numero tem 11 caracteres")
                for c in self.numero:
                    count = 0
                    for b in self.numero:
                        if b == c:
                             count +=1
                    if count == 5:
                         print("Seu numero esta igual")
                         break
            else:
                print("Digite de novo")
            
            

            


ver = verificar("21332132122")
ver.numero_telefone()
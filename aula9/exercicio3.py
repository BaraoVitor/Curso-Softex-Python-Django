class Primo:
    def __init__(self):
        self.primos = [1,2,3,4,5,6,7,8,9,10]
        self.pimo2 = []
    def verificador(self):
        for i in range(0,11):
            eprimo = True
            for e in self.primos:
                    verificador = i % e
                    if verificador == 0:
                        eprimo = False
                    else:
                         self.pimo2.append(e)

        print("ele e primo",self.pimo2)
                         
                         
                         
pi = Primo()
pi.verificador()
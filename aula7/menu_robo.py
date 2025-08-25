'''
posiçao = 0
while True:
    print("1-Avançar: \n 2-Recuar:  \n 3-Status: \n 4- Desligar")
    m = int(input("Digite o movimento: "))
    if m == 1:
        posiçao +=1
        print(f"A posiçao do robo e {posiçao}")
    elif m == 2:
        posiçao -=1
        print(f"A posiçao do robo e {posiçao}")
    elif m == 3:
        print(f"A posiçao do robo e {posiçao}")
    elif m ==4:
        print(f"A posiçao do robo e {posiçao}")
        break
    else:
        print(f"Vc nao digitou a posiçao errada.")
'''
class robo:
    def __init__(self):
        self.posicao = 0
    def numeros (self):
        while True:
            print("1-Avançar: \n 2-Recuar:  \n 3-Status: \n 4- Desligar")
            movimento = int(input("Digite o movimento: "))
            if movimento == 1:
                self.posicao +=1
                print(f"\nA posiçao do robo e {self.posicao}\n")
            elif movimento == 2:
                self.posicao -=1
                print(f"\nA posiçao do robo e {self.posicao}\n")
            elif movimento == 3:
                print(f"\nA posiçao do robo e {self.posicao}\n")
            elif movimento ==4:
                print(f"\nA posiçao do robo e {self.posicao}\n")
                break
            else:
                print(f"Vc nao digitou a posiçao errada.")
robot = robo()
robot.numeros()
class Agenda:
    def __init__(self):
        self.contatos = {}
    def funcionalidades (self):
        while True:
            print("O que vc quer \n" "1 - Adicionar contato" "2 - Buscar contato" "3 - Sair")
            m = input("Digite aqui:")
            if m == "1":
                nome = input("Digite o nome:")
                a = input("Qual contato?\n")
                self.contatos[nome] = a
                
            elif m == "2":
                b = input("Digite o contato:")
                if b in self.contatos:
                    print("Contato Encontrado")
                else:
                    print("Digite de novo")
            else:
                print("Tchau")
                break

o = Agenda()
o.funcionalidades()

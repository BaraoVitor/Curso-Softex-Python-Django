
class Livros:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor



class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar(self):
        m = input("Qual livro voce quer adicionar?\nR:")
        if isinstance(m, str):
            self.acervo.append(m)
        elif m.isdigit():
            print("Nao aceitamos numeros.")
            return
        autor = input("Digite o autor:")
        if autor.isdigit():
            print("Nao digite numeros")
        
        livro = Livros(m ,autor)
        self.acervo.append(livro)
        print(f"Livro {livro} adicionado")

    def lista(self):
        print("\n Tem esses livros")
        if not self.acervo:
            print("Vazia")
        else:
            for livro in self.acervo:
                print("-", livro)
bi = Biblioteca()
while True:
    print("Digite 1- para adicionar\n 2- listar \n 3- para sair")
    es = input("R:")
    if es == "1":
        bi.adicionar()
    elif es == "2":    
        bi.lista()
    elif es == "3":
        break
    else:
        print("Numero invalido")
    

class Livros:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"O livro '{self.titulo}' é do autor {self.autor}"


class Biblioteca:
    def __init__(self):
        self.acervo = []

 
    def adicionar(self, livro: Livros):
        self.acervo.append(livro)
        print(f"Livro {livro} adicionado com sucesso!")
    def adicionar_usuario(self):
        titulo = input("Digite o título do livro: ").strip()
        if not titulo or titulo.isdigit():
            print("Título inválido. Não pode ser vazio ou número.")
            return

        autor = input("Digite o autor: ").strip()
        if not autor or autor.isdigit():
            print("Autor inválido. Não pode ser vazio ou número.")
            return

        livro = Livros(titulo, autor)
        self.adicionar(livro)
    def listar(self):
        if not self.acervo:
            print("O acervo está vazio.")
            return
        print("\nLivros no acervo:")
        for livro in self.acervo:
            print("-", livro)
biblioteca = Biblioteca()

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Sair")
    escolha = input("R: ").strip()

    if escolha == "1":
        biblioteca.adicionar_usuario()
    elif escolha == "2":
        biblioteca.listar()
    elif escolha == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")

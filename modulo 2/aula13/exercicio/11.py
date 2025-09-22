class Livros:
    def __init__(self,titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"O livro {self.titulo} e do autor {self.autor}"

class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar(self, livro:Livros):
        self.acervo.append(livro)
    
    def listar(self):
        for livro in self.acervo:
            print(livro)

livro1 = Livros("titulo1", "autor1")
livro2 = Livros("titulo2", "autor2")
biblioteca = Biblioteca()
biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.listar()
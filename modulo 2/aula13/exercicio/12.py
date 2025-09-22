class Filme:
    def __init__(self, titulo:str, diretor:str, ano:int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
    def __str__(self):
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor:{self.diretor}"

fil = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)
print(fil)
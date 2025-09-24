class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.deracao = duracao_seg
    
    def exibir(self):
        print(f"O titulo e {self.titulo} e o {self.deracao}.")

class Musica(Midia):
    def __init__(self,titulo, duracao_seg, nome):
        super.__init__(titulo, duracao_seg)
        self.nome = nome
    def exibir(self):
        print(f"O titulo e {self.titulo} e o {self.deracao}. O nome do artista{self.nome}")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao
    def exibir(self):
        print(f"O titulo e {self.titulo} e o {self.deracao}. O nome do artista{self.nome}. O nome da {self.resolucao}")



musi = Musica("a fogueira", 98, "Daniel")
musi1 = Musica("A foqueira", 0 , "7k")

dicionarios = {"musica":[] ,"videos":[]}
dicionarios["musica"].append(musi)
dicionarios["videos"].append(musi1)

print(dicionarios)
for i in dicionarios():
    for u in i:
        u.exibir()
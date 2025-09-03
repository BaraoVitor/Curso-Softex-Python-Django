class Site:
    def __init__(self):
        self.estoqueprin = [("Camiseta", 101), ("Calça", 102), ("Bone", 103), ("Tênis", 104)]
        self.estoqueon = [("Bone", 103), ("Camisa POLO", 105), ("Calça", 102), ("Chinelo", 106)]
    
    def disponivel(self):
        loja = set(self.estoqueprin)
        onlin = set(self.estoqueon)
        igual = loja.intersection(onlin)
        
        apenas_loja = loja.difference(onlin)
        apenas_site = onlin.difference(loja)
        print(f"\nLoja e no site{igual}\n"  f"Apenas loja {apenas_loja}\n"  f"Apenas site{apenas_site}\n")

da = Site()
da.disponivel()
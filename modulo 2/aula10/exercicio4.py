class Notas:
    def __init__(self):
        self.notas = [("Ana" ,9.5), ("João", 8.0), ("Maria",10.0),("Pedro", 7,5), ("Ana",10.0), ("Carlos",6.5)]
    def notas_oi(self):
        notas_maiores = set()
        for nome, nota in self.notas:
            if nota == 10:
                notas_maiores.add(nota)                
                print(f"A maior nota e {notas_maiores}")
                print(f"NADA {nome}")
            



no = Notas()
no.notas_oi()
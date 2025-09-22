class Funcionario:
    percentual_bonus = 1.10
    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario
    
    def aplicar_bonus(self):
        total = self.salario * Funcionario.percentual_bonus
        print(f"O salario da(o) {self.nome} e de {total:.2f}")
    
f1 = Funcionario("Daniel", 1000.10)
f2 = Funcionario("Vitor", 19999.90)
f1.aplicar_bonus()
f2.aplicar_bonus()
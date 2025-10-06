from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int, matricula, ):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.mateira = []
    @property
    def metodo(self):
        return self.materia
    @metodo.getter
    def metodo(self, materia, nota):
        aula = materia.get(materia)
        if aula:
            aula.append(materia)
        else:
            materia[materia] = [nota] 
    
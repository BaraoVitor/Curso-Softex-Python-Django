class Login:
    def __init__(self):
        self.acessos = [("Pedro", "Suceso"), ("Ana", "Falha"), ("Maria", "Sucesso"), ("Pedro","Falha"), ("Ana", "Falha")]
    
    def verificar(self):
        acesso_sucesso = set()
        acessos_so_falha = set()
        
        for nome , status in self.acessos:
            if status == "sucesso":
              acesso_sucesso.add(nome)
        
            elif self.acessos == "falha":
                acessos_so_falha.add(nome)
        sofalha = acessos_so_falha.difference(acesso_sucesso)
        print(f"Usuarios com falha{sofalha}")
        print(f"Usuarios com sucessos {acesso_sucesso}")
        
        
        
lo = Login()
lo.verificar()
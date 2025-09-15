def cadastrar_localidade(bairros: dict) -> None:
    '''Permite ao atendente cadastrar um novo bairro'''
    nome_bairro = input("Digite o nome do bairro (identificador)").lower()
    if nome_bairro in bairros:
        print("Erro! Bairro ja cadastrado")
        return
    try:
        nome_completo = input("Digite o nome completo do bairro: ").strip()
        valor_frete = float(input(f"Digite o valor do frete do bairro {nome_completo}:"))

        if nome_bairro and valor_frete >= 0 and nome_completo:
            bairros [nome_bairro] = {"nome": nome_completo, "frete": valor_frete}
            print(f"Localidade{nome_completo} com frete de R${valor_frete:.2f} cadastrado com sucesso.")

        else:
            print("Dados invalidos.O cadastro nao foi realizado.")
            
    except ValueError:
        print("Entrada invalida! O valor do frete deve ser um numero.")
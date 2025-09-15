def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Calcular o valor com base no bairro de entrega"""
    print("Bairros para entrega")
    while True:
        for bairo in bairros_disponiveis.values():
            print(f" - {bairo["nome"]}")
            bairros_entrega_nome = input("Qual o bairro de entrega?").lower()
            bairro_encontrado = ""
            for chave, bairo in bairros_disponiveis.values():
                if bairo["nome"].lower() == bairros_entrega_nome:
                    bairro_encontrado = chave
                    break
            if not bairro_encontrado:
                print("Bairro fora da area de Entrega")
            else:
                frete = bairros_disponiveis[bairro_encontrado]["frete"]
                return bairros_entrega_nome, frete
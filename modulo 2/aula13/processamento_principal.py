
def processar_pedidos(paes_disponiveis: dict) -> tuple[dict, int, float, dict] | None:
    ''' 
    Processa o pedido do cliente, verifica o estoque e calcula o frete.
    Retorna uma tupla com o dicionario do pao, quantidade,
    valor total da compra e o dicionario atualizado de paes.
    '''

    print("Temos os seguintes pães:")
    for chave, pao in paes_disponiveis.values():
        print(f" - {pao["nome"]}")
    
    escolha_pao = input("Qual pao voce deseja?\nR:").lower()
    pao_encontrado = ""

    for chave, pao in paes_disponiveis.items():
        if pao["nome"].lower() == escolha_pao:
            pao_encontrado = chave
            break
    if not pao_encontrado:
            print("Opçao Invalida!")
            return None
    
    pao_escolhido = paes_disponiveis[pao_encontrado]

    try:
        quantidade = int(input(f"Digite a quantidade do {pao_escolhido["nome"]}"))

        if quantidade <= 0:
            print("Quantidade invalida!")
            return None
    
    except ValueError:
        print("Error!Qunatidade deve ser um numero inteiro.")
        return None
    if quantidade > pao_escolhido["quantidade"]:
        print(f"Infelizmente so tenho {pao_escolhido["quantidade"]} unidade deste pao.")
        return None
    
    paes_disponiveis[pao_encontrado]["quantidade"] -= quantidade
    valor_compra = quantidade * pao_escolhido["valor"]
    return pao_escolhido, quantidade, valor_compra, paes_disponiveis


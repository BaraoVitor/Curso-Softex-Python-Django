def dados() -> dict:
    """Carregar e retornar os dados de produtos, frete e funcionarios"""
    return{
        "atendente" : "Maria",
        "paes":{
            "frances":{"nome":"Pão frances", "Valor": 0.50,"Quantidade":15},
            "Daces":{"nome":"Pão doce", "Valor": 5.00,"Quantidade":20},
            "Forma":{"nome":"Pão de forma", "Valor": 5.99,"Quantidade":10},
        },
        "bairros":{ 
            "barroco":{"nome":"Barroco","Frete":5.00},
            "Sao jose": {"nome":"Sao jose", "Frete": 15.00},
        },
        "codigo_venda_base":95875
    }
def obter_dados_cliente() -> dict:
    """Solicita e retorna os dados do cliente"""
    nome = input("Informe seu nome:")
    return {"nome": nome}
def solicitar_forma_pagamento() -> str:
    """Solicitar e retornar a forma de pagamento escolhida"""
    while True:
        pagamento = input("Escolha a forma de pagamento(1-Dinehiro, 2-Cartao)")
        if pagamento =="1":
            return"Dinheiro"
        elif pagamento == "2":
            return "Cartao"
        else:
            print("Forma de pagamento invalida")

def gerar_codigo_venda(codigo_base:int) -> int:
    """Gera e retorna o codigo de venda"""
    return codigo_base + 1 

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

def cadastrar_produto (estoque:dict)-> None:
    """Permite ao atende cadastrar um novo produto """
    nome_produto = input("Digite o nome do novo produto(identificador)").lower().strip()

    if nome_produto in estoque:
        print("Error! Produto ja cadastrado com este identificador!!!")
        return 
    
    try: 
        nome_completo = input("Digite o nome completo do produto: ")
        valor = input(float("Digite o valor do novo produto:"))
        quantidade = int(input("Digite a quantidade inicial do produto:"))
        
        if nome_produto and valor > 0 and quantidade > 0:
            estoque[nome_completo] = {"nome":nome_completo, "valor":valor,"quantidade":quantidade}
            print(f"Produto{nome_completo} cadastrado com sucesso!")
        
        else:
            print("Error! Dados invalidos.")
    except ValueError:
        print("Entrada de dados invalida")

def atualizar_produto(estoque: dict) -> None:
    """Permite ao atendente atualizar um produto exitente"""
    nome_produto = input("Digite o nome do produto para atualizar (identificador): ").lower()

    if nome_produto not in estoque:
        print("Produto nao cadastrado")
        return
    
    print(f"Produto '{estoque[nome_produto]}' selecionado.")
    escolha = input("O que deseja atualizar? \n \
          1- Valor; \n\
          2 - quantidade")
    
    try:
        if escolha == "1":
            novo_valor = float(input("Digite o novo valor do produto:"))
            if novo_valor > 0:
                estoque[ nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R${novo_valor:.2f}")
            else:
                print("Valor invalido.")
        elif escolha == "2":
            nova_quantidade = int(input("Digite a nova quantidade do produto "))
            if nova_quantidade > 0:
                estoque[nome_produto]["quantidade"] += nova_quantidade
                print(f"Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")
            else:
                print("Quantidade invalida!")
        else:
            print("Erro! Opção invalida.")
    except ValueError:
        print("Error! Digite apenas numeros")


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

def iniciar_program():
    """Funçao que inicia o loop principal do programa de vendas"""
    banco_dados = dados()
    atendente = banco_dados["atendente"]
    paes_estoque = banco_dados["paes"]
    bairros_disponiveis = banco_dados["bairros"]
    codigo_venda = banco_dados["codigo_venda_base"]

    while True:
        print(" -- Bem vindo(a) a Padaria Desespero, sou o(a) atendente {atendente}. -- ")
        print(" --  Menu Principal --")
        print(" 1 -  Iniciar Vendas\n 2 - cadastrar Nova Localidade\n 3 - Cadastrar Nova localidade \n 4 - Sair do Sistema")

        opcao = input("Escolha a sua opçao:")

        if opcao == "1":
            pedido = processar_pedidos(paes_estoque)
            if not pedido:
                continue
            pao_escolhido, qtd_pedido, valor_compra, paes_estoque = pedido
            print(f"Seu pedido foi de {qtd_pedido} {pao_escolhido['nome']} ficou em R${valor_compra:.2f}.")
            forma_retirada = input("Digite 1 - retirar \n 2 - entregar")
            valor_frete = 0.0

            if forma_retirada == "2":
                bairro,valor_frete = calcular_frete(bairros_disponiveis)
                print(f"Valor do frete para o bairro {bairros_disponiveis[bairro]['nome']} e de R$ {valor_frete:.2f}.")
            
            elif forma_retirada != "1":
                print("Opçao invalida!")
                continue

            dados_cliente = obter_dados_cliente()
            forma_pagamento = solicitar_forma_pagamento()

            valor_total_compra = valor_frete + valor_compra
            codigo_venda = gerar_codigo_venda(codigo_venda)
            banco_dados["codigo_venda_base"] = codigo_venda

            print("-- Resumo da venda -- ")
            print(f"Cliente: {dados_cliente['nome']}")
            print(f"Valor dos pães: R${valor_compra:.2f}")
            print(f"Valor do frete: R${valor_frete:.2f}")
            print(f"Valor total da compra   R${valor_total_compra}")
            print(f"Codigo da entrega: {codigo_venda}")

        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            print("Saindo do sistema.Ate a proxima.")
            break
        else:
            print("Opçao invalida.")
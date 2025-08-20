'''
Cormecio padaria 
1- O programa tem que rodar em loop infinito ate ser parado
2- Cliente pedir um tipo de pao (frances, doce, australiano, forma)
3-Cada pao tera uma quantidade
4-valor do pao 
5- Pedir forma de pagmento (cartao, dinheiro, pix)
6- forma de entrega
7- dados do cliente (se for entrega)
8-valor do frete por bairro
9- nome do atendente
10- codigo da entrega
'''
#nome do pao 
nome_frances = "Frances"
nome_Doce = "Doce"
nome_forma = "Forma"
#valor do pao 
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99
#quantidade
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18
#Nome da atendente
nome_atendente = "Maria"
#nome do bairro
bairro_barroco = "barroco"
bairro_jose = "sao Jose"
#valores do frete
frete_barroco = 5.00
frete_jose = 10.00
#codigo de venda
codigo_venda = 98568

while True:
    print(f"-- Bem vindo a padaria,Desespero,sou a atendente {nome_atendente} --")
    escolha = int(input(f"Temos os paes:{nome_frances, nome_Doce, nome_forma}"))
    if escolha == nome_frances:
        quantidade = int(input(f"Qual a quantidade de paes {nome_frances} que deseja?"))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compras = quantidade * valor_frances
            print(f"Seu pedido ficou em {valor_compras}.")
        else:
            print(f"Infelizmente so tenho {quantidade_frances} paes {nome_frances} disponiveis.")
            break
    forma_retirada = input("E para 1:retirar ou 2:entregar? ").lower()
    if forma_retirada == "2":
        bairro_entrega = input(f"Qual o bairro de entrega? (1:{bairro_barroco}, 2:{bairro_jose}) ")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R${valor_frete}.")
        elif bairro_entrega == "2":
            valor_frete = frete_jose
            print(f"Valor do frete R${valor_frete}.")
        else:
            print("Fora da area de entrega.")
        break

    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Por favor, informe seu nome:  ")
    forma_pagamento = input("Qual a forma de pagamento? (1:cartao, 2:dinheiro) ")
    if forma_pagamento == "1":
        forma_pagamento = "dinheiro"
    else:
        forma_pagamento = "Cartao"
    codigo_atual = codigo_venda + 1

    print(f"O valor total da sua compra foi de R${valor_compras + valor_frete} com codigo{codigo_venda} .")
    break
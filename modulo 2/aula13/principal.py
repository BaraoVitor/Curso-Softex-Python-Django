from banco_dados import dados
from calcular_frete import calcular_frete
from dados_cliente import obter_dados_cliente
from forma_pagamento import solicitar_forma_pagamento
from gerar_codigo import gerar_codigo_venda
from gerenciar_localidade import cadastrar_localidade
from gerenciar_produto import cadastrar_produto , atualizar_produto
from processamento_principal import processar_pedidos


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

i = iniciar_program()

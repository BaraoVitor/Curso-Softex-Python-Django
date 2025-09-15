
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
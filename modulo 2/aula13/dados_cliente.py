def obter_dados_cliente() -> dict:
    """Solicita e retorna os dados do cliente"""
    nome = input("Informe seu nome:")
    return {"nome": nome}
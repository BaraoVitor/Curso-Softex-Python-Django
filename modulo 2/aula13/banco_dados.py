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

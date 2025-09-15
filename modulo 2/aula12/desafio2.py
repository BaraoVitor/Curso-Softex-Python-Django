class Calc:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def contas(self):
        while True:
            print("\nDigite o número 5 no operador para sair")
            
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            if not num1.isdigit() or not num2.isdigit():
                print("Digite apenas números inteiros!")
                continue

            num1 = int(num1)
            num2 = int(num2)

            operador = input("Digite o operador lógico:\n 1 - ( + )\n 2 - ( - )\n 3 - ( x )\n 4 - ( / )\n 5 - Sair\nR: ")

            if operador == "1":
                print("Resultado:", num1 + num2)
            elif operador == "2":
                print("Resultado:", num1 - num2)
            elif operador == "3":
                print("Resultado:", num1 * num2)
            elif operador == "4":
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida!")
                else:
                    if num1 % num2 == 0:
                        resultado = num1 // num2
                    else:
                        resultado = num1 / num2
                    print("Resultado:", resultado)
            elif operador == "5":
                print("Tchau")
                break
            else:
                print("Operador inválido! Escolha de 1 a 5.")
c = Calc()
c.contas()

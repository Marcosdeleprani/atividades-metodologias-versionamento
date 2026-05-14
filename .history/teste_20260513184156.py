print("=== CALCULADORA EM PYTHON ===")

escolha = int(input("1- soma\n2- subtração\n3- multiplicação\n4- divisão"))
numero1 = float(input("digite o primeiro valor: "))
numero2 = float(input("digite o segundo valor: "))
match escolha:

    case 1:
        adicao()
    case 2:
        subtracao()
    case 3:
        multiplicacao()
    case 4:
        divisao()
    case _:
        print("erro na operação")
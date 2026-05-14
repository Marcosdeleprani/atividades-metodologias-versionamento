print("=== CALCULADORA EM PYTHON ===")

escolha = int(input("1- soma\n2- subtração\n3- multiplicação\n4- divisão"))

match escolha:

    case 1:
        adicao()
    case 2:
        subtracao()
    case 3:
        multiplicacao()
    case 4:
        divisao()
    case _
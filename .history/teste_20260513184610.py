print("=== CALCULADORA EM PYTHON ===")

escolha = int(input("1- soma\n2- subtração\n3- multiplicação\n4- divisão"))
numero1 = float(input("digite o primeiro valor: "))
numero2 = float(input("digite o segundo valor: "))

match escolha:

    case 1:
        valorF = adicao(numero1,numero2)
    case 2:
        valorF = subtracao(numero1,numero2)
    case 3:
        valorF = multiplicacao(numero1,numero2)
    case 4:
        valorF = divisao(numero1,numero2)
    case _:
        print("operação invalida")

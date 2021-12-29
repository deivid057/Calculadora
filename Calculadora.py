from init import *

while True:

    Menu(['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Sair do Script!'])

    Opc = int(input("Sua Opção: "))

    if Opc <= 4:
        x = float(input("Digite um Número: "))
        y = float(input("Digite outro Número: "))
        print('\n')
    if Opc == 1:
        cabeçalho("Soma")
        print("{} + {} = {}".format(x, y, (x + y)))
        print("\n")
    elif Opc == 2:
        cabeçalho("Subtração")
        print("{} - {} = {}".format(x, y, (x - y)))
        print("\n")
    elif Opc == 3:
        cabeçalho("Multiplicação")
        print("{} x {} = {}".format(x, y, (x * y)))
        print("\n")
    elif Opc == 4:
        cabeçalho("Divisão")
        print("{} : {} = {}".format(x, y, (x / y)))
        print("\n")
    else:
        cabeçalho( "Saindo do Script......")
        break

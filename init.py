def Soma(x,y):
    return x + y

def Subtração(x,y):
    return x - y

def Multiplicação(x,y):
    return x * y

def Divisão(x,y):
    return x / y

def linha(tam = 40):
    return "-" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def Menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())

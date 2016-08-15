import numpy as np

def f1():   #Funcao que fornece os valores de y0 a yf de uma funcao de terceiro grau
    inicial = int(input('Digite o valor x0:'))
    final = int(input('Digite o valor xf: '))
    intervalo = int(input('Digite o valor dos intervalos: '))
    x = list(range(inicial, final, intervalo))
    i = inicial
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    d = float(input('Digite o valor de d: '))
    text_file = open('fGrauTres.txt', 'w')
    for i in range(len(x)):
        x[i] = a * (x[i] ** 3) + b * (x[i] ** 2) + c * x[i] + d
        text_file.write(str(x[i]) + '\n')
        print(x[i])
        i += 1
    text_file.close()

def f2():
    inicial = float(input('Digite o valor x0: '))
    n = float(input('Digite o numero de termos: '))
    intervalo = float(input('Digite o valor dos intervalos: '))
    x = list()
    i = 0
    text_file = open("floatRange.txt", "w")
    while (i <= n):
        x.append(inicial + intervalo * i)
        print(x)
        text_file.write(str(x[i]) + '\n')
        i += 1
        print()
    text_file.close()

f2()
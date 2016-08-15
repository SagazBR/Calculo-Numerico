import numpy as np


strt = int(input('Digite um numero inicial: '))
stp = int(input('Digite um numero final: '))
ste = int(input('Digite um delta: '))
inf = list(range(strt, stp, ste))
print('As chaves para esta conjectura sao: ' + str(inf))


def collatz():
    i = 0
    cntr = 0
    values = list()
    while cntr < len(inf):
        n = inf[cntr]
        print('A chave para esta conjectura e ' + str(n))
        print()
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            values.append(n)
            print(values[i])
            i += 1
        print('Fim da conjectura.')
        print()
        cntr += 1

collatz()

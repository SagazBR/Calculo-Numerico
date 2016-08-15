import numpy as np
import factorial as fct


def sinX():
    x = float(input('Choose a x for (x * pi)/ d radians:'))
    d = float(input('Choose a d for (x * pi)/ d radians:'))
    termI = 1
    termEx = 0
    y = (x / d) * np.pi
    senOfX = 0
    while termEx < 50:
        senOfX += ((y ** termI) / (fct.factorial(termI))) * (-1) ** (termEx)
        termI += 2
        termEx += 1
    print(str(senOfX))
    return senOfX


def cosX():
    x = float(input('Choose a x for (x * pi)/ d radians:'))
    d = float(input('Choose a d for (x * pi)/ d radians:'))
    termI = 0
    termEx = 0
    y = (x / d) * np.pi
    cosOfX = 0
    while termEx < 50:
        cosOfX += ((y ** termI) / (fct.factorial(termI))) * (-1) ** (termEx)
        termI += 2
        termEx += 1
    print(str(cosOfX))

import math as math
import numpy as np
from sympy import *


def f(x): return math.cos(math.cos(math.cos(math.cos(x**2))))

a = 0
b = 2
aproxValue = 1.447977898105671 # Valor obtido com erro inferior a 1.5e-15

def Simpson():
    print('Valor absoluto usado é %.14f:' % aproxValue)
    print()
    for j in range (0,2):
        if j == 0: # Para 7 casas decimais
            n = 80 # Valor obtido no programa auxiliar
            error = 1.5e-7
        else: # Para 12 casas decimais
            n = 1418 # Valor obtido no programa auxiliar
            error = 1.5e-12
        
        deltaX = (b-a)/n
        multiplier = float(deltaX/3)
        points = np.linspace(a, b, n+1)
        i = 0
        total = 0.0
        for x in points:
            if i % 2 == 0:
                if x != a and x != b:
                    total += 2*f(x)
                else:
                    total += f(x)
            else:
                total += 4*f(x)
            i += 1

        total = total*multiplier
        print('Regra de Simpson com n =', n, ', erro =', error, 'e |I-If| = {:.3e}'.format(abs(aproxValue-total)))
        if j == 0:
            print('Resultado: %.7f' % total,'± {:.3e}'.format(abs(aproxValue-total)))
        else:
            print('Resultado: %.12f' % total,'± {:.3e}'.format(abs(aproxValue-total)))
        print() 


def Rectangule():
    print('Regra dos Rectângulos:')
    for n in range(1, 21):
        result = 0.0
        exp = 2**(n)
        deltaX = (b-a)/exp
        points = np.linspace(a, b, exp)
        points = points[:-1]
        for x in points:
            result += f(x)
        result = result*deltaX
        print('Valor de K:', n, 'Resultado: %.15f' %
              result, 'Erro:', abs(aproxValue-result))


def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps = 2 * eps
    return eps


Simpson()
#   Rectangule()
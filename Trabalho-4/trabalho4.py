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
    n = 2516 # Calculado no programa auxiliar
    deltaX = (b-a)/n
    multiplier = float(deltaX/3)
    points = np.linspace(a, b, n+1)
    i = 0
    total = 0.0
    error = 1.5e-13
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
    print('Regra de Simpson com n =', n, ', erro =', error, 'e |I-If| = %.20f' % abs(aproxValue-total))
    print('Resultado: %.17f ± 1.5e-13' % total)
    print()
    print('7 casas decimais: %.7f' % total)
    print('12 casas decimais: %.12f' % total)
    print()
    print('Regra dos Rectângulos:')


def Rectangule():
    for n in range(1, 21):
        deltaX = (b-a)/n
        result = 0.0
        points = np.linspace(a, b, n+1)
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
Rectangule()

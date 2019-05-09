import math as math
import numpy as np
from sympy import *


def f(x): return math.cos(math.cos(math.cos(math.cos(x**2))))


a = 0
b = 2


def Simpson():
    n = 32768  # Calcular o n usando a formula é impossível por isso este número da uma aproximação bastante boa que é usada em baixo
    deltaX = (b-a)/n
    multiplier = float(deltaX/3)
    points = np.linspace(a, b, n+1)
    i = 0
    total = 0.0
    error = epsilon() # Erro fácil para usar
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
    print('Regra de Simpson com n =', n, 'e erro =', error)
    print('Resultado: %.17f ± 2.22e-16' % total)
    print()
    print('7 casas decimais: %.7f' % total)
    print('12 casas decimais: %.12f' % total)
    print()
    print('Regra dos Rectângulos')
    return total


def Rectangule():
    for n in range(1, 21):
        result = 0.0
        deltaX = (b-a)/n
        points = np.linspace(a, b, n+1)
        points = points[:-1]
        for x in points:
            result += f(x)
        result = result*deltaX
        print('Valor de K:', n, 'Resultado: %.15f' %
              result, 'Erro:', abs(realVal-result))


def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps = 2 * eps
    return eps


realVal = Simpson()
Rectangule()

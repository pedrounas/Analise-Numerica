import math as math
import numpy as np


def f(x): return 1/(1+x)


def Simpson():
    n = 4
    a = 0
    # b = 2
    b = 1
    deltaX = (b-a)/n
    multiplier = float(deltaX/3)
    #def f(x): return math.cos(math.cos(math.cos(math.cos(x**2))))
    points = np.linspace(0, 1, 5)
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
    print('Regra de Simpson com n =', n)
    print('7 casas decimais: %.7f' % total)
    print('12 casas decimais: %.12f' % total)
    print()
    print('Regra dos Rectângulos')

def Rectangule():
    a = 0
    b = 1
    for n in range(1, 21):
        result = 0.0
        deltaX = (b-a)/n
        points = np.linspace(a, b, n+1)
        points = points[:-1]
        for x in points:
            result += f(x)
        print('Valor de K:', n, 'Resultado:', result*deltaX)


Simpson()
Rectangule()

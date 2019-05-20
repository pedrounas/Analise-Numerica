import math as math
import numpy as np
from sympy import *


def f(x): return math.cos(math.cos(math.cos(math.cos(x**2))))

a = 0
b = 2
aproxValue = 1.447977898105671
n = 1

for j in range(0,2):
    while(1):
        deltaX = (b-a)/n
        multiplier = float(deltaX/3)
        points = np.linspace(a, b, n+1)
        i = 0
        total = 0.0
        if j == 0:
            error = 1.5e-7
        else:
            error = 1.5e-12
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
        if (abs(aproxValue - total) < error):
            print('Valor de é', n)
            print()
            break
        n+=1
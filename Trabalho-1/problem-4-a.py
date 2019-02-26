from __future__ import division
import numpy as np
import math

count = 0

def adder( n ):
    sum = 0
    for i in range(0, n + 1):
        sum += math.factorial(i)**2/math.factorial(2*i + 1)
    return sum * (9/(2*math.sqrt(3)))

for i in range (-15, -7):
    
    count = 0
    cenas = abs((math.pi - adder(count)))
    while (cenas >= 10**i):
        count = count + 1
        cenas = abs((math.pi - adder(count)))
    
    print 'Valor do erro:' , 10**i,  'Valor da serie:', count, '------->', '%.15f' % adder(count)
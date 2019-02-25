from __future__ import division
import numpy as np
import math

count = 0

def adder( n ):
    sum = 0
    for i in range(0, n + 1):
        sum += math.factorial(i)**2/math.factorial(2*i + 1)
    return sum * (9/(2*math.sqrt(3)))

while (count < 10):
    print '%.15f' % np.sum(np.absolute(adder(count)) - adder(count))
    count = count + 1


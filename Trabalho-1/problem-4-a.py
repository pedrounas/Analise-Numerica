import numpy as np
import math

for i in range (-15, -7):
    count = 0
    sum = 0
    while ( 1 ):
        x = abs(math.factorial(count)**2/math.factorial(2*count + 1))
        sum+= x
        y = sum * (9/(2*math.sqrt(3)))
        if (abs(math.pi - y) >= 10**i):
            count = count + 1
        else:
            break
    
    z = abs(math.pi - y)
    print ('Valor do erro:' , 10**i,  '| Valor da serie:', count, '| En (Arrendondar a n+1 casas * 10^n): ', '%.16f' % z)
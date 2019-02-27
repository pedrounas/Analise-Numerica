import numpy as np
import math

for i in range (-8, -7):
    count = 0
    sum = 0
    while ( 1 ):
        x = abs(((-1)**count)/(2*count+1))
        print(x)
        sum+= x
        y = sum * 4
        print(y)
        if (abs(math.pi - y) >= 10**i):
            count = count + 1
        else:
            break

    print ('Valor do erro:' , 10**i,  '| Valor da serie:', count, '| Sn (Arrendondar a n+1 casas * 10^n): ', '%.16f' % y)
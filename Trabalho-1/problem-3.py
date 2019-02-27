import numpy as np
import math

for i in range (-15, -7):
    count = 0
    sum = 0
    while ( 1 ):
        x = abs(((-1)**count)/(2*count+1))
        if (x >= 10**i):
            sum+= x
            count = count + 1

        else:
            break
    
    y = sum * 4

    print ('Valor do erro:' , 10**i,  'Valor da serie:', count, '------->', '%.16f' % y)
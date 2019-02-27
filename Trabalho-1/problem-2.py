import numpy as np
import math

for i in range (-15, -7):
    count = 0
    sum = 0
    while ( 1 ):
        x = abs(math.factorial(count)**2/math.factorial(2*count + 1))
        if (x >= 10**i):
            sum+= x
            count = count + 1
        
        else:
            break
    
    y = sum * (9/(2*math.sqrt(3)))

    print ('Valor do erro:' , 10**i,  '| Valor da serie:', count, '| Sn (Arrendondar a n+1 casas * 10^n): ', '%.16f' % y)
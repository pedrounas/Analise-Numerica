import math as math

def main():
    f = lambda x: x**2 - (math.cos(x))**2
    df = lambda x: 2*x + math.sin(2*x)
    eps = epsilon()
    firstZero = NewtonMethod(f,df,-1,1,eps)
    getInterval(firstZero,10**-1)

def NewtonMethod(f,df,a,b,eps):
    it = 0
    x = a
    while True:
        xn = x - f(x)/df(x)
        it+= 1
        error = abs(xn-x)
        if (error <= eps):
            break
        x = xn
    print("X Value -> %0.20f" % x, "| Iterations ->", it, "| A value ->", a, "| B value ->", b)
    return x

def getInterval(zero,amp):
    leftBound = zero - amp
    rightBound = zero + amp
    print("[%0.20f" % leftBound,"; %0.20f]" % rightBound)

def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps  = 2 * eps
    return eps

main()
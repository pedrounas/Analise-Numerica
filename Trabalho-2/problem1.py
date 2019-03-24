import math as math

def main():

    # Definimos a função, a sua derivada e o erro que é epsilon. 
    
    f = lambda x: x**2 - (math.cos(x))**2
    df = lambda x: 2*x + math.sin(2*x)
    eps = epsilon()

    # PROBLEMA 1 #

    # 1a) - Procurar o primeiro 0 na função usando o método de Newton (Valor concordante com o gráfico da função)
    # Imprime o valor, o número de iterações e o intervalo.

    firstZero = NewtonMethod(f,df,-1,1,eps)

    # 1b) - Intervalo para o primeiro 0 da função anterior com amplitude de 10^-1 ou seja 0.05 para cada lado.
    
    getInterval(firstZero,10**-1)

    # 1c) - Não faço a mínima
    
    # 1d) - Aproximar o primeiro 0 com erro inferior a 5*10^-12, nada de especial.

    getAproximation(firstZero,5*10**-12)

    # 1e) - Sendo que usamos eps como erro no 1a) e como é menor que o erro dado aqui, o número de iterações será igual.

    # PROBLEMA 2 # 

    # 2a) - x^2 - cos(x)^2 = 0 => -x^2 = -cos(x)^2 => x^2 = cos(x)^2 => x = cos(x)). Ou seja g(x) = cos(x) e usamos isso com o método iterativo.

    f2 = lambda x: math.cos(x)
    SimpleIterativeMethod(f2,-1,eps,100)

    # 2b) - No fucking idea.

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
    print("\nProblema 1a)")
    print("X -> %0.20f" % x, "|| Iterations ->", it, "|| A value ->", a, "|| B value ->", b)
    print("\n")
    return x

def getInterval(zero,amp):
    leftBound = zero - amp
    rightBound = zero + amp
    print("\nProblema 1b)")
    print("Interval -> [%0.20f" % leftBound,"; %0.20f]" % rightBound)
    print("\n")

def getAproximation(zero,err):
    print("\nProblema 1d)")
    print("Aproximation -> %0.12f" %zero, "±", err)
    print("\n")

def SimpleIterativeMethod(f,x0,eps,nMax):
    x1 = f(x0)
    err = abs(x1 - x0)
    i = 1
    while (err > eps and i <= nMax):
        x0 = x1
        x1 = f(x0)
        err = abs(x1 - x0)
        i=i+1
    if i > nMax:
        print("Não foi possível ao fim de %d iterações encontrar a solução." % i)
        return
    else:
        print("\nProblema 2a)")
        print("Solução encontrada: %0.20f" % x1)
        print("Erro: %0.20f" % err, "Iterations:", i)
        print("\n")
        return x1

def epsilon():
    eps = 1
    while (eps + 1 > 1):
        eps = eps / 2
    eps  = 2 * eps
    return eps

main()
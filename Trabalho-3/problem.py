import math as math

def main():
    startLagrange()

def startLagrange():
    xValue = []
    yValue = []
    print('Insira o valor de n: ', end='')
    n = int(input())
    print('Insira o valor de x: ', end='')
    x0 = typeCheck(input())
    print('Insira o valor da abcissa e ordenada para os n+1 pontos: ')
    for i in range(0,n+1):
        x, y = input().split() # Separa as inputs para a var x e var y
        xValue.append(typeCheck(x)) # Mete no fim do array
        yValue.append(typeCheck(y))
    Lagrange(n,x0,xValue,yValue)
    printLagrange(n,x0,xValue,yValue)

def Lagrange(n,x0,xVal,yVal):
    res = 0
    for t in range(0,n+1): # Vai de x0 a xn
        num = 1
        den = 1
        for i in range(0,n+1):
            if t != i: # Ignora xt
                num *= (x0-xVal[i])
                den *= (xVal[t]-xVal[i])
        res += (num/den) * yVal[t]
    print('Valor de pn(x): ', res)

def printLagrange(n,x0,xVal,yVal): # Imprime o polinomio para confirmar valores
    print('pn(x) = ',end='')
    for t in range(0,n):
        print('(',end='')
        for i in range(0,n+1):
            if t != i:
                print('(', x0,'-',xVal[i],')',end='')
        print('/',end='')
        for i in range(0,n+1):
            if t != i:
                print('(',xVal[t], '-',xVal[i],')',end='')
        print(')',end='')
        print(' *', yVal[t], ' + ', end='')
    t = n
    print('(',end='')
    for i in range(0,n+1):
        if t != i:
            print('(', x0,'-',xVal[i],')',end='')
    print('/',end='')
    for i in range(0,n+1):
        if t != i:
            print('(',xVal[t], '-',xVal[i],')',end='')
    print(')',end='')
    print()

def typeCheck(x): # Converte a input em int ou float dependendo do tipo
    try:
        return int(x)
    except ValueError:
        return float(x)

main()
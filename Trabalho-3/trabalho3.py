import math as math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


def main():
    # showFunction()
    startLagrange()
    # cubicSpline()


def showFunction():
    points = np.linspace(0, 10, 100)
    def fx(x): return (( x - 1 ) * ( x - 2 ) * ( x - 2.5 ) * ( x - 3 ) * ( x - 4 )/( 0 - 1 ) * ( 0 - 2 ) * ( 0 - 2.5 ) * ( 0 - 3 ) * ( 0 - 4 ))
    plt.plot(points, fx(points))
    plt.show()

def findClosest(x0,xVal,yVal):
    test = xVal
    a = min(test, key=lambda x:abs(x-x0))
    del test[test.index(a)]
    b = min(test, key=lambda x:abs(x0-x))
    del test[test.index(b)]
    c = min(test, key=lambda x:abs(x0-x))
    print(a,b,c)

def startLagrange():
    xValue = []
    yValue = []
    print('Insira o valor de n: ', end='')
    n = int(input())
    print('Insira o valor de x: ', end='')
    x0 = typeCheck(input())
    print('Insira o valor da abcissa e ordenada para os n+1 pontos: ')
    with open("input.txt", "r") as inp:
        for line in inp:
            x, y = line.split()  # Separa as inputs para a var x e var y
            xValue.append(typeCheck(x))  # Mete no fim do array
            yValue.append(typeCheck(y))
    # print()
    # test = xValue
    # test_ = yValue
    # a = min(test, key=lambda x:abs(x-x0))
    # aIndex = test.index(a)
    # del test[aIndex]
    # del test_[aIndex]
    # b = min(test, key=lambda x:abs(x0-x))
    # bIndex = test.index(b)
    # del test[bIndex]
    # del test_[bIndex]
    # c = min(test, key=lambda x:abs(x0-x))
    # cIndex = test.index(c)
    # del test[cIndex]
    # del test_[cIndex]
    print()
    printLagrange(n, x0, xValue, yValue)
    Lagrange(n,x0,xValue,yValue)
    printNewton(n, x0, xValue, yValue)
    Newton(n,x0,xValue,yValue)
    # findClosest(x0,xValue,yValue)


def Lagrange(n, x0, xVal, yVal):
    res = 0.0
    for t in range(0, n+1):  # Vai de x0 a xn
        num = 1.0
        den = 1.0
        for i in range(0, n+1):
            if t != i:  # Ignora xt
                num *= (x0-xVal[i])
                den *= (xVal[t]-xVal[i])
        # print(num/den * yVal[t])
        res += (num/den) * yVal[t]
        # print(res)
    print('Valor de pn(x) segundo Método de Lagrange: ', res)
    print()


def Newton(n, x0, xVal, yVal):
    res = yVal[0]
    for t in range(0, n):
        split = 1
        for i in range(0, t+1):
            split *= (x0-xVal[i])
        res += split*splitDif(t+1, xVal, yVal, 0, 1)
    print('Valor de pn(x) segundo Método de Newton:', res)


def splitDif(n, xVal, yVal, a, b):
    dif = 1
    # print(n)
    if n == 1:
        # print(a,b)
        return (yVal[b]-yVal[a])/(xVal[b]-xVal[a])
    else:
        return (splitDif(n-1, xVal, yVal, 1, n)-splitDif(n-1, xVal, yVal, 0, n-1))/(xVal[n]-xVal[0])


def typeCheck(x):  # Converte a input em int ou float dependendo do tipo
    try:
        return int(x)
    except ValueError:
        try: 
            return float(x)
        except ValueError:
            return x



def printLagrange(n, x0, xVal, yVal):  # Imprime o polinomio para confirmar valores
    print('Método de Lagrange = ', end='')
    for t in range(0, n):
        print('(', end='')
        for i in range(0, n+1):
            if t != i:
                print('(', x0, '-', xVal[i], ')', end='')
            if i != n and i != 0:
                print(' * ', end='')
        print('/', end='')
        for i in range(0, n+1):
            if t != i:
                print('(', xVal[t], '-', xVal[i], ')', end='')
            if i != n and i != 0:
                print(' * ', end='')
        print(')', end='')
        print(' *', yVal[t], ' + ', end='')
    t = n
    print('(', end='')
    for i in range(0, n+1):
        if t != i:
            print('(', x0, '-', xVal[i], ')', end='')
    print('/', end='')
    for i in range(0, n+1):
        if t != i:
            print('(', xVal[t], '-', xVal[i], ')', end='')
    print(')', end='')
    print()
    print()


def printNewton(n, x0, xVal, yVal):
    print('Método de Newton =', yVal[0], '+ ', end='')
    for t in range(0, n):
        for i in range(0, t+1):
            print('(', x0, '-', xVal[i], ') * ', end='')
        print('F[', end='')
        for j in range(0, t+2):
            print(xVal[j], end='')
            if j != t+1:
                print(', ', end='')
        print('] ', end='')
        if t != n-1:
            print('+ ', end='')
    print()

# returns a function


def cubicSpline():
    xPoints=[]
    yPoints=[]
    x=typeCheck(input("Insira a abcissa pretendida: "))
    n=int(input("Insira o valor de n: "))
    print("Insira as n abcissas: ")
    for i in range(1, n+2):
        xPoints.append(input())
    print("Insira as n ordenadas: ")
    for i in range(1, n+2):
        yPoints.append(input())

    coefTuples=interpolate.splrep(xPoints, yPoints)
    print(coefTuples)
    spline=interpolate.splev(x, coefTuples)
    print(spline)
    return


main()

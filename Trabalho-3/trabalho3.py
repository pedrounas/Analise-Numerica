import math as math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


def main():
	#exercicio1a

	#exercicio1b (Precisa do input dos pontos, comentar para testar)
    #cubicSpline(False, None, None)
	
	#exercicio 2a
	cubicSpline(True, None, None)
	
	#exercicio 2b I
	f = lambda x: 4*np.power(x,2) + np.sin(9*x)
	points = createPoints(f)
	#exercicio 2b II
	cubicSpline(True,points,f)

def createPoints(f):
	xPoints = np.linspace(-1,1,9)
	yPoints = []
	for i in xPoints:
		yPoints.append(round(f(i),3))
	points = zip(xPoints,yPoints)
	return points

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

def cubicSpline(default, Outpoints, originalFunction):
	points = []

	if (default == False): #Insere pontos à mão
		graph = plt.figure('Exercicio 1b')
		n = int(input("Insira o número de pontos a inserir:"))
		for i in range(1,n+1):
			xn = float(input("Insira a abcissa " + str(i) + ":"))
			yn = float(input("Insira a ordenada " + str(i) + ":"))
			points.append( (xn, yn) )
	elif (default == True and Outpoints == None): #Usa os pontos default
		points = [ (0, 1.4) , (1, 0.6) , (2, 1.0) , (2.5, 0.6) , (3, 0.6), (4, 1.0) ]
		graph = plt.figure('Exercicio 2a (Spline Cúbico)')
	else: #Usa a função do 2b
		points = Outpoints
		graph = plt.figure('Exercicio 2b II (Spline Cúbico)')
	x, y = zip(*points)
	subplot = graph.add_subplot(111)
	plt.scatter(x, y, color='black')
	for xy in zip(x, y):
		subplot.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')
	temp1,temp2 = interpolate.splprep([x, y], s=0)
	spaceP = np.arange(0, 1.01, 0.01)
	spline = interpolate.splev(spaceP, temp1)
	plt.plot(x, y, 'orange', spline[0], spline[1], 'blue')
	if (Outpoints == None):
		plt.legend(['Pontos', 'Spline Cubico'])
	else:
		originalP = np.arange(-1.0,1.01,0.01)
		plt.plot(originalP, originalFunction(originalP), 'red')
		plt.legend(['Pontos', 'Spline Cubico', 'Função Original'])
	plt.show()

main()

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
from matplotlib import pyplot as plt

#Definindo a função

def f(x):
    return x**3 -x -1

x = np.linspace(0 , 10 ,100)
y = f(x)

#Definindo o plotamento
def p(A, B):
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.grid(True)
    plt.title("Zero de funções")
    [xmin, xmax, ymin, ymax] = plt.axis()
    plt.plot([A, A], [ymin, ymax], '-.')
    plt.plot([B, B], [ymin, ymax], '-.')

#Definindo o intervalo e achando um novo

A = 1
B = 10

#Definir condição de parada

x_tol = 0.0001
y_tol = 0.0001
x_anterior = B
while True:
    p(A, B)

    [xmin, xmax, ymin, ymax] = plt.axis()
    xi1 = A + (B-A)/3
    xi2 = B - (A-B)/3
    plt.plot([xi1, xi1], [ymin, ymax], 'k--')
    print ("Aproximação em Y : %.6lf" % f(xi2))
    print("X : %.6lf" % xi2)
    if f(xi1) < f(xi2) :
        B = xi2
    else:
        A = xi1
    #Checar condição de parada


        #No eixo X
    if abs(xi1 - xi2) < x_tol:
        break


    plt.show()

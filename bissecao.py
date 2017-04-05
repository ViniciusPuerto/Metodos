import numpy as np
from matplotlib import pyplot as plt

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

A = 1
B = 2
#Definindo o intervalo e achando um novo

#Definir condição de parada

x_tol = 0.0001
y_tol = 0.0001
x_anterior = B
while True:
    p(A, B)

    [xmin, xmax, ymin, ymax] = plt.axis()
    xi = (A + B)/2
    plt.plot([xi, xi], [ymin, ymax], 'k--')
    print ("Aproximação em Y : %.6lf" % f(xi))
    print("X : %.6lf" % xi)
    if f(A)*f(xi) < 0:
        B = xi
    elif f(A)*f(xi) == 0:
        print("Raiz encontrada: %.6lf" % xi)
    else:
        A = xi
    #Checar condição de parada
        #no eixo y
    if abs(f(xi))< y_tol:
        break
        #No eixo X
    if abs(x_anterior - xi) < x_tol:
        break
    x_anterior = xi

    plt.show()
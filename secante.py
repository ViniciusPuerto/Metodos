import numpy as np
from matplotlib import pyplot as plt

def f(x):

    return (np.pi*x**2*(3-x))/3 - 0.5

x = np.linspace(0 , 10 ,100)
y = f(x)

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
B = 10
x0 = 0.25
x01 = 0.5
#x_tol = 0.0001
y_tol = 0.002

while True:
    p(A, B)
    [xmin, xmax, ymin, ymax] = plt.axis()
    xi = (x0*f(x01) - f(x0)*x01)/(f(x01)-f(x0))
    plt.plot([xi, xi], [ymin, ymax], 'k--')
    print("Aproximação em Y : %.6lf" % f(xi))
    print("X : %.6lf" % xi)
    if abs(f(xi)) < y_tol:
        break
        # No eixo X
    #if abs(x0 - xi) < x_tol:
   #     break
    x0 = x01
    x01 = xi
    plt.show()
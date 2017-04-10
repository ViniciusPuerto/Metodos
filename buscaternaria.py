import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x * np.e ** -x + 0.2

def f_linha(x):
    return np.e ** -x * (x - 1)

def hessiana(x):
    return np.e ** -x * (2 - x)

x = np.linspace(0, 3, 100)
y = f(x)

def plot_function(interval_min, interval_max, point_inside_interval):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y = f(x)')
    plt.title('Zeros de funções')
    plt.grid()

    [xmin, xmax, ymin, ymax] = plt.axis()
    plt.plot([point_inside_interval, point_inside_interval], [ymin, ymax], 'k--')

    if interval_min != interval_max:
        plt.plot([interval_min, interval_min], [ymin, ymax], 'k-')
        plt.plot([interval_max, interval_max], [ymin, ymax], 'k-')

    plt.show()

plot_function(0, 3, 0)

# Métodos da Busca Ternária e Pela Razão Áurea
# --------------------------------------------

# Definir o intervalo inicial
A = 1
B = 3

# Definir condições de parada
x_tol = 0.0001
x_anterior = B

# Definir variável auxiliar para contagem de iterações
counter = 1

# Definir constante áurea
phi = (1 + 5 ** .5) / 2

while True:
    # Encontrar a próxima aproximação do ponto crítico da função
    xi1 = A + (B - A) / 3 # Método da Busca Ternária
    xi2 = B - (B - A) / 3 # Método da Busca Ternária
#     xi1 = B - (B - A) / phi # Método da Busca Pela Razão Áurea
#     xi2 = A + (B - A) / phi # Método da Busca Pela Razão Áurea
    xi = min(xi1, xi2)

    # Visualizar o gráfico
    # plot_function(A, B, xi)
    print('%2d: f(%+.6f) = %+.6f' % (counter, xi, f(xi)))
    counter += 1

    # Definir o novo intervalo
    if f(xi1) < f(xi2):
        B = xi2
    else:
        A = xi1

    # Checar as condições de parada
    # Eixo X
    if abs(x_anterior - xi) < x_tol:
        break
    x_anterior = xi


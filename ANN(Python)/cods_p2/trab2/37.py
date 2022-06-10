import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')



x = [0.089, 0.127, 0.694, 0.95, 1.109, 1.701, 2.079, 2.22, 2.38, 2.464, 2.973, 2.992, 3.004, 3.441, 3.725, 4.432, 4.481, 4.541, 4.55, 4.557, 4.713, 4.749, 4.983]
y = [1.512, 1.642, 2.991, 2.892, 2.713, 2.089, 2.006, 2.048, 2.144, 2.214, 2.812, 2.833, 2.846, 2.875, 2.165, 1.64, 1.873, 2.173, 2.218, 2.252, 2.881, 2.956, 2.503]


intervalo = [-1.263, 1.102]
subintervalos = [1, 22, 47, 50, 92, 138, 209, 263, 564, 972, 1845, 5145]

'''
n = len(subintervalos)
for i in range(n):
    trapz(f, intervalo[0], intervalo[1], subintervalos[i])
'''

trapzPonto(x, y)
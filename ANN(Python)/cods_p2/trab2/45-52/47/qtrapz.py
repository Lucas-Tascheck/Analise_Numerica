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
    return (9 + 4*(math.cos(0.49*x)**2))*(5*math.exp(-0.52*x) + 2*math.exp(0.18*x))

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')



x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
y = [0, 1.11, 2.66, 3.24, 4.48, 5.3, 5.79, 6.8, 7.75, 8.8, 9.77, 10.47, 11.47]

a = 2.74
b = 7.69
n = 19

#trapz(f, a, b, n)
trapzPonto(x, y)
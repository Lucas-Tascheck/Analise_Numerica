import math


def quadratura(f, x, c):
    return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g


if __name__ == '__main__':


    #exemplo 1
    x = ()
    c = ()

    def f_1(x):
        return 1 + 2 * x ** 4 -3 * x**5 + 8 * x**7

    aprox_1 = quadratura(f_1, x, c)

    #exemplo 2
    def f_2(x):
        return math.exp(-x*x)

    nós = ()
    pesos = ()

    for i in range(2, 6):
        aprox_2 = quadratura(f_2, x=nós[i], c=pesos[i])
        print(f'{aprox_2 = }')

    #exemplo 3
    def f_3(x):
        return x**2 * math.sin(x)
    
    for i in range(2, 6):
        aprox_3 = quadratura(f_3, x=nós[i], c=pesos[i])
        print(f'{aprox_3 = }')

    #exemplo 4

    def f_4(x):
        return math.exp(-x*x)

    a, b = 0, 1
    g = change(f_4, a, b)
    for i in range(2, 6):
        aprox_4 = quadratura(g, x=nós[i], c=pesos[i])
        print(f'{aprox_4 = }')
        
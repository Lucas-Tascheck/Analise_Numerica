import math
import numpy as np


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h/2


def coeff_a(f, n: int, num_intervalos=256):
    def func(x):
        return f(x) * np.cos(x * n)
    return trapz(func, -np.pi, np.pi, num_intervalos) / np.pi

def coeff_b(f, n: int, num_intervalos=256):
    def func(x):
        return f(x) * np.sin(x * n)
    return trapz(func, -np.pi, np.pi, num_intervalos) / np.pi

def fourier(c, a, b):
    def func(x):
        soma = c
        for n, coeffs in enumerate(zip(a, b), 1):
            ai, bi = coeffs
            soma += (ai * np.cos(n * x) + bi * np.sin(n * x))
        return soma
    return func

if __name__ == '__main__':

    def f(x):
        if x < 0:
            return 3 + x / np.pi
        return 1 + x / np.pi

    num_intervalos = 256
    num_coeffs = 10   # num termos na serie = 2 * num_coeffs + 1

    c = trapz(f, -np.pi, np.pi, num_intervalos) / (2 * np.pi)
    a = [coeff_a(f, ni, num_intervalos) for ni in range(1, num_coeffs)]
    b = [coeff_b(f, ni, num_intervalos) for ni in range(1, num_coeffs)]

    serie = fourier(c, a, b)


    import matplotlib.pyplot as plt

    t = np.linspace(-np.pi, np.pi, 200)
    ft = [f(ti) for ti in t]

    st = [serie(ti) for ti in t]

    plt.plot(t, ft)
    plt.plot(t, st)
    plt.savefig("fourier.png")

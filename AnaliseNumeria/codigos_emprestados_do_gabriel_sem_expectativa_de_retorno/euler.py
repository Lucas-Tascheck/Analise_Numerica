

def euler(f, x0: float, y0: float, h: float, n: float):
    for k in range(n):
        y = y0 + h * f(x0 + k * h, y0)
        print(f'x_{k+1} = {x0 + (k + 1) * h}\ny_{k+1} = {y}\n')
        y0 = y

x0 = 0.71419
y0 = 0.95514
def f(x, y):
    return y * (1- x) + x + 2

r = euler(f, x0, y0, h=0.10144, n=10)
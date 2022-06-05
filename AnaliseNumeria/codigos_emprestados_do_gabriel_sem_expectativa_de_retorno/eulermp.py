

def eulermp(f, x0, y0, h, n):
    for k in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + h * m1 / 2)
        y1 = y0 + h * m2
        x0 += h
        y0 = y1
        yield x0, y0

def f(x, y):
    return y * (2 - x) + x + 1

x0 = 1.92684
y0 = 2.12005
h = 0.13841
n = 10

resp = eulermp(f, x0, y0, h, n)

for i, value in enumerate(resp, 1):
    xi, yi = value
    print(f'x_{i} = {xi}\ny_{i} = {yi}\n')
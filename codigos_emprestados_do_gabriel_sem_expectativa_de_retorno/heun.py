

def heun(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h * (m1 + m2) / 2

        x0 += h
        y0 = y1
        r.append((x0, y0))
    return r


def f(x, y):
    return y * (2 - x) + x + 1

x0 = 1.16898
y0 = 1.40346

r = heun(f, x0, y0, 0.17768, 10)
for x,y in r:
    print(f'{x} - {y}')
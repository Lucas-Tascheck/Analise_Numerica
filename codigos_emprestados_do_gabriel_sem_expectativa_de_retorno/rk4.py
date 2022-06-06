

def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        m3 = f(x0 + h / 2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        y1 = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6

        x0 += h
        y0 = y1
        r.append((x0, y0))
    return r


def f(x, y):
    return y * (1-x) + x + 2

x0 = 0.60302
y0 = 2.24668

r = rk4(f, x0, y0, 0.19376, 10)
for x,y in r:
    print(f'phi({x}) ~ {y}')
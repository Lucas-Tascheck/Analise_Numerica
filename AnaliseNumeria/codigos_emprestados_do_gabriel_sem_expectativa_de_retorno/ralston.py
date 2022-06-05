

def ralston(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (3/4) * h, y0 + (3/4) * h * m1)
        y1 = y0 + h * (m1 + 2 * m2) / 3

        x0 += h
        y0 = y1
        r.append((x0, y0))
    return r


def f(x, y):
    return y * (2 - x) + x + 1

x0 = 0.85731
y0 = 0.43052

r = ralston(f, x0, y0, 0.16556, 10)
for x,y in r:
    print(f'{x} - {y}')
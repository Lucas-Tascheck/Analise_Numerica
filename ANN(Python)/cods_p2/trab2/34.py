import math

def richardson(col_1):
    n = len(col_1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]


if __name__ == '__main__':

    #exemplo 1

    def func(x):
        return math.sin(x)**4 - 4*math.sin(x)**2 + math.cos(x**2) + math.exp(-x**2) + 5

    x0 = 0.51484
    approximations = [-3.633534842939852, -3.8711681494900745, -3.9763994801442664, -4.025614839055493, -4.049377001103494, -4.061047574352187]

    approx = richardson(approximations)
    print(f'Aproximação = {approx}')
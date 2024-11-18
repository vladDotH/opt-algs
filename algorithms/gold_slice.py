import sympy

lambdaParam = ((-1 + sympy.sqrt(5)) / 2).evalf()


# Функция алгоритма оптимизации для метода золтого сечения
def gold_slice(
        f: sympy.Lambda, epsilon: float,
        a: float = -1, b: float = 1, maxIter=1_000_000_000
) -> (float, list[float]):
    X = [(a + b) / 2]
    d = b - a
    i = 0
    while abs(d) > 2 * epsilon and i < maxIter:
        i += 1
        ld = lambdaParam * abs(d)
        x1 = b - ld
        x2 = a + ld
        fx1 = f(x1).evalf()
        fx2 = f(x2).evalf()

        if fx1 < fx2:
            b = x2
        else:
            a = x1
        d = b - a
        X.append((a + b) / 2)

    return (a + b) / 2, X

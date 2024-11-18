import sympy


# Функция алгоритма оптимизации для метода Ньютона-Рафсона
def newton_rafson(
        f1: sympy.Lambda, f2: sympy.Lambda,
        delta: float, x0: float = 0, maxIter=1_000_000_000
) -> (float, list[float]):
    x = x0
    X = [x0]
    fx1 = f1(x).evalf()
    fx2 = f2(x).evalf()
    i = 0
    while abs(fx1) > delta and i < maxIter:
        i += 1
        x = x - fx1 / fx2
        X.append(x)
        fx1 = f1(x).evalf()
        fx2 = f2(x).evalf()

    return x, X

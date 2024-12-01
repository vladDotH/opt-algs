import sympy


# Функция алгоритма оптимизации для метода хорд
def chords(
        f1: sympy.Lambda, epsilon: float, delta: float,
        a: float = -1, b: float = 1, maxIter=10_000
) -> (float, list[float]):
    f1a = f1(a).evalf()
    f1b = f1(b).evalf()
    if not (f1a < 0 < f1b):
        raise Exception('Некорректный интервал')

    X = []

    i = 0
    while True:
        i += 1
        f1a = f1(a).evalf()
        f1b = f1(b).evalf()
        x = a - f1a * (b - a) / (f1b - f1a)
        X.append(x)

        f1x = f1(x).evalf()
        if f1x > delta:
            b = x
        elif f1x < -delta:
            a = x
        else:
            return x, X

        if abs(b - a) <= 2 * epsilon or i > maxIter:
            return (a + b) / 2, X

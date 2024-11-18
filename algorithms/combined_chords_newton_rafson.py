import sympy


def combined_chords_newton_rafson(
        f1: sympy.Lambda, f2: sympy.Lambda,
        epsilon: float, delta: float, a: float, b: float, maxIter=1_000
) -> (float, list[float]):
    f1a = f1(a).evalf()
    f1b = f1(b).evalf()
    if not (f1a < 0 < f1b):
        raise Exception('incorrect interval')

    X = []
    i = 0
    while True:
        i += 1

        f1a = f1(a).evalf()
        f1b = f1(b).evalf()

        # Выбор метода: касательных или хорд
        if f1a * f2(a).evalf() > 0:
            # Метод касательных для a
            a_new = a - f1a / f2(a).evalf()
        else:
            # Метод хорд для a
            a_new = a - f1a * (b - a) / (f1b - f1a)

        if f1b * f2(b).evalf() > 0:
            # Метод касательных для b
            b_new = b - f1b / f2(b).evalf()
        else:
            # Метод хорд для b
            b_new = b - f1b * (b - a) / (f1b - f1a)

        # Обновляем интервал
        if abs(f1(a_new).evalf()) < delta:
            a = a_new
        else:
            b = b_new

        # Добавляем приближение в список
        x = (a + b) / 2
        X.append(x)

        # Проверяем условия выхода
        if abs(f1(x).evalf()) < delta or abs(b - a) < 2 * epsilon or i > maxIter:
            return x, X

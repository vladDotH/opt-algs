import sympy

from algorithms import gold_slice, Method
from algorithms import combined_chords_newton_rafson


def parallel_gold_slice_and_combined_chords_newton_rafson(
        f: sympy.Lambda, f1: sympy.Lambda, f2: sympy.Lambda,
        epsilon: float, delta: float, a: float, b: float, maxIter=10_000
) -> (float, list[float], Method):
    xmin1, steps1 = gold_slice(f, delta, a, b, maxIter)
    xmin2, steps2 = combined_chords_newton_rafson(f1, f2, epsilon, delta, a, b, maxIter)
    # Выбор наилучшего результата
    if f(xmin1) < f(xmin2):
        return xmin1, steps1, Method.GOLD_SLICE
    else:
        return xmin2, steps2, Method.CHORDS_AND_NEWTON_RAFSON

import numpy as np
import sympy
from PyQt6.QtWidgets import *

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure


class Plot(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("График")

        self.canvas = FigureCanvas(Figure())
        self.plt = self.canvas.figure.subplots()
        navbar = NavigationToolbar(self.canvas, self)

        lt = QVBoxLayout(self)
        lt.addWidget(self.canvas)
        lt.addWidget(navbar)

        self.setLayout(lt)
        self.line = None

    def clear(self) -> None:
        self.canvas.figure.clf()
        self.plt = self.canvas.figure.subplots()
        self.canvas.draw()

    def set_data(self, f: sympy.Lambda, x0: float, X: list[float]) -> None:
        self.clear()

        padding = 2.5
        minPoints = 100
        maxPoints = 150
        xmin = float(min(x0, *X) - padding)
        xmax = float(max(x0, *X) + padding)
        span = (xmax - xmin) / 2 + padding
        points = min(max(len(X), minPoints), maxPoints) * 10

        plotX = np.linspace(xmin - span, xmax + span, points)
        plotY = [f(x).evalf() for x in plotX]

        self.plt.plot(plotX, plotY, color='royalblue')

        y0 = f(x0).evalf()
        Y = [f(x).evalf() for x in X]

        ymin = float(min(y0, *Y))
        ymax = float(max(y0, *Y))

        # Отсеиваем часть точек для ускорения графика
        maxScatterPoints = 50
        k = max(len(Y) // maxScatterPoints, 1)

        for x, y in zip(X[::k], Y[::k]):
            self.plt.scatter(x, y, color='pink')
        self.plt.scatter(x0, y0, color='crimson')

        xMargin = abs(xmax - xmin) / 10
        yMargin = abs(ymax - ymin) / 10

        span = 2.5
        self.plt.set_ylim(ymin - yMargin - span, ymax + yMargin + span)
        self.plt.set_xlim(xmin - xMargin - span, xmax + xMargin + span)
        self.canvas.draw()

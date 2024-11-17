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

        xmin = min(X)
        xmax = max(X)
        span = (xmax - xmin) / 2
        points = len(X) * 10
        plotX = np.linspace(xmin - span, xmax + span, points)
        plotY = [f(x).evalf() for x in plotX]

        self.plt.plot(plotX, plotY, color='royalblue', linestyle='--')

        y0 = f(x0).evalf()
        Y = [f(x).evalf() for x in X]

        for x, y in zip(X, Y):
            self.plt.scatter(x, y, color='pink')
        self.plt.scatter(x0, y0, color='crimson')

        self.canvas.draw()

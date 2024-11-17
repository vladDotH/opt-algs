import sympy.parsing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from algorithms import Method, gold_slice, chords, newton_rafson
from gui.Control import Control
from gui.Plot import Plot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Алгоритмы оптимизации")
        self.info = self.menuBar().addAction('О программе', self.onInfo)

        self.control = Control(self)
        self.plot = Plot(self)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Orientation.Horizontal)
        splitter.addWidget(self.control)
        splitter.addWidget(self.plot)
        self.setCentralWidget(splitter)

        self.control.solve.pressed.connect(self.onSolve)

    def onInfo(self) -> None:
        msg = '''Делайте что хотите'''
        QMessageBox(
            QMessageBox.Icon(QMessageBox.Icon.Information),
            'Справка',
            msg
        ).exec()

    def onSolve(self):
        try:
            x = sympy.Symbol('x')

            method = self.control.algorithmsGroup.checkedId()
            func = self.control.expression.text()
            expr = sympy.parsing.parse_expr(func)
            f = sympy.Lambda(x, expr)
            f1 = sympy.Lambda(x, expr.diff(x))
            f2 = sympy.Lambda(x, expr.diff(x, x))

            x0 = 0
            X = []

            match method:
                case Method.GOLD_SLICE.value:
                    eps = float(self.control.eps.text())
                    a = float(self.control.a.text())
                    b = float(self.control.b.text())
                    x0, X = gold_slice(f, eps, a, b)
                case Method.CHORDS.value:
                    eps = float(self.control.eps.text())
                    delta = float(self.control.delta.text())
                    a = float(self.control.a.text())
                    b = float(self.control.b.text())
                    x0, X = chords(f1, eps, delta, a, b)
                case Method.NEWTON_RAFSON.value:
                    delta = float(self.control.delta.text())
                    a = float(self.control.a.text())
                    x0, X = newton_rafson(f1, f2, delta, a)
                case _:
                    raise Exception('Не выбран метод')

            self.plot.set_data(f, x0, X)

        except Exception as exception:
            msg = exception.__str__()
            QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Warning),
                'Ошибка',
                msg
            ).exec()

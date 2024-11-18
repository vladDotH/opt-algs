import sympy.parsing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from algorithms import Method, gold_slice, chords, newton_rafson, combined_chords_newton_rafson, \
    parallel_gold_slice_and_combined_chords_newton_rafson
from gui.Control import Control
from gui.LoggerWidget import LoggerWidget
from gui.Plot import Plot
from util import Logger, LogLevel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Алгоритмы оптимизации")
        self.info = self.menuBar().addAction('О программе', self.onInfo)

        self.control = Control(self)
        self.plot = Plot(self)
        self.logger = LoggerWidget(self)
        Logger.connect(self.logger.print)

        controlSplitter = QSplitter(self)
        controlSplitter.setOrientation(Qt.Orientation.Vertical)
        controlSplitter.addWidget(self.control)
        controlSplitter.addWidget(self.logger)

        splitter = QSplitter(self)
        splitter.setOrientation(Qt.Orientation.Horizontal)
        splitter.addWidget(controlSplitter)
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
        Logger.log('Запуск решения', LogLevel.Info)
        try:
            x = sympy.Symbol('x')

            method = self.control.algorithmsGroup.checkedId()
            func = self.control.expression.text()
            expr = sympy.parsing.parse_expr(func)
            expr1 = expr.diff(x)
            expr2 = expr.diff(x, x)
            f = sympy.Lambda(x, expr)
            f1 = sympy.Lambda(x, expr1)
            f2 = sympy.Lambda(x, expr2)

            Logger.log(f'Метод: {Method(method).translate()}', LogLevel.Info)
            Logger.log(f'Функция: {str(expr)}', LogLevel.Info)
            Logger.log(f'Первая производная: {str(expr1)}', LogLevel.Info)
            Logger.log(f'Вторая производная: {str(expr2)}', LogLevel.Info)

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
                case Method.CHORDS_AND_NEWTON_RAFSON.value:
                    eps = float(self.control.eps.text())
                    delta = float(self.control.delta.text())
                    a = float(self.control.a.text())
                    b = float(self.control.b.text())
                    x0, X = combined_chords_newton_rafson(f1, f2, eps, delta, a, b)
                case Method.PARALLEL_GOLD_SLICE_AND_CHORDS_AND_NEWTON_RAFSON.value:
                    eps = float(self.control.eps.text())
                    delta = float(self.control.delta.text())
                    a = float(self.control.a.text())
                    b = float(self.control.b.text())
                    x0, X = parallel_gold_slice_and_combined_chords_newton_rafson(f1, f2, eps, delta, a, b)
                case _:
                    raise Exception('Не выбран метод')

            Logger.log(f'Получено решение: {x0}', LogLevel.Info)
            self.plot.set_data(f, x0, X)

        except Exception as exception:
            msg = exception.__str__()
            QMessageBox(
                QMessageBox.Icon(QMessageBox.Icon.Warning),
                'Ошибка',
                msg
            ).exec()

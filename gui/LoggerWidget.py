from PyQt6.QtWidgets import *

from util import LogLevel


# Виджет вывода логов
class LoggerWidget(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Журнал")

        self.levels = [False] * 3
        box = QGroupBox("Уровни событий")
        boxlt = QVBoxLayout(box)
        self.debug = QCheckBox("Отладочные")
        self.info = QCheckBox("Информационные")
        self.warn = QCheckBox("Ошибки")

        self.debug.toggled.connect(lambda s: self.levelToggled(0, s))
        self.info.toggled.connect(lambda s: self.levelToggled(1, s))
        self.warn.toggled.connect(lambda s: self.levelToggled(2, s))

        for i, w in zip(list(range(3)), [self.debug, self.info, self.warn]):
            boxlt.addWidget(w)
        boxlt.addStretch()

        self.info.toggle()
        self.warn.toggle()
        box.setLayout(boxlt)

        lt = QHBoxLayout(self)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        lt.addWidget(box)
        lt.addWidget(self.text)
        self.setLayout(lt)

    def levelToggled(self, n: int, state: bool) -> None:
        self.levels[n] = state

    # Вывод лога в виджет (можно использовать в качестве слота для логгера из util.Logger)
    def print(self, s: str, lvl: LogLevel) -> None:
        if self.levels[lvl.value]:
            self.text.append(f'[{lvl.name}]: {s}')

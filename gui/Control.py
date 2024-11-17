from PyQt6.QtCore import Qt, QLocale
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import *
from algorithms import Method


class Control(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Управление")
        self.controlLayout = QVBoxLayout(self)

        expressionTitle = QLabel("Функция f(x) = ", self)
        self.expression = QLineEdit(self)

        algGroupBox = QGroupBox('Метод', self)
        algLt = QGridLayout(algGroupBox)
        self.algorithmsGroup = QButtonGroup(algGroupBox)
        gold_slice = QRadioButton('Золотого сечения', self)
        chords = QRadioButton('Хорд', self)
        newton_rafson = QRadioButton('Ньютона-Рафсона', self)

        cols = 3
        for i, b in enumerate([gold_slice, chords, newton_rafson]):
            self.algorithmsGroup.addButton(b, i)
            algLt.addWidget(b, i // cols, i % cols)

        algGroupBox.setLayout(algLt)

        for w in [expressionTitle, self.expression, algGroupBox]:
            self.controlLayout.addWidget(w)

        self.solve = QPushButton('Запуск', self)

        self.settingsLayout = QVBoxLayout(self)
        self.settingsWidget: QWidget = None

        self.controlLayout.addLayout(self.settingsLayout)
        self.controlLayout.addWidget(self.solve)
        self.controlLayout.addStretch()
        self.setLayout(self.controlLayout)

        self.algorithmsGroup.idPressed.connect(self.method_selected)

        self.validator = QDoubleValidator(self)
        self.validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.validator.setLocale(QLocale("en_US"))

    def method_selected(self, btnId: int):
        if self.settingsWidget is not None:
            self.settingsLayout.removeItem(self.settingsLayout.itemAt(0))
            self.settingsWidget.deleteLater()

        match btnId:
            case Method.GOLD_SLICE.value:
                self.gold_slice()
            case Method.CHORDS.value:
                self.chords()
            case Method.NEWTON_RAFSON.value:
                self.newton_rafson()

    def gold_slice(self):
        widget = QWidget(self)
        lt = QVBoxLayout(widget)

        epsTitle = QLabel('Эпсилон', widget)
        self.eps = QLineEdit('0.1', self)
        self.eps.setValidator(self.validator)

        aTitle = QLabel('Точка a', widget)
        self.a = QLineEdit('-10', self)
        self.a.setValidator(self.validator)

        bTitle = QLabel('Точка b', widget)
        self.b = QLineEdit('10', self)
        self.b.setValidator(self.validator)

        for w in [epsTitle, self.eps, aTitle, self.a, bTitle, self.b]:
            lt.addWidget(w)

        lt.addStretch()
        widget.setLayout(lt)
        self.settingsLayout.addWidget(widget)
        self.settingsWidget = widget

    def chords(self):
        widget = QWidget(self)
        lt = QVBoxLayout(widget)

        epsTitle = QLabel('Эпсилон', widget)
        self.eps = QLineEdit('0.1', self)
        self.eps.setValidator(self.validator)

        deltaTitle = QLabel('Дельта', widget)
        self.delta = QLineEdit('0.1', self)
        self.delta.setValidator(self.validator)

        aTitle = QLabel('Точка a', widget)
        self.a = QLineEdit('-10', self)
        self.a.setValidator(self.validator)

        bTitle = QLabel('Точка b', widget)
        self.b = QLineEdit('10', self)
        self.b.setValidator(self.validator)

        for w in [epsTitle, self.eps, deltaTitle, self.delta, aTitle, self.a, bTitle, self.b]:
            lt.addWidget(w)

        lt.addStretch()
        widget.setLayout(lt)
        self.settingsLayout.addWidget(widget)
        self.settingsWidget = widget

    def newton_rafson(self):
        widget = QWidget(self)
        lt = QVBoxLayout(widget)

        deltaTitle = QLabel('Дельта', widget)
        self.delta = QLineEdit('0.1', self)
        self.delta.setValidator(self.validator)

        aTitle = QLabel('Точка x0', widget)
        self.a = QLineEdit('10', self)
        self.a.setValidator(self.validator)

        for w in [deltaTitle, self.delta, aTitle, self.a]:
            lt.addWidget(w)

        lt.addStretch()
        widget.setLayout(lt)
        self.settingsLayout.addWidget(widget)
        self.settingsWidget = widget

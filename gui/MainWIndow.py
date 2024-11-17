from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Алгоритмы оптимизации")
        self.setCentralWidget(QLabel("Welcome", self))
        self.info = self.menuBar().addAction('О программе', self.onInfo)

    def onInfo(self) -> None:
        msg = '''Делайте что хотите'''
        QMessageBox(
            QMessageBox.Icon(QMessageBox.Icon.Information),
            'Справка',
            msg
        ).exec()

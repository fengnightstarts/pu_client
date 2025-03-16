from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QAction
from utill.bean import *
from .ui.log_view import Ui_MainWindow
from datetime import datetime


class log_window(QMainWindow):
    add_log_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__set_context_menu()
        self.__bind()
        self.num = 0

    def __bind(self):
        self.add_log_signal.connect(self.__add_log)
        self.ui.pushButton.clicked.connect(
            lambda: self.__set_max_log(self.ui.spinBox.value())
        )
        self.clear_action.triggered.connect(self.__clear)
        self.copy_action.triggered.connect(self.__copy)

    def __set_context_menu(self):
        self.ui.plainTextEdit.setContextMenuPolicy(
            Qt.ContextMenuPolicy.ActionsContextMenu
        )
        self.clear_action = QAction("清空", self)
        self.copy_action = QAction("复制", self)
        self.ui.plainTextEdit.addAction(self.clear_action)
        self.ui.plainTextEdit.addAction(self.copy_action)

    def __clear(self):
        self.num = 0
        self.ui.plainTextEdit.clear()

    def __copy(self):
        self.ui.plainTextEdit.copy()

    @Slot(str)
    def __add_log(self, log: str):
        self.num += 1
        self.ui.plainTextEdit.appendPlainText(log)

    def add_log(self, log: str):
        self.add_log_signal.emit(log)

    def __set_max_log(self, max_log: int):
        self.ui.spinBox.setValue(max_log)

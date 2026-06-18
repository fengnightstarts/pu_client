import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QCompleter, QVBoxLayout, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.comboBox = QComboBox()
        self.comboBox.setEditable(True)
        # 添加示例数据
        items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
        self.comboBox.addItems(items)
        # 创建QCompleter
        self.completer = QCompleter(self.comboBox.model())
        self.completer.setFilterMode(Qt.MatchContains)
        self.comboBox.setCompleter(self.completer)
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        self.setLayout(layout)
        self.setWindowTitle("QComboBox with QCompleter")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec())

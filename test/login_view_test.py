import sys
import os

import view.login_view as login_view
import utill.http_client as http_client

from PySide6.QtWidgets import QApplication


def main():
    app = QApplication()
    window = login_view.login_window()
    window.set_school_list(http_client.get_school_list())
    window.show()
    app.exec()

from queue import Queue
import app.main
from view import *
import PySide6.QtWidgets
import threading
from logger import log_to_window


def main():
    q = Queue()
    ap = PySide6.QtWidgets.QApplication()
    login_window = login_view.login_window()
    main_window = main_view.main_window()
    log_window = log_view.log_window()
    log_to_window.init(log_window)
    log_window.show()
    t = threading.Thread(
        target=app.main.start,
        args=(q, login_window, main_window),
        name="app_main",
    )
    t.setDaemon(True)
    t.start()
    ap.exec_()

import PySide6.QtWidgets
from queue import Queue
import threading
from view import login_view, main_view, log_view
from log import log_to_window
import app.main


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


if __name__ == "__main__":
    main()

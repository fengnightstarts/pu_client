import PySide6.QtWidgets
from queue import Queue
import threading
import view
import log
import app.main
import view.log_view


def main():
    q = Queue()
    ap = PySide6.QtWidgets.QApplication()
    login_window = view.login_view.login_window()
    main_window = view.main_view.main_window()
    log_window = view.log_view.log_window()
    log.log_to_window.init(log_window)
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

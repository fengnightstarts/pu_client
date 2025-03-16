from view.log_view import log_window
from datetime import datetime

window: log_window = None


def init(log_view):
    global window
    window = log_view


def add_log(msg):
    window.add_log(datetime.now().strftime("%H:%M:%S") + " " + msg)

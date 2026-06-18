from view import main_view
from utill import http_client
from PySide6.QtWidgets import QApplication
from .get_act_list_test import token, sid


def main():
    app = QApplication([])
    act_list = http_client.get_activity_list(token=token, sid=sid)
    act_list = [
        http_client.get_activity_info(token=token, sid=sid, act_id=act_id)
        for act_id in act_list
    ]
    main_window: main_view.main_window = main_view.main_window(act_list)
    main_window.set_all_acts(act_list)
    main_window.show()
    app.exec()

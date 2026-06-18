from view import main_view
from utill import http_client
from utill.filter import *
from .get_info_test import token, sid
from PySide6.QtWidgets import QApplication
import json


def main():
    def get_filt_methods_test(list):
        print(list)

    def get_category_test(list):
        print(list)

    app = QApplication()
    normal = all_true()
    hasjoin = filter_by_has_join().decorate(normal)
    notfull = filter_by_capacity().decorate(hasjoin)
    join_time = filter_by_join_time().decorate(notfull)
    act_list = http_client.get_activity_list(token, sid)
    act_list = [
        http_client.get_activity_info(token=token, sid=sid, act_id=id)
        for id in act_list
    ]
    view = main_view.main_window()
    view.set_all_acts(act_list)

    view.show()
    app.exec()

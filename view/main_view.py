from .ui.act_widget import Ui_act_Widget
from .ui.main_view import Ui_MainWindow
from utill import filter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt, Slot, Signal
from utill.bean import Activity, Message, commands
from PySide6.QtWidgets import QSizePolicy
import requests
from enum import Enum
import app.main
from utill import bean
from PySide6.QtWidgets import QMessageBox


class widget_type(Enum):
    all = 0
    filted = 1
    target = 2


img_cache = {}


def get_img_data(url: str):
    if not img_cache.get(url, None):
        img_cache[url] = requests.get(url).content

    return img_cache[url]


class act_widget(QWidget):
    def __init__(self, act: Activity, type: widget_type, main_window):
        super().__init__()
        self.ui: Ui_act_Widget = Ui_act_Widget()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.act = act
        self.type = type

        # 设置活动图片
        pixmap = QPixmap()
        pixmap.loadFromData(get_img_data(act.logo))
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.img_Label.setPixmap(pixmap)
        # self.ui.img_Label.setFixedSize(100, 100)
        self.ui.img_Label.setAlignment(Qt.AlignCenter)
        self.ui.img_Label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # 设置活动信息
        info_text = (
            f"{act.name}\n"
            f"{act.status_name} "
            f"{act.category_name} "
            f"学分: {act.credit}\n"
            f"报名开始时间: {act.join_start_time}\n"
            f"报名结束时间: {act.join_end_time}\n"
            f"活动开始时间: {act.start_time}\n"
            f"活动结束时间: {act.end_time}\n"
            f"地址: {act.address} "
            f"是否已报名: {'是' if act.has_join else '否'}\n"
            f"允许学院: {act.allow_college or 'all'} \n"
            f"允许年级: {act.allow_year or 'all'} "
            f"报名需审核: {'否' if act.join_type else '是'}\n"
        )
        self.ui.teinfo_TextEdit.setText(info_text)
        self.ui.teinfo_TextEdit.setReadOnly(True)
        self.__set_contextMenu()

    def __set_contextMenu(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        if self.type == widget_type.target:
            self.del_action = QAction("删除", self)
            self.del_action.triggered.connect(self.__del_act)
            self.addAction(self.del_action)
        else:
            self.add_action = QAction("报名", self)
            self.add_action.triggered.connect(self.__add_act)
            self.addAction(self.add_action)

        self.flush_action = QAction("刷新", self)
        self.flush_action.triggered.connect(self.__flush_act)
        self.addAction(self.flush_action)
        self.join_to_server_action = QAction("加入服务器", self)
        self.join_to_server_action.triggered.connect(self.__join_to_server)
        self.addAction(self.join_to_server_action)

    def __del_act(self):
        print("del act")
        self.main_window.del_act_from_target_list(self.act.id)

    def __add_act(self):
        print("add act")
        app.main.push_msg(Message(commands.join_activity, act=self.act))
        self.main_window.set_act(self.act, widget_type.target)

    def __flush_act(self):
        print("flush act")
        app.main.push_msg(Message(commands.get_activity_info, act_id=self.act.id))

    def __join_to_server(self):
        app.main.push_msg(Message(commands.join_to_server, act=self.act))


class main_window(QMainWindow):
    show_window_signal = Signal()
    close_window_signal = Signal()
    set_status_bar_signal = Signal(str)
    set_act_signal = Signal(Activity, widget_type)
    del_target_act_widget_signal = Signal(int)
    hide_window_signal = Signal()
    open_message_window_signal = Signal(str, str)

    def __init__(self, act_list: list[Activity] = None):
        super().__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.act_dict: dict = {}
        self.all_act_widget_dict: dict = {}
        self.filted_act_widget_dict: dict = {}
        self.target_act_widget_dict: dict = {}
        self.filt_context: filter.filt_context = None
        self.__bind()
        self.__flush_filter_context()

    def load_config(self, config: bean.Config):
        self.ui.grade_LineEdit.setText(config.grade)
        self.ui.college_LineEdit.setText(config.college)
        self.ui.server_url.setText(config.server_url)
        for cate in config.categories:
            self.ui.callegory_comboBox.addItem(cate)
        for method in config.filt_method:
            if method == bean.filt_method.default_filt:
                self.ui.default_filter_CheckBox.setChecked(True)
            if method == bean.filt_method.filt_by_capacity:
                self.ui.default_filter_CheckBox.setChecked(True)
            elif method == bean.filt_method.filt_by_join_type:
                self.ui.filt_by_join_type_checkBox.setChecked(True)
            elif method == bean.filt_method.filt_by_category:
                self.ui.filt_by_category_checkBox.setChecked(True)
        for acti in config.target_act_list:
            app.main.push_msg(Message(commands.get_activity_info, act=acti))
        self.__filt_acts()

    def __bind(self):
        self.ui.callegory_pushButton.clicked.connect(self.__add_category)
        self.show_window_signal.connect(lambda: self.show())
        self.close_window_signal.connect(lambda: self.close())
        self.hide_window_signal.connect(lambda: self.hide())
        self.set_status_bar_signal.connect(
            lambda status: self.ui.statusbar.showMessage(status)
        )
        self.set_act_signal.connect(self.__set_act)
        self.ui.filt_action.triggered.connect(self.__filt_acts)
        self.ui.del_cate_pushButton.clicked.connect(self.__del_category)
        self.ui.flush_action.triggered.connect(
            lambda: app.main.push_msg(Message(commands.get_activity_list))
        )
        self.ui.save_config_action.triggered.connect(
            lambda: app.main.push_msg(Message(commands.save_config))
        )
        self.ui.back_login_action.triggered.connect(
            lambda: app.main.push_msg(Message(commands.back_login))
        )
        self.open_message_window_signal.connect(self.__open_message_window)
        self.ui.link_to_server_action.triggered.connect(
            lambda: app.main.push_msg(
                Message(commands.login_to_server, base_url=self.ui.server_url.text())
            )
        )

    def get_filt_methods(self) -> list[bean.filt_method]:
        filt_methods: list[bean.filt_method] = []
        if self.ui.default_filter_CheckBox.isChecked():
            filt_methods.append(bean.filt_method.default_filt)
        if self.ui.filt_by_join_type_checkBox.isChecked():
            filt_methods.append(bean.filt_method.filt_by_join_type)
        if self.ui.filt_by_category_checkBox.isChecked():
            filt_methods.append(bean.filt_method.filt_by_category)
        if self.ui.filt_by_tribe.isChecked():
            filt_methods.append(bean.filt_method.filt_by_tribe)
        return filt_methods

    @Slot()
    def __add_category(self):
        self.ui.callegory_comboBox.addItem(self.ui.callegory_comboBox.currentText())
        self.ui.callegory_comboBox.setCurrentIndex(-1)
        self.ui.callegory_comboBox.showPopup()

    @Slot()
    def __del_category(self):
        self.ui.callegory_comboBox.removeItem(self.ui.callegory_comboBox.currentIndex())

    @Slot()
    def __filt_acts(self):
        self.__flush_filter_context()
        for act in self.act_dict.values():
            self.__filt_act(act)

    def __flush_filter_context(self):
        methods = self.get_filt_methods()
        for i, item in enumerate(methods):
            if item == bean.filt_method.default_filt:
                methods.pop(i)
                methods.append(bean.filt_method.filt_by_capacity)
                methods.append(bean.filt_method.filt_by_join_end_time)
                methods.append(bean.filt_method.filt_by_college)
                methods.append(bean.filt_method.filt_by_grade)
                break
        self.filt_context = filter.filt_context(
            filt_methods=methods,
            categories=self.get_categories(),
            grade=self.get_grade(),
            college=self.get_college(),
            tribe="null",
        )

    def __filt_act(self, act: Activity):
        if self.filt_context.filt(act):
            if self.filted_act_widget_dict.get(act.id, None):
                return
            self.__set_act_widget(
                self.ui.filter_acts_VBoxLayout,
                act,
                self.filted_act_widget_dict,
                widget_type.filted,
            )
        elif self.filted_act_widget_dict.get(act.id, None):
            self.filted_act_widget_dict[act.id].deleteLater()
            self.filted_act_widget_dict.pop(act.id)

    def get_grade(self) -> str:
        return self.ui.grade_LineEdit.text()

    def get_college(self) -> str:
        return self.ui.college_LineEdit.text()

    def get_categories(self) -> list[str]:
        return [
            self.ui.callegory_comboBox.itemText(i)
            for i in range(self.ui.callegory_comboBox.count())
        ]

    def show_window(self):
        self.show_window_signal.emit()

    def hide_window(self):
        self.hide_window_signal.emit()

    def close_window(self):
        self.close_window_signal.emit()

    def set_status_bar(self, status: str):
        self.set_status_bar_signal.emit(status)

    def get_target_act_list(self) -> list[Activity]:
        result = []
        for _, v in self.target_act_widget_dict.items():
            result.append(v.act)
        return result

    def __set_act_widget(
        self,
        layout: QVBoxLayout,
        act: Activity,
        act_widget_dict: dict,
        type: widget_type,
    ):
        new_widget = act_widget(act, type, self)
        if not act_widget_dict.get(act.id):
            act_widget_dict[act.id] = new_widget
            layout.addWidget(new_widget)
        else:
            layout.replaceWidget(act_widget_dict[act.id], new_widget)
            act_widget_dict[act.id].deleteLater()
            act_widget_dict[act.id] = new_widget

    def set_act(self, act: Activity, type: widget_type = widget_type.all):
        self.set_act_signal.emit(act, type)

    @Slot(Activity, widget_type)
    def __set_act(self, act: Activity, type: widget_type = widget_type.all):
        if type != widget_type.target:
            self.act_dict[act.id] = act
            self.__set_act_widget(
                self.ui.all_acts_VBoxLayout, act, self.all_act_widget_dict, type
            )
            self.__filt_act(act)
        if type == widget_type.target or self.target_act_widget_dict.get(act.id, None):
            self.__set_act_widget(
                self.ui.target_acts_VBoxLayout, act, self.target_act_widget_dict, type
            )

    def del_act_from_target_list(self, act_id):
        self.__del_target_act_widget(act_id)
        print("del act from target list")
        app.main.push_msg(Message(commands.cancel_join, act_id=act_id))

    @Slot()
    def __del_target_act_widget(self, act_id):
        if self.target_act_widget_dict.get(act_id, None):
            self.target_act_widget_dict[act_id].deleteLater()
            self.target_act_widget_dict.pop(act_id)

    def del_target_act_widget(self, act_id):
        self.del_target_act_widget_signal.emit(act_id)

    def __open_message_window(self, title: str, message: str):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def open_message_window(self, title: str, message: str):
        self.open_message_window_signal.emit(title, message)

from .ui.login_view_UI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot
from utill.bean import User, School, login_method, commands, Message
from view.models import SchoolModel
import app.main
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl


class login_window(QMainWindow):
    status_sginal = Signal(str)
    school_list_signal = Signal(list)
    close_window_signal = Signal()
    show_window_signal = Signal()
    hide_window_signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.school_list: list[School] = []
        self.ui.school_ComboBox.setEditable(False)
        self.__bind()
        self.test()

    def load_config(self, user: User):
        self.ui.username_LineEdit.setText(user.username)
        self.ui.password_LineEdit.setText(user.password)
        self.ui.lineEdit.setText(user.get_school_name())

    def test(self):
        self.ui.username_LineEdit.setText("202311070403")
        self.ui.password_LineEdit.setText("Skd@074757")
        self.ui.lineEdit.setText("山东科技大学")

    def __bind(self):
        self.__init_comboBox()
        self.ui.login_PushButton.clicked.connect(self.login)
        self.school_list_signal.connect(self.__set_school_list)
        self.ui.lineEdit.textChanged.connect(
            lambda: self.school_model.filt(self.ui.lineEdit.text())
        )
        self.status_sginal.connect(lambda status: self.ui.statusbar.showMessage(status))
        self.close_window_signal.connect(lambda: self.close())
        self.hide_window_signal.connect(lambda: self.hide())
        self.show_window_signal.connect(lambda: self.show())
        self.ui.flush_school_lists_action.triggered.connect(
            lambda: app.main.push_msg(Message(commands.get_school_list))
        )
        self.ui.project_action.triggered.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://github.com/fengnightstarts/pu_client/")
            )
        )

        if self.ui.auto_loginRadioButton.isChecked():
            return login_method.auto_login
        elif self.ui.use_this_token_RadioButton.isChecked():
            return login_method.use_this_token
        else:
            return login_method.login_on_hand

    def __init_comboBox(self):
        self.ui.school_ComboBox.clear()
        self.school_model = SchoolModel(self.school_list)
        self.ui.school_ComboBox.setModel(self.school_model)

    def set_school_list(self, school_list: list):
        self.school_list_signal.emit(school_list)

    def get_user(self):
        school = self.get_school()
        if school is None:
            raise ValueError("school is not found")
        return User(self.get_username(), self.get_password(), school.id)

    def get_username(self):
        return self.ui.username_LineEdit.text()

    def get_password(self):
        return self.ui.password_LineEdit.text()

    def get_school(self) -> School:
        return self.school_model.getSchool(self.ui.school_ComboBox.currentIndex())

    def set_status_bar(self, status: str):
        self.status_sginal.emit(status)

    @Slot(list)
    def __set_school_list(self, school_list: list[School]):
        for i, item in enumerate(school_list):
            if not isinstance(item, School):
                raise ValueError(
                    f"the {i} of list {item} is not a school object but a {type(item)}"
                )
        self.school_list = school_list
        self.__init_comboBox()
        if self.ui.lineEdit.text() != "":
            self.school_model.filt(self.ui.lineEdit.text())

    @Slot()
    def login(self):
        app.main.push_msg(Message(commands.login, user=self.get_user()))

    def close_window(self):
        self.close_window_signal.emit()

    def hide_window(self):
        self.hide_window_signal.emit()

    def show_window(self):
        self.show_window_signal.emit()

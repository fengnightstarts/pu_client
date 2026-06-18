from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QStyle,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


APP_QSS = """
QWidget {
    font-family: "Microsoft YaHei", "Microsoft YaHei UI", "PingFang SC", "Noto Sans CJK SC", "Segoe UI";
    font-size: 13px;
    color: #111827;
}
QMainWindow, QDialog, QWidget#centralwidget {
    background: #f9fafb;
}
QToolBar {
    background: #ffffff;
    border-bottom: 1px solid #e5e7eb;
    spacing: 6px;
    padding: 6px 18px;
}
QToolBar::separator {
    width: 1px;
    background: #e5e7eb;
    margin: 7px 8px;
}
QToolButton {
    background: transparent;
    border: 0;
    border-radius: 6px;
    padding: 6px;
    color: #374151;
    font-weight: 600;
    min-height: 22px;
    min-width: 22px;
}
QToolButton:hover {
    background: #eff6ff;
    color: #1d4ed8;
}
QToolButton:pressed {
    background: #dbeafe;
}
QLineEdit, QComboBox, QSpinBox {
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 8px 10px;
    min-height: 24px;
    selection-background-color: #3b82f6;
}
QLineEdit:hover, QComboBox:hover, QSpinBox:hover {
    border-color: #9ca3af;
}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border-color: #3b82f6;
}
QLineEdit:disabled, QComboBox:disabled, QSpinBox:disabled {
    background: #f3f4f6;
    color: #9ca3af;
}
QPushButton {
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 8px 13px;
    color: #111827;
    font-weight: 600;
    min-height: 24px;
}
QPushButton:hover {
    border-color: #9ca3af;
    background: #f9fafb;
}
QPushButton:focus {
    border-color: #3b82f6;
}
QPushButton:disabled {
    background: #f3f4f6;
    color: #9ca3af;
}
QPushButton#login_PushButton, QPushButton#PrimaryPillButton {
    background: #2563eb;
    border-color: #2563eb;
    color: #ffffff;
    font-weight: 700;
}
QPushButton#login_PushButton:hover, QPushButton#PrimaryPillButton:hover {
    background: #1d4ed8;
    border-color: #1d4ed8;
}
QPushButton#PillButton {
    background: #ffffff;
    border: 1px solid #d1d5db;
    color: #111827;
}
QGroupBox {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    margin-top: 12px;
    padding: 22px 12px 12px 12px;
    font-weight: 600;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 5px;
    color: #4b5563;
}
QCheckBox, QRadioButton {
    color: #374151;
    spacing: 8px;
    min-height: 24px;
}
QTabWidget::pane {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    background: #ffffff;
    top: -1px;
}
QTabBar::tab {
    background: #f9fafb;
    color: #6b7280;
    border: 1px solid #e5e7eb;
    border-bottom: 0;
    padding: 9px 18px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
QTabBar::tab:selected {
    background: #ffffff;
    color: #111827;
    font-weight: 700;
}
QTabBar::tab:hover {
    color: #2563eb;
}
QScrollArea {
    border: 0;
    background: transparent;
}
QScrollArea > QWidget > QWidget {
    background: transparent;
}
QStatusBar {
    background: #f9fafb;
    border-top: 1px solid #e5e7eb;
    color: #6b7280;
}
QPlainTextEdit, QTextEdit {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 10px;
    selection-background-color: #3b82f6;
}
QTextEdit#ActivityInfo {
    background: transparent;
    border: 0;
    border-radius: 0;
    padding: 0;
    color: #374151;
}
QWidget#HeaderPanel, QWidget#StatsCard, QWidget#LoginPanel, QWidget#ActivityCard {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
}
QWidget#ActivityCard:hover {
    border-color: #bfdbfe;
}
QLabel#HeroTitle {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
}
QLabel#HeroSubtitle, QLabel#MutedText, QLabel#AboutSubtitle, QLabel#AboutBody,
QLabel#AboutFooter {
    color: #6b7280;
}
QLabel#FormLabel {
    color: #374151;
    font-weight: 600;
}
QLabel#StatsNumber {
    font-size: 22px;
    font-weight: 800;
    color: #111827;
}
QLabel#StatsLabel {
    color: #6b7280;
}
QLabel#AboutEyebrow {
    color: #2563eb;
    font-weight: 700;
    letter-spacing: 1px;
}
QLabel#AboutTitle {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
}
QLabel#AboutThanks {
    font-size: 20px;
    font-weight: 800;
    color: #111827;
}
QLabel#AuthorAvatar {
    background: #f3f4f6;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    color: #6b7280;
}
QLabel#AuthorAvatarImage {
    background: transparent;
    border: 0;
}
"""


def apply_app_style(app: QApplication):
    app.setStyle("Fusion")
    app.setFont(QFont("Microsoft YaHei", 10))
    app.setStyleSheet(APP_QSS)


def _polish_toolbar(window: QMainWindow):
    if window.menuBar():
        window.menuBar().hide()
    if hasattr(window.ui, "toolBar"):
        window.ui.toolBar.setMovable(False)
        window.ui.toolBar.setFloatable(False)
        window.ui.toolBar.setIconSize(QSize(18, 18))
        window.ui.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        for action in window.ui.toolBar.actions():
            if not action.toolTip():
                action.setToolTip(action.text())


def _standard_icon(name: str):
    icon = getattr(QStyle, name, None)
    if icon is not None:
        return icon
    return getattr(QStyle.StandardPixmap, name)


def _set_action_icon(window: QMainWindow, action_name: str, icon_name: str):
    action = getattr(window.ui, action_name, None)
    if action:
        action.setIcon(window.style().standardIcon(_standard_icon(icon_name)))


def _spacious_layout(layout, margins=(14, 14, 14, 14), spacing=12):
    layout.setContentsMargins(*margins)
    layout.setSpacing(spacing)


def _make_pill(text: str, primary=False):
    button = QPushButton(text)
    button.setObjectName("PrimaryPillButton" if primary else "PillButton")
    button.setCursor(Qt.PointingHandCursor)
    button.setMinimumHeight(38)
    return button


def _login_row(text: str, field: QWidget):
    row_widget = QWidget()
    row_widget.setMinimumHeight(42)
    row = QHBoxLayout(row_widget)
    row.setContentsMargins(0, 0, 0, 0)
    row.setSpacing(16)
    label = QLabel(text)
    label.setObjectName("FormLabel")
    label.setFixedWidth(80)
    label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
    field.setMinimumHeight(40)
    field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    row.addWidget(label)
    row.addWidget(field, 1)
    return row_widget


def _insert_overview(window: QMainWindow):
    if getattr(window, "_overview_inserted", False):
        return

    header = QWidget()
    header.setObjectName("HeaderPanel")
    header_layout = QHBoxLayout(header)
    header_layout.setContentsMargins(20, 16, 20, 16)
    header_layout.setSpacing(16)

    title_box = QVBoxLayout()
    title_box.setContentsMargins(0, 0, 0, 0)
    title_box.setSpacing(4)
    title = QLabel("PU 活动助手")
    title.setObjectName("HeroTitle")
    subtitle = QLabel("轻松筛选活动、管理报名列表，支持保存配置与服务器同步")
    subtitle.setObjectName("HeroSubtitle")
    title_box.addWidget(title)
    title_box.addWidget(subtitle)
    header_layout.addLayout(title_box, 1)

    side_box = QVBoxLayout()
    side_box.setContentsMargins(0, 0, 0, 0)
    side_box.setSpacing(8)

    actions = QHBoxLayout()
    actions.setSpacing(8)
    actions.addWidget(_make_pill("刷新活动", primary=True))
    actions.addWidget(_make_pill("过滤列表"))
    actions.addWidget(_make_pill("Star on GitHub"))
    side_box.addLayout(actions)

    actions.itemAt(0).widget().clicked.connect(lambda: window.ui.flush_action.trigger())
    actions.itemAt(1).widget().clicked.connect(lambda: window.ui.filt_action.trigger())
    actions.itemAt(2).widget().clicked.connect(window.show_about)

    stats = QHBoxLayout()
    stats.setSpacing(10)
    window._stats_labels = {}
    for key, label, number in (
        ("all", "全部活动", "0"),
        ("filtered", "过滤结果", "0"),
        ("target", "报名列表", "0"),
    ):
        card = QWidget()
        card.setObjectName("StatsCard")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(12, 7, 12, 7)
        card_layout.setSpacing(2)
        label_widget = QLabel(label)
        label_widget.setObjectName("StatsLabel")
        number_widget = QLabel(number)
        number_widget.setObjectName("StatsNumber")
        window._stats_labels[key] = number_widget
        card_layout.addWidget(label_widget)
        card_layout.addWidget(number_widget)
        stats.addWidget(card)

    side_box.addLayout(stats)
    header_layout.addLayout(side_box)
    window.ui.verticalLayout_2.insertWidget(0, header)
    window._overview_inserted = True


def style_login_window(window: QMainWindow):
    window.setWindowTitle("PU 活动助手 - 登录")
    window.resize(720, 560)
    window.setMinimumSize(620, 560)
    _polish_toolbar(window)

    central = QWidget(window)
    central.setObjectName("centralwidget")
    root = QVBoxLayout(central)
    root.setContentsMargins(40, 28, 40, 22)
    root.setSpacing(14)

    title = QLabel("PU 活动助手")
    title.setObjectName("HeroTitle")
    title.setAlignment(Qt.AlignCenter)
    subtitle = QLabel("轻松管理校园活动报名与筛选")
    subtitle.setObjectName("HeroSubtitle")
    subtitle.setAlignment(Qt.AlignCenter)
    root.addWidget(title)
    root.addWidget(subtitle)
    root.addSpacing(16)

    panel = QWidget(central)
    panel.setObjectName("LoginPanel")
    panel.setMaximumWidth(560)
    panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    panel.setMinimumHeight(320)
    panel_layout = QVBoxLayout(panel)
    panel_layout.setContentsMargins(24, 24, 24, 24)
    panel_layout.setSpacing(10)

    window.ui.username_LineEdit.setPlaceholderText("请输入学号")
    window.ui.password_LineEdit.setPlaceholderText("请输入密码")
    window.ui.password_LineEdit.setEchoMode(QLineEdit.Password)
    window.ui.lineEdit.setPlaceholderText("输入关键字筛选学校")
    window.ui.school_ComboBox.setPlaceholderText("选择学校")
    window.ui.login_PushButton.setFixedHeight(44)

    panel_layout.addWidget(_login_row("学校名称", window.ui.lineEdit))
    panel_layout.addWidget(_login_row("学校", window.ui.school_ComboBox))
    panel_layout.addWidget(_login_row("用户名", window.ui.username_LineEdit))
    panel_layout.addWidget(_login_row("密码", window.ui.password_LineEdit))

    radio_row = QHBoxLayout()
    radio_row.setContentsMargins(96, 10, 0, 0)
    radio_row.setSpacing(24)
    radio_row.addWidget(window.ui.login_on_hand_RadioButton)
    radio_row.addWidget(window.ui.auto_loginRadioButton)
    radio_row.addWidget(window.ui.use_this_token_RadioButton)
    radio_row.addStretch(1)
    panel_layout.addLayout(radio_row)

    panel_layout.addSpacing(8)
    panel_layout.addWidget(window.ui.login_PushButton)
    root.addWidget(panel, 0, Qt.AlignHCenter)
    root.addStretch(1)

    window.ui.label_2.setText("作者：星夜不荟")
    window.ui.label_2.setObjectName("MutedText")
    window.ui.label_2.setAlignment(Qt.AlignCenter)
    root.addWidget(window.ui.label_2)
    window.setCentralWidget(central)
    window.ui.centralwidget = central
    window.ui.verticalLayout = root

    _set_action_icon(window, "flush_school_lists_action", "SP_BrowserReload")
    _set_action_icon(window, "project_action", "SP_DirLinkIcon")


def style_main_window(window: QMainWindow):
    window.setWindowTitle("PU 活动助手")
    window.resize(1060, 760)
    window.setMinimumSize(860, 620)
    _polish_toolbar(window)
    _spacious_layout(window.ui.verticalLayout_2, (32, 18, 32, 18), 14)
    for layout in (
        window.ui.horizontalLayout_2,
        window.ui.horizontalLayout_5,
        window.ui.horizontalLayout_6,
        window.ui.horizontalLayout_3,
    ):
        layout.setSpacing(10)
    for label in (window.ui.label, window.ui.label_2, window.ui.label_3, window.ui.label_4):
        label.setObjectName("FormLabel")
        label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
    window.ui.label.setFixedWidth(56)
    window.ui.label_2.setFixedWidth(56)
    window.ui.label_3.setFixedWidth(76)
    window.ui.label_4.setFixedWidth(92)
    window.ui.callegory_pushButton.setText("添加类别")
    window.ui.del_cate_pushButton.setText("删除类别")
    window.ui.callegory_pushButton.setMinimumWidth(78)
    window.ui.del_cate_pushButton.setMinimumWidth(78)
    window.ui.groupBox.setMinimumHeight(88)
    window.ui.horizontalLayout_4.setContentsMargins(12, 24, 12, 10)
    window.ui.horizontalLayout_3.setSpacing(22)
    for area in (window.ui.scrollArea, window.ui.scrollArea_2, window.ui.scrollArea_3):
        area.setFrameShape(QFrame.NoFrame)
    for layout in (
        window.ui.all_acts_VBoxLayout,
        window.ui.filter_acts_VBoxLayout,
        window.ui.target_acts_VBoxLayout,
    ):
        layout.setSpacing(12)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setAlignment(Qt.AlignTop)
    window.ui.college_LineEdit.setPlaceholderText("学院")
    window.ui.grade_LineEdit.setPlaceholderText("年级，如 2023")
    window.ui.server_url.setPlaceholderText("可选：同步服务器地址")
    window.ui.callegory_comboBox.setPlaceholderText("输入或选择活动类别")
    _set_action_icon(window, "flush_action", "SP_BrowserReload")
    _set_action_icon(window, "filt_action", "SP_FileDialogContentsView")
    _set_action_icon(window, "save_config_action", "SP_DialogSaveButton")
    _set_action_icon(window, "back_login_action", "SP_ArrowBack")
    _set_action_icon(window, "link_to_server_action", "SP_DriveNetIcon")
    _insert_overview(window)


def style_log_window(window: QMainWindow):
    window.setWindowTitle("运行日志")
    window.resize(680, 560)
    _spacious_layout(window.ui.verticalLayout, (18, 18, 18, 14), 12)
    window.ui.plainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)


def style_activity_card(widget):
    widget.setObjectName("ActivityCard")
    widget.setMinimumHeight(156)
    widget.ui.horizontalLayout_2.setContentsMargins(14, 14, 16, 14)
    widget.ui.horizontalLayout_2.setSpacing(16)
    widget.ui.img_Label.setFixedSize(104, 104)
    widget.ui.img_Label.setAlignment(Qt.AlignCenter)
    widget.ui.teinfo_TextEdit.setObjectName("ActivityInfo")
    widget.ui.teinfo_TextEdit.setFrameShape(QFrame.NoFrame)
    widget.ui.teinfo_TextEdit.setReadOnly(True)
    widget.ui.teinfo_TextEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
    widget.ui.teinfo_TextEdit.setMinimumHeight(116)

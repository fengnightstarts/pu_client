# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 673)
        self.flush_action = QAction(MainWindow)
        self.flush_action.setObjectName("flush_action")
        self.flush_action.setMenuRole(QAction.MenuRole.NoRole)
        self.filt_action = QAction(MainWindow)
        self.filt_action.setObjectName("filt_action")
        self.filt_action.setMenuRole(QAction.MenuRole.NoRole)
        self.save_config_action = QAction(MainWindow)
        self.save_config_action.setObjectName("save_config_action")
        self.save_config_action.setMenuRole(QAction.MenuRole.NoRole)
        self.back_login_action = QAction(MainWindow)
        self.back_login_action.setObjectName("back_login_action")
        self.back_login_action.setMenuRole(QAction.MenuRole.NoRole)
        self.link_to_server_action = QAction(MainWindow)
        self.link_to_server_action.setObjectName("link_to_server_action")
        self.link_to_server_action.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.college_LineEdit = QLineEdit(self.centralwidget)
        self.college_LineEdit.setObjectName("college_LineEdit")

        self.horizontalLayout_2.addWidget(self.college_LineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.grade_LineEdit = QLineEdit(self.centralwidget)
        self.grade_LineEdit.setObjectName("grade_LineEdit")

        self.horizontalLayout_2.addWidget(self.grade_LineEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.callegory_comboBox = QComboBox(self.centralwidget)
        self.callegory_comboBox.setObjectName("callegory_comboBox")
        self.callegory_comboBox.setEditable(True)

        self.horizontalLayout_5.addWidget(self.callegory_comboBox)

        self.callegory_pushButton = QPushButton(self.centralwidget)
        self.callegory_pushButton.setObjectName("callegory_pushButton")
        self.callegory_pushButton.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.callegory_pushButton)

        self.del_cate_pushButton = QPushButton(self.centralwidget)
        self.del_cate_pushButton.setObjectName("del_cate_pushButton")
        self.del_cate_pushButton.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_5.addWidget(self.del_cate_pushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filt_by_category_checkBox = QCheckBox(self.groupBox)
        self.filt_by_category_checkBox.setObjectName("filt_by_category_checkBox")

        self.horizontalLayout_3.addWidget(self.filt_by_category_checkBox)

        self.default_filter_CheckBox = QCheckBox(self.groupBox)
        self.default_filter_CheckBox.setObjectName("default_filter_CheckBox")
        self.default_filter_CheckBox.setChecked(False)

        self.horizontalLayout_3.addWidget(self.default_filter_CheckBox)

        self.filt_by_tribe = QCheckBox(self.groupBox)
        self.filt_by_tribe.setObjectName("filt_by_tribe")

        self.horizontalLayout_3.addWidget(self.filt_by_tribe)

        self.filt_by_join_type_checkBox = QCheckBox(self.groupBox)
        self.filt_by_join_type_checkBox.setObjectName("filt_by_join_type_checkBox")

        self.horizontalLayout_3.addWidget(self.filt_by_join_type_checkBox)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.server_url = QLineEdit(self.centralwidget)
        self.server_url.setObjectName("server_url")

        self.horizontalLayout_6.addWidget(self.server_url)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.all_acts = QWidget()
        self.all_acts.setObjectName("all_acts")
        self.horizontalLayout = QHBoxLayout(self.all_acts)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QScrollArea(self.all_acts)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 68, 20))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.all_acts_VBoxLayout = QVBoxLayout()
        self.all_acts_VBoxLayout.setObjectName("all_acts_VBoxLayout")

        self.verticalLayout_7.addLayout(self.all_acts_VBoxLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.all_acts, "")
        self.filter_acts = QWidget()
        self.filter_acts.setObjectName("filter_acts")
        self.verticalLayout_4 = QVBoxLayout(self.filter_acts)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.filter_acts)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 380, 377))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.filter_acts_VBoxLayout = QVBoxLayout()
        self.filter_acts_VBoxLayout.setObjectName("filter_acts_VBoxLayout")

        self.verticalLayout_8.addLayout(self.filter_acts_VBoxLayout)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.filter_acts, "")
        self.target_acts = QWidget()
        self.target_acts.setObjectName("target_acts")
        self.verticalLayout_6 = QVBoxLayout(self.target_acts)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_3 = QScrollArea(self.target_acts)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 68, 20))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.target_acts_VBoxLayout = QVBoxLayout()
        self.target_acts_VBoxLayout.setObjectName("target_acts_VBoxLayout")

        self.verticalLayout_9.addLayout(self.target_acts_VBoxLayout)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.target_acts, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 424, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.flush_action)
        self.toolBar.addAction(self.filt_action)
        self.toolBar.addAction(self.save_config_action)
        self.toolBar.addAction(self.back_login_action)
        self.toolBar.addAction(self.link_to_server_action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.flush_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5237\u65b0\u5168\u90e8\u6d3b\u52a8", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.flush_action.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u91cd\u65b0\u83b7\u53d6\u6d3b\u52a8\u5217\u8868\u548c\u6d3b\u52a8\u4fe1\u606f",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filt_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5237\u65b0\u8fc7\u6ee4\u5217\u8868", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.filt_action.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\u70b9\u51fb\u4ee5\u5237\u65b0\u8fc7\u6ee4\u5217\u8868",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.save_config_action.setText(
            QCoreApplication.translate("MainWindow", "\u4fdd\u5b58\u914d\u7f6e", None)
        )
        self.back_login_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u8fd4\u56de\u767b\u5f55\u754c\u9762", None
            )
        )
        self.link_to_server_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u8fde\u63a5\u670d\u52a1\u5668", None
            )
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "\u5b66\u9662", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "\u5e74\u7ea7", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "\u6d3b\u52a8\u7c7b\u522b:", None)
        )
        self.callegory_pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u6dfb\u52a0", None)
        )
        self.del_cate_pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u5220\u9664", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u8fc7\u6ee4\u9009\u9879", None)
        )
        # if QT_CONFIG(tooltip)
        self.filt_by_category_checkBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u8fc7\u6ee4\u975e\u9009\u5b9a\u7c7b\u522b\u7684\u6d3b\u52a8</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filt_by_category_checkBox.setText(
            QCoreApplication.translate(
                "MainWindow", "\u9009\u5b9a\u6d3b\u52a8\u7c7b\u522b", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.default_filter_CheckBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u8fc7\u6ee4\u4eba\u6570\u5df2\u6ee1\u3001\u62a5\u540d\u65f6\u95f4\u5df2\u7ed3\u675f\u3001\u4e0d\u5141\u8bb8\u81ea\u5df1\u5b66\u9662\u3001\u5e74\u7ea7\u62a5\u540d\u7684</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.default_filter_CheckBox.setText(
            QCoreApplication.translate("MainWindow", "\u9ed8\u8ba4\u8fc7\u6ee4", None)
        )
        # if QT_CONFIG(tooltip)
        self.filt_by_tribe.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u8fc7\u6ee4\u53ea\u5141\u8bb8\u7279\u5b9a\u90e8\u843d\u62a5\u540d\u7684\u6d3b\u52a8</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filt_by_tribe.setText(
            QCoreApplication.translate(
                "MainWindow", "\u7279\u5b9a\u90e8\u843d\u6d3b\u52a8", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.filt_by_join_type_checkBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u8fc7\u6ee4\u62a5\u540d\u9700\u5ba1\u6838\u7684\u6d3b\u52a8</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filt_by_join_type_checkBox.setText(
            QCoreApplication.translate(
                "MainWindow", "\u62a5\u540d\u9700\u5ba1\u6838", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", "\u670d\u52a1\u5668\u5730\u5740\uff1a", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.all_acts),
            QCoreApplication.translate("MainWindow", "\u5168\u90e8\u5217\u8868", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.filter_acts),
            QCoreApplication.translate("MainWindow", "\u8fc7\u6ee4\u5217\u8868", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.target_acts),
            QCoreApplication.translate("MainWindow", "\u62a5\u540d\u5217\u8868", None),
        )
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "toolBar", None)
        )

    # retranslateUi
